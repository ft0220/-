from pyquery import PyQuery as pq

d=pq(url="https://kabutan.jp/stock/?code=7203")
d.make_links_absolute("https://kabutan.jp/stock/?code=7203")
print(d)

