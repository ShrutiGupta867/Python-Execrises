# 4) Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
#
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#Meyhod-1
# dict_1= dict(zip(keys, values))
# print(dict_1)

#Method-2
dict_1={}
for i in range(len(keys)):
    dict_1.update({keys[i]: values[i]})
print(dict_1)


