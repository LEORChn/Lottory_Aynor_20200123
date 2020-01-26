
import os
from leorchn.lib import *
from leorchn.TablePrinter import TablePrint

if __name__ == '__main__':
	pass

has_more = 1
count = 1
tab = TablePrint()
tab.inputHead('No', 'Name', 'Uid', 'Time')
url = 'https://api.vc.bilibili.com/dynamic_repost/v1/dynamic_repost/repost_detail?dynamic_id=347521373177424315'
offset = ''
while has_more == 1:
	j = httpj(f'get '+ url + offset)
	for obj in j['data']['items']:
		k = obj['desc']
		uname = k['user_profile']['info']['uname']
		uid = k['uid']
		time = datetime.fromtimestamp(k['timestamp']).astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')
		tab.input(count, uname, uid, time)
		count += 1
	os.system('cls')
	tab.print()
	has_more = j['data']['has_more']
	if has_more == 1:
		offset = '&offset=' + j['data']['offset']
os.system('pause')