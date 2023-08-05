h1 = int(input("Enter hour 1 :"))
m1 = int(input("Enter minute 1 :"))
s1 = int(input("Enter second 1 :"))
h2 = int(input("Enter hour 2 :"))
m2 = int(input("Enter minute 2 :"))
s2 = int(input("Enter second 2 :"))
s = s1+s2
m = m1+m2
h = h1+h2
if(s>=60):
    s = s-60
    m = m+1
if(m>=60):
    m = m-60
    h = h+1
if(h>=24):
    h = h-24
print("The time is ",h,"hours",m,"minutes and ",s,"seconds")