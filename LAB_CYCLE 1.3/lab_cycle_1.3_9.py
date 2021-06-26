data={"Anja":100,"Joshy":200,"Hobby":35}

list1=list(data.items())

list1.sort()
print("Ascending Order ",list1)

list2=list(data.items())
list2.sort(reverse=True)
print("DEs Order ",list2)