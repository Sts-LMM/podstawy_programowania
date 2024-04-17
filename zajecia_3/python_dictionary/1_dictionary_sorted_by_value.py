import operator

def sort_desc(d):
    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_d

def sort_asc(d):
    sorted_a = dict(sorted(d.items(), key=operator.itemgetter(1)))
    return sorted_a

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
	
print('Original dictionary:', d)
print('Dictionary in ascending order by value:', sort_asc(d))
print('Dictionary in descending order by value:', sort_desc(d))
