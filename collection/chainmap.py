from collections import deque, ChainMap
import os, argparse
from rich import print

"""
一个 ChainMap 将多个字典或者其他映射组合在一起，创建一个单独的可更新的视图。 如果没有 maps 被指定，就提供一个默认的空字典，这样一个新链至少有一个映射。
"""

toys = {'blocks': 30, "Monopoly": 20}
computers = {'Dell': 4000, "Macbook pro": 12000}
clothing = {'Jeans': 50, "T-Shirt": 50}

collection_set = ChainMap(toys, computers, clothing)
print(collection_set)
print(collection_set.get("T-Shirt"))
print(list(collection_set))

com = toys.copy()
com.update(toys)
print(list(com))

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()

print(namespace)
print(vars(namespace))
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}
combined = ChainMap(command_line_args, os.environ, defaults)
print(defaults)
print(combined['color'])
print(combined['user'])

########################################################################################################################
c = ChainMap()
d = c.new_child()
e = c.new_child()

print(c)
print(d)
print(e)
e.maps[0] = {"a": 22222}
print(e)
print(c.get("a"))
print(list(e))

d['x'] = 1
print(d['x'])
del d['x']
print(d)
