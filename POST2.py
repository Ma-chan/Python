with urllib.request.urlopen('https://judgeapi.u-aizu.ac.jp/users/matty007') as res:
...     html=res.read().decode("utf-8")
...     print(html)
