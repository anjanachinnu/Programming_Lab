list1=[2,4,5,6]
list2=[2,3,4,8]
common=[]

sum1=sum(list1)
sum2=sum(list2)
if len(list1)==len(list2):
    print("\nTow lists are of same length")
else:
    print("\nTwo Lists are of Unequal Length")
if sum(list1)==sum(list2):
    print("\nThe Lists are of Same Sum")
else:
    print("\nThe Lists of Sum are not equal")
