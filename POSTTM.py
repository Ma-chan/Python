import time
>>> import urllib
>>> import urllib2
>>> if __name__ == '__main__':
...     start=time.time()
...     url="http://judge.u-aizu.ac.jp/onlinejudge/finder.jsp?course=ITP1"
...     param=[("id",0),("param","dammy")]
...     url+="?{0}".format(urllib.urlencode(param))
...     result=None
...     try:
...             result=urllib.urlopen(url).read()
...     except ValueError:
...             print("アクセスに失敗しました。")
...     elapsed_time=time.time()-start
...     print("elapsed_time:{0}".format(elapsed_time)+"[sec]")
