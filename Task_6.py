# Read the given file and store them in a list of dictionaries.
#
# eg:
# 0: Merry is boiling matrass while Dog is meowing for coffee.
# 1: Jeniffer is kissing tea while Dog is meowing for kettle.
#
# expected output:
# [
#
# {"0": "Merry is boiling matrass while Dog is meowing for coffee."}
# ,
#
# {"1": "Jeniffer is kissing tea while Dog is meowing for kettle."}

#Write a File with the help of With
with open('file.txt','w') as f:
 f.write("0: Merry is boiling matrass while Dog is meowing for coffee.\n")
 f.write("1: Jeniffer is kissing tea while Dog is meowing for kettle.")

#Here try to read a file
l=[]
with open('file.txt','r') as f:
    for i in f:
        t=i.split(': ')
        it = iter(t)
        s=dict(zip(it,it))
        l.append(s)

print(l)



















