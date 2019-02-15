with urllib.request.urlopen('https://judgeapi.u-aizu.ac.jp/users/yatt') as res:
...     html=res.read().decode("utf-8")
...     print(html)
