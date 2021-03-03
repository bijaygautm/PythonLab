i=10
while i>=1:
    print(i)
    i-=1
print("program is over")

#WAP to print all the odd and even number with appropriate message from 1 to 50.

i=1
while i<=50:
    if i % 2==0:
        print(i,":even")
    else:
        print(i,":odd")
    i=i+1


# wap to find the sum of elements of list using while loop

lst = [1, 2, 3, 4, 5, 6]
sum=0
for i in lst:
    sum = sum + i
print('the sum is', sum)
