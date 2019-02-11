import urllib
import urllib2
url="http://judge.u-aizu.ac.jp/onlinejudge/finder.jsp?course=ITP1"
params = {"id":0, "param" : "dammy" }
params = urllib.urlencode(params)
req = urllib2.Request(url)
res = urllib2.urlopen(req)
