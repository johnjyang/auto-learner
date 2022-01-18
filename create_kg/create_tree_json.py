from get_data import *
import json

s_1 = get_data("summaries_1")
c_1 = get_data("clusters_1")
s_0 = get_data("summaries_0")
c_0 = get_data("clusters_0")

# list of string -> list of s_0
c_1_split = []
for c in c_1:
    tmp_split = c.split(', ')
    c_1_split.append(tmp_split)

# convert list of s_0 to list of index in s_0
c_1_index = []
for c in c_1_split:
    tmp_c = []
    for s in c:
        tmp_c.append(s_0.index(s))
    c_1_index.append(tmp_c)

# list of string -> list of searches
c_0_split = []
for c in c_0:
    tmp_split = c.split(', ')
    c_0_split.append(tmp_split)

# list of index in s_0 -> list of [sum_0, [searches]]
sum_0_t = []
for c in c_1_index:
    tmp_c = []
    for s in c:
        tmp_c.append(s_0[s])
        tmp_c.append(c_0_split[s])
    sum_0_t.append(tmp_c)

# list of [sum_0, [searches]] -> list of [sum_1, [sum_0, [searches]]]
sum_1_t = []
for s in range(len(s_1)):
    tmp_c = []
    tmp_c.append(s_1[s])
    tmp_c.append(sum_0_t[s])
    sum_1_t.append(tmp_c)

# list of [sum_1, [sum_0, [searches]]] -> {"id": sum_1, "name": sum_1, children: [{[sum_0, [searches]]}]}
data = {
    "id": "John's Search History",
    "name": "John's Search History",
    "children": []
}
children = []
word_list = []

for s in range(len(sum_1_t[:50])):
    dict_0 = {
        "id": sum_1_t[s][0] + "_0",
        "name": sum_1_t[s][0],
        "collapsed": True,
        "children": []
    }
    children_0 = []

    for s1 in range(0, len(sum_1_t[s][1]), 2):
        dict_1 = {
            "id": sum_1_t[s][1][s1] + "_1",
            "name": sum_1_t[s][1][s1],
            "collapsed": True,
            "children": []
        }
        children_1 = []

        for s2 in range(len(sum_1_t[s][1][s1 + 1])):
            if not sum_1_t[s][1][s1 + 1][s2] in word_list:
                dict_2 = {
                    "id": sum_1_t[s][1][s1 + 1][s2] + "_2",
                    "name": sum_1_t[s][1][s1 + 1][s2],
                    "collapsed": True,
                }
                children_1.append(dict_2)
                word_list.append(sum_1_t[s][1][s1 + 1][s2])

        dict_1["children"] = children_1
        children_0.append(dict_1)

    dict_0["children"] = children_0
    children.append(dict_0)

data["children"] = children
data = json.dumps(data)

# write json file
with open('./frontend/search_tree.json', 'w') as outfile:
    outfile.write(data)
