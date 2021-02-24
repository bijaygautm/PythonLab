#WAP N students take K apple and distribute them among each other evenly. The reamaining parts
# remain in the basket. How many apples will each single student get? How many apples will reamin in the basket?
# The program reads the number N and K. It should print the two answers for the question above.

stdN = int(input("no of students"))
appK = int (input("no of apples"))

dist = int(appK/stdN)

print("each student will get", dist, "apple")

rem = appK - stdN*dist

print ( " the remaining apple is", rem)
