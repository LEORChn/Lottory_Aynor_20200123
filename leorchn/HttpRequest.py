import urllib.request
import urllib.parse
import gzip

def dictization(dat, linebreak: str, kvbreak: str): # 字典格式化
	if isinstance(dat, dict): return dat
	elif isinstance(dat, str):
		dit = {}
		for q in dat.split(linebreak):
			q = q.split(kvbreak, 1) # 分割限制=1，即分割成两份
			if len(q) == 2: dit[q[0].strip()] = q[1].strip()
		return dit

def httpq(*args):
	method = url = ''
	head, form = {}, {}
	ftype = 0
	for p in (args[0] if isinstance(args[0], tuple) else args):
		if p == None:
			raise ValueError('{} 值为 None。如果真的需要留空，请使用空字符串而不是 None。'.format('Method,Url,Head,Formed'.split(',')[ftype]))
		elif ftype == 0:
			s = p.split(' ', 2)
			method = s[0].upper()
			if len(s) > 1:
				ftype += 1
				url = s[1]
		elif ftype == 1: url = p
		elif ftype == 2: head = dictization(p.replace('\r', ''), '\n', ':')
		elif ftype == 3: form = dictization(p, '&', '=')
		ftype += 1
	if url.startswith('s:'): url = url.replace('s:', 'https://', 1)
	if not url.startswith('http://') and not url.startswith('https://'):
		url = 'http://' + url
	requst = urllib.request.Request(url, headers=head, method=method)
	form = urllib.parse.urlencode(form).encode('utf8')
	return urllib.request.urlopen(requst, data=form)

def http(*args):
	result = httpq(args[0] if isinstance(args[0], tuple) else args)
	response = result.read()
	charset = 'UTF-8'
	resinfo = result.info()
	if 'Content-Encoding' in resinfo:	# 自动完成数据解压
		if resinfo['Content-Encoding'] == 'gzip':
			response = gzip.decompress(response)
	if 'Content-Type' in resinfo:		# 自动完成文本编码解码
		ct = resinfo['Content-Type']
		if ct.__contains__('charset='):
			charset = ct.split('charset=')[1].split(';')[0]
	return response.decode(charset)
