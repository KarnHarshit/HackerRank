#1 Write a Python Program to find the print sum, average of all numbers, smallest and
# largest element of a list.
l1 = list()

n = int(input ("Enter the number of elements:"))
for i in range(n):
    ele = int (input ("Enter the element: "))
    l1.append(ele)

largest  = max(l1)
smallest = min(l1)
average = sum(l1) / len(l1)
print ("Largest of elements of ", l1, "is: ", largest )
print ("Smallest of elements of ", l1, "is: ", smallest )
print ("Average of list", l1, "is: ", average )