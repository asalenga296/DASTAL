def count(arr,n):
    c=0
    for i in arr:
        if i==n:
            c+=1
    return c

#declaring given array
x=[2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]
print("Given array is",x)
#access 89 and 90 from array x
print(x[5],x[9])
#printing array elements from index 1 to 8
print("Elements from 1 to 8: ")
for i in range(1,9):
    print(x[i],end=' ')
print()
#cllaing count function by passing x,5
print("count of 5's in array are: ")
print(count(x,5))
#Adding the element 42 and dropping elements 89, 90, and 65
x.append(42)
x.remove(89)
x.remove(90)
x.remove(65)
print("Updated array after removing 89,90 and 65 and adding 42: ")
print(x)
s=0
for i in x:
    s+=i
print("Sum of elements of array x is:",s)