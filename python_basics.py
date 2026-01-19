print("Hello World!")

#Add two digit
a=20
b=10
print('Sum of',a,'and',b,'is:',a+b)

#print data type of variable
a=3.14
type(a)#float
b=2
type(b)#int
c='dhaka'
type(c)#str


#assign values in a single line
a,b,c = 100,8.9,"xyz" 
print(a,b,c) 


# single line comment
"""
multi line comment
"""


# type casting
x=int(3.345678) #assign as 3 
y=str(123)  #assign as "123" 
z=float(2)  #assign as 2.0 
print (x,y,z)


# String operations
s="Md.Sarawer Bhuiyan"
print(s)
print(s[0:10]) # print characters starting from 1 to 10
print(s[3:])   # print characters starting from 3 to end
print(s*2)     #print string s two times
print(s+'abc') #print concatenated string


#list
list=["abc",100,3.14,'xyz'] #we can store diffrent types of data in list
list[0]='x' #we can modify any element in list
print(list)
print(list[0])
print(list[1:3])
type(list)


#'tuple'
tp=(5,7,'aaa',67.45)
print(tp)
print(tp[3])
#tp[3]=3.14  ##'tuple' object does not support item assignment
type(tp)


# range(start,stop,steps)
for i in range (1,10,2):   
    print(i)    


# Dictionary
dx={'name':'sarawer','ID':'528','Age':23}
print(dx)
type(dx)
print(dx['name'])
print(dx['ID'])
print(dx['Age'])
print(dx.keys())   #print all keys
print(dx.values()) #print all values


#user input
x=input('enter 1st number:')
y=input('enter 2st number:')
print(x+y)  #if x=2 & y=3 it prints 23.by default user input is a string

x=int(input('enter 1st number:'))
y=int(input('enter 2st number:'))
print(x+y) #if x=2 & y=3 it prints 5


#separator
print(1,2,3,4,5) #by default all elements are separated by a space
print(1,2,3,4,5,sep=',') #seperate by ,
print(1,2,3,4,5,sep='') #for no seperation we can use separate by empty string.



#floor division
print(100//14)


#exponent
print(5**2)


#modulo
print(5%2) 
print(-5%2) #positive 
print(5%-2) #negetive..if devident is negetive then mod will be negetive



##the operator listed at the top of the list will be execute first
'''
1-> ()
2-> **
3-> %,*,/,//
4-> +,-
'''
print(10+4*5)


#Add and assign
x=5
x+=5
print(x)
#sub and assign
y=10
y-=5
print(y)
#multiply and assign
a=5
a*=5
print(a)
#divide and assign 
b=25
b/=5
print(b)
#module and assign
c=15
c%=4
print(c)
#floor division and assign
d=25
d//=5
print(d)
#Exponentiation and assign
e=2
e**=3
print(e)


#Bitwise AND
print(5&3) 
'''
5-> 0101
3-> 0011
----------
    0001  (1)
'''
#Bitwise OR
print(5|3) 
'''
5-> 0101
3-> 0011
----------
    0111  (7)
'''
#Bitwise XOR
print(5^3) 
'''
5-> 0101
3-> 0011
----------
    0110  (6)
'''
#Bitwise NOT
print(~5) 
'''
~x = -(x + 1)
'''
#bitwise left shift
print(3<<2)
'''
0011 -> 001100(12)
'''
#bitwise right shift
print(8>>2)
'''
1000 -> 0010(2)
'''



