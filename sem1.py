#ex1
#n=700
#m=750
#print((m+n-1)//n)

# ex2
#n=20
#m=21
#v=22
#print((m+n+v+1)//2)

#ex4
year=int(input('введите год: '))
if year % 4==0 and year % 100!= 0 or year % 400 == 0:
    print ('yes')
else:
     print ('no')