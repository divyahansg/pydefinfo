import os
import sys
import argparse
import jedi
import logging
from structures import *

logger = logging.getLogger("pydefinfo")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

parser = argparse.ArgumentParser()
parser.add_argument('-l','--line', type=int)
parser.add_argument('-c','--col', type=int)
parser.add_argument('-f','--filename')
args = parser.parse_args()
source = sys.stdin.read()

def normalize(p):
	""" Transform p to Unix-style by replacing backslashes """
	return p.replace('\\', '/')

class SourceGrapher():
	def __init__(self, source, file, line, col):
		self._source = source
		self._file = file
		self._line = line
		self._col = col
		self._abs_base_dir = os.path.abspath(os.getcwd())
		self._syspath = sys.path
		self._stdlibpaths = []
		for p in self._syspath:
			if not p.endswith('site-packages'):
				self._stdlibpaths.append(p)

	def get_def(self):
		jedi_script = jedi.Script(source=self._source, line=self._line, column=self._col, path='')
		definitions = jedi_script.goto_definitions()
		for d in definitions:
			logger.debug(
				'processing def: %s | %s | %s',
				d.desc_with_module,
				d.name,
				d.type,
			)
			sg_def = self._jedi_def_to_def_key(d)
			print (sg_def.Repo)
			print (sg_def.Unit)
			print (sg_def.UnitType)
			print (sg_def.Path)
			print (normalize(self._file))	

	def _jedi_def_to_def_key(self, d):
		path, dep = self._full_name_and_dep(d)
		if dep is not None:
			repo, unit, unit_type = dep.Repo, dep.Name, dep.Type
		else:
			repo, unit, unit_type = "", self._unit, self._unit_type
		return DefKey(
			Repo=repo,
			Unit=unit,
			UnitType=unit_type,
			Path=path,
		)

	def _full_name_and_dep(self, d):
		if d.in_builtin_module():
			return d.full_name, UnitKey(Repo=STDLIB_UNIT_KEY.Repo, Type=UNIT_PIP, Name="__builtin__", CommitID="", Version="")

		if d.module_path is None:
			raise Exception('no module path for definition %s' % repr(d))

		# This detects `self` and `cls` parameters makes them to point to the class:
		# To trigger this parameters must be for a method (a class function).
		if d.type == 'param' and (d.name == 'self' or d.name == 'cls') and d.parent().parent().type == 'class':
			d = d.parent().parent()

		module_path, is_internal = self._rel_module_path(d.module_path)
		if module_path is None:
			raise Exception('could not find name for module path %s' % d.module_path)

		if self._jedi_def_is_ivar(d):
			classname = self._jedi_def_ivar_classname(d)
			path = '{}/{}.{}'.format(module_path, classname, d.name)
		else:
			path = '{}/{}.{}'.format(module_path, d.full_name, d.name)

		dep = None
		if not is_internal:
			dep, err = self._module_to_dep(module_path)
			if err is not None:
				raise Exception(err)

		return path, dep

	def _rel_module_path(self, module_path):
		if module_path.startswith(self._abs_base_dir):
			return normalize(os.path.relpath(module_path, self._abs_base_dir)), True # internal

		for p in self._syspath:
			if p == '':
				continue
			if module_path.startswith(p):
				return normalize(os.path.relpath(module_path, p)), False # external

		if self._virtual_env is not None and module_path.startswith(self._virtual_env):
			module_path = normalize(os.path.relpath(module_path, self._virtual_env))
			return module_path.split('/site-packages/', 1)[1], False

		return None, False

	def _jedi_def_is_ivar(self, df):
		try:
			return (df.parent().type == 'function' and
					df.parent().parent().type in ['class', 'instance'] and
					df.description.startswith('self.'))
		except:
			return False

	def _jedi_def_ivar_classname(self, df):
		return '.'.join(df.full_name.split('.')[:-1])

	def _module_to_dep(self, m):
		# Check explicit pip dependencies
		"""
		for pkg, dep in self._modulePathPrefixToDep.items():
			if m.startswith(pkg):
				return dep, None
		"""
		for stdlibpath in self._stdlibpaths:
			if os.path.lexists(os.path.join(stdlibpath, m)):
				# Standard lib module
				return UnitKey(Repo=STDLIB_UNIT_KEY.Repo,
							   Type=STDLIB_UNIT_KEY.Type,
							   Name=STDLIB_UNIT_KEY.Name,
							   CommitID=STDLIB_UNIT_KEY.CommitID,
							   Version=STDLIB_UNIT_KEY.Version), None
		return None, ('could not find dep module for module %s, candidates were %s' % (m, repr(self._modulePathPrefixToDep.keys())))


srcgrapher = SourceGrapher(source, args.filename, args.line, args.col)
srcgrapher.get_def()

