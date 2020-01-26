
from leorchn.HttpRequest import httpq as h1
from leorchn.HttpRequest import http as h2
from leorchn.Time import *
import json as fson
import os, sys, logging, hashlib
def pl(*args):
	for s in args: print(s, end='')
	print('')
def trace(e):
	if isinstance(e, BaseException): logging.exception(e)
	else:
		try: return e()
		except BaseException as e2: trace(e2)

__httpDebugPrint = False
def __hdp(args, c=None): # HTTP 调试总控
	s= ''
	try:
		s = h2(args)
		if __httpDebugPrint: print(s)
	except BaseException as e:
		pl('{}\n-> {}'.format(args[0], e.__str__()))
	return '{}' if s == '' and c == dict else s

def setHttpDebugPrint(b: bool = False): global __httpDebugPrint; __httpDebugPrint = b
def getHttpDebugPrint(): return __httpDebugPrint
def http(*args): return __hdp(args)
def httpl(*args): print(h2(args))
def httpq(*args): return h1(args)
def httpj(*args): return fson.loads(__hdp(args, dict))
def json(s:str): return fson.loads(s)
def json_dump(d): return fson.dumps(d)

def print_sys_path():
	for p in sys.path: pl(p)
def md5(s: str):
	m = hashlib.md5()
	m.update(s.encode(encoding='utf-8'))
	return m.hexdigest()

def mkdirs(path:str, force:bool=False):
	if os.path.exists(path):
		return not os.path.isfile(path)
	else:
		try:
			os.makedirs(path)
			return True
		except:
			return False

def mkdirs_forfile(path:str):
	return mkdirs(os.path.dirname(path))
'''
def regMatch(text:str, regex:str, index:int=0): # index=返回的数据位置。-1=返回整个数组
	return rM(text, regex, index)

def regSplit(text:str, regex:str, max:int=0):
	return rS(text, regex, max)
'''
import urllib.parse
def encodeURI(s, encode='utf8'): return urllib.parse.quote(s.encode(encode))
def decodeURI(s, encode='utf8'): return urllib.parse.unquote(s, encode)

os.system('title YOU ARE RUNNING leorchn.lib LITE VERSION, DO NOT MERGE THIS VERSION TO MASTER BRANCH!')
