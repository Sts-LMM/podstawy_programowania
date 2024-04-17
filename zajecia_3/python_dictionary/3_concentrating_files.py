def concentrate(dic1,dic2,dic3):
    for d in (dic1, dic2, dic3):
        dic4.update(d)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
print('Dictionary before concentration:',dic4) 
concentrate(dic1,dic2,dic3)
print('Dictionary after concentration:',dic4) 
