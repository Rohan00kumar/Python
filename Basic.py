'''
#bsic tupple declearation
tup=(1,3,34,56,67)
print(tup)

#hetrogeneous tupple
tup1=(1,1,3,4,5,'Rohan','Game')
print(tup1)

#Initialization
tup2=(1,2,3,4)
a,b,c,d = tup2
print(c)

#Unpacking tupple
a,b,*c =tup
print(*c)
a,*b,c = tup
print(*b)
'''

#adding iteam in tupple
tup = (1,3,4)
tup2 = (2,4,6,8)
print(tup+tup2)