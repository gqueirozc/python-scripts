firstnumber =1
lastnumber =1
i=int(input("Select the size of numbers for the sequence: "))

print(firstnumber)
print(lastnumber)
while i!=0:
    fibonnaci = firstnumber + lastnumber
    print(fibonnaci)
    firstnumber = lastnumber
    lastnumber = fibonnaci
    i-=1

input()