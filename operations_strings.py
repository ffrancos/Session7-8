s1=("hello")
s2=("world")
print(s1+" "+s2)
print(3*s2)
#len function gives you the size of the string
print(3*s2,len(3*s2))
for c in s2:
    print(c*4)

new_string=""
for c in s2:
    new_string+=c*4
print(new_string)
print("h" in s1)
print("d"in s2)
print("x"in s1)
print("wor" in s2)

