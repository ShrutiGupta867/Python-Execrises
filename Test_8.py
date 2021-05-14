# Read the file and store the data in the list as shown below:
# Use try except block for error handling
#
# expected output:
# [
#
# {"id": 0, "data": "Bill is shouting at egg while Dog is shouting at tea."}
# ,
#
# {"id": 1, "data": "Jeniffer is kissing fish while Grandfather is boiling egg."}]

# with open("Test_8.txt",'w') as f:
#     f.write('"id": 0, "data": "Bill is shouting at egg while Dog is shouting at tea." \n')
#     f.write('"id": 1, "data": "Jeniffer is kissing fish while Grandfather is boiling egg."')

try:
    name=input('Enter filename : ')
    f= open(name,'r')
    d = f.read().splitlines()
    l = list()
    p = list()
    for x in d:
        m=x.split(',')
        l.append(m)

    for i in l:
        d1=dict()
        for j in i:
            t=j.split(': ')
            it= iter(t)
            d1.update(zip(it,it))
        p.append(d1)

    print(p)

except IOError:
    print('File not Exits')






