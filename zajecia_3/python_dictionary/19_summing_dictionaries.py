def sum_dict(obj_1,obj_2):
    summary={}
    for key in obj_1.keys() | obj_2.keys():
        summary[key] = obj_1.get(key,0) + obj_2.get(key,0)
    return summary

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
summed = sum_dict(d1,d2)
print(summed)