from typing import List, Dict, Tuple, NamedTuple, Union, Any

class UnitKey:
	def __init__(self, Name, Type, Repo="", CommitID="", Version=""):
		self.Name = Name
		self.Type = Type
		self.Repo = Repo
		self.CommitID = CommitID
		self.Version = Version

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

UNIT_PIP = "PipPackage"
STDLIB_UNIT_KEY = UnitKey(
    Name = 'Python',
    Type = UNIT_PIP,
    Repo = 'github.com/python/cpython',
    CommitID = '',
    Version='',
)
BUILTIN_UNIT_KEY = UnitKey(
    Name = '__builtin__',
    Type = UNIT_PIP,
    Repo = 'github.com/python/cpython',
    CommitID = '',
    Version = '',
)

DefKey = NamedTuple('DefKey', [
    ('Repo', str),
    ('Unit', str),
    ('UnitType', str),
    ('Path', str),
])