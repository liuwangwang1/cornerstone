from collections import Counter

c = Counter()
print(c)
c = Counter("alllll")
print(c)
print(c['l'])
c = Counter({"red": 4, "blue": 2})
print(c)
c = Counter(cats=4, dogs=8)
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d = sorted(c.elements())
print(d)
c = Counter("sdasdsadasdasdasd").most_common(6)
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

d = sum(c.values())
print(d)
print(c.clear())
print(list(c))
print(dict(c))
