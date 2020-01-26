import time
from datetime import datetime, timezone, timedelta

def time10(setted:str=None, format:str=None):
	return int(datetime.strptime(setted, format).timestamp()) if setted else int(time.time())

def time13(setted:str=None, format:str=None):
	return time10(setted, format) * 1000

def nowdate(timezone_hour_shift:int=8):
	return datetime.fromtimestamp(time10()).astimezone(timezone(timedelta(hours=timezone_hour_shift)))

def timeshift(d:datetime, year:int=0, month:int=0, day:int=0, hour:int=0, minute:int=0, second:int=0):
	y, m = d.year + year, d.month + month
	while m > 12: y, m = y + 1, m - 12
	while m < 1:  y, m = y - 1, m + 12
	sd = d.replace(year=y, month=m)
	return sd + timedelta(days=day, hours=hour, minutes=minute, seconds=second)