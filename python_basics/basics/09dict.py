#!/usr/bin/env python
# coding:utf-8
import copy

citys = ["Beijing", "Shanghai", "Jinan", "Qingdao"]
city_codes = ["010", "021", "0531", "0532"]

for i in range(len(citys)):
    print("{} : {}".format(citys[i], city_codes[i]))
print("\n")

d = {}
d["name"] = "bambrow"
print(d)
d["age"] = 22
d["height"] = 1.79
print(d)
e = {11: 'a', 22: 'b', 33: 'c', 44: 'd'}
print(e)
del e[44]
print(e)
print("\n")

website = (["Go", "Google"], ["Ba", "Baidu"], ["Bi", "Bing"])
print(dict(website))
webpage = dict(Gi="GitHub", Bi="BitBucket")
print(webpage)
facebook = {}.fromkeys(("Fa", "Fb"), "Facebook")
print(facebook)
print("\n")

print(len(d))
print("age" in d)
webpage.update(dict(website))
webpage.update(facebook)
print(webpage)
webpage.pop("Fb")
print(webpage)
print(webpage.get("Bi"))
print("Bi" in webpage)
print(list(webpage.keys()))
print(list(webpage.values()))
print(list(webpage.items()))
print("\n")

for k in webpage:
    print(k, end=' ')
print("\n")

for v in list(webpage.values()):
    print(v, end=' ')
print("\n")

for k,v in list(webpage.items()):
    print(k, ":", v, end=' ')
print("\n")

f = d
g = d.copy()
print(id(d))
print(id(f))
print(id(g))
print("\n")

d[55] = ["q", "w", "e", "r"]
h = d.copy()
print(id(d))
print(id(h))
d[55].remove("r")
print(d)
print(h)
print("\n")

print(id(d[55]))
print(id(h[55]))
print("\n")

h = copy.deepcopy(d)
print(id(d[55]))
print(id(h[55]))
d[55].remove("e")
print(d)
print(h)
print("\n")

d.clear()
print(d)
print("\n")

letter = e.get(33)
print(letter)
letter = e.get(55, "Instead")
print(letter)
print(e)
letter = e.setdefault(55, "Instead")
print(letter)
print(e)
print("\n")

print(e.popitem())
# randomly delete and return
print(e)
