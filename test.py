"""
Stdlib modules defined in vanilla Python (3.5)
"""
import abc
import aifc
# import antigravity
import argparse
import ast
import asynchat
import asyncio
import asyncore
import base64
import bdb
import binhex
import bisect
import bz2
import calendar
import cgi
import cgitb
import chunk
import cmd
import codecs
import codeop
import code
import collections
import colorsys
import compileall
import concurrent
import configparser
import contextlib
import copy
import copyreg
import cProfile
import crypt
import csv
import ctypes
import curses
import datetime
import dbm
import decimal
import difflib
import dis
import distutils
import doctest
import dummy_threading
import email
import encodings
import enum
import filecmp
import fileinput
import fnmatch
import formatter
import fractions
import ftplib
import functools
import genericpath
import getopt
import getpass
import gettext
import glob
import gzip
import hashlib
import heapq
import hmac
import html
import http
import idlelib
import imaplib
import imghdr
import importlib
import imp
import inspect
import io
import ipaddress
import json
import keyword
import lib2to3
import linecache
import locale
import logging
import lzma
import macpath
import macurl2path
import mailbox
import mailcap
import mimetypes
import modulefinder
import multiprocessing
import netrc
import nntplib
import ntpath
import nturl2path
import numbers
import opcode
import operator
import optparse
import os
import pathlib
import pdb
import pickle
import pickletools
import pipes
import pkgutil
import platform
import plistlib
import poplib
import posixpath
import pprint
import profile
import pstats
import pty
import pyclbr
import py_compile
import pydoc_data
import pydoc
import queue
import quopri
import random
import reprlib
import re
import rlcompleter
import runpy
import sched
import selectors
import shelve
import shlex
import shutil
import signal
import site
import smtpd
import smtplib
import sndhdr
import socket
import socketserver
import sqlite3
import sre_compile
import sre_constants
import sre_parse
import ssl
import statistics
import stat
import stringprep
import string
import struct
import subprocess
import sunau
import symbol
import symtable
import sysconfig
import tabnanny
import tarfile
import telnetlib
import tempfile
import test
import textwrap
# import this
import threading
import timeit
import tokenize
import token
import traceback
import tracemalloc
import trace
import tty
# import turtle
import types
import typing
import unittest
import urllib
import uuid
import uu
import venv
import warnings
import wave
import weakref
import webbrowser
import wsgiref
import xdrlib
import xml
import xmlrpc
import zipapp
import zipfile

"""
From-imports
"""
from os import path
from os.path import basename

"""
Reference stuff inside packages
"""
def argparse_example():
    parser = argparse.ArgumentParser(description='ddd')
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

from datetime import timedelta
def datetime_example():
    year = timedelta(days=365)

def os_example():
    os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
    os.path.commonpath(['/usr/lib', '/usr/local/lib'])
