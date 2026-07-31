n=int(input("Enter the number: "))
mid=(n)//2
for i in range(n):
    for j in range(n):
        if(i==mid or j==mid):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()


for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if(i>j):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if(i<j):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if(i==j or (i+j)==n-1):
            print("   ",end=" ")
        else:
            print(" * ",end=" ")
    print()


for i in range(n):
    for j in range(n):
        if i >= j:
            if j == 0 or i == n - 1 or i == j:
                print(" * ", end=" ")
            else:
                print("   ", end=" ")
        else:
            print("   ", end=" ")
    print()


for i in range(n):
    for j in range(n):
        if i<=j:
            if(i==0 or j==n-1 or i==j):
                print(" * ",end=" ")
            else:
                print("   ",end=" ")
        else:
            print("   ",end=" ")
    print()