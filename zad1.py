first = second = third = "Python 2023"
#a
print(first == second)
print(second == third)

#b
print
print("first: "+str(type(first))+" "+hex(id(first)))
print("second: "+str(type(second))+" "+hex(id(second)))
print("third: "+str(type(third))+" "+hex(id(third)))

third = "Java 11"
print("After chainging value of third:")
print(first == second)
print(second == third)

#b
print
print("first: "+str(type(first))+" "+hex(id(first)))
print("second: "+str(type(second))+" "+hex(id(second)))
print("third: "+str(type(third))+" "+hex(id(third)))
