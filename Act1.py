#Numpy - Numerical Python
import numpy as np
a=[1,2,3,4,5]
print(type(a))
b=np.array(a)
print(type(b))

#Creating an Array
c=np.array([1,2,3,4,5])
print(type(c))
c=c+10
print(c)

#a=a+1
#print(a)
#Mathematical operations can't be performed directly on lists

#d=np.array([1,2,3],"Bob")
#print(d)
#array only works with one type of data (homogeneous)

e=np.zeros(10)
print(e)
f=np.ones(10)
print(f)

g=np.array([1,2,3,4,5],dtype = "f")
print(g)

#Multidimensional Aray
h=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(h)

print("Array Dimension",h.ndim) #1D,2D,3D aray
print("Number of rows_col",h.shape) #number of rows and columns (3,3), (1,4)
print("Number of elements",h.size) #number of elements (9), (3)
print("Array size",h.nbytes,"bytes") #size in bytes 

i=np.arange(1,100) #Big arrays, starting and one after ending value
print(i)

j=np.arange(0,101,2) #last number is step size
print(j)

k=np.arange(1,100,2)
print(k)

#random
l=np.random.randint(1,10) #select any random value in given range
print(l)

m=np.random.permutation(np.arange(1,11)) #puts numbers in given range in random order
print(m)

n=np.random.rand(1,20) #prints 20 random float from 0 to 1. 1 is for the 1D array of 20 elements
print(n)
print()

o=np.random.rand(5,30)
print(o)
print()

p=np.arange(1,10).reshape(3,3) #reshape converts arrays into rows and columns
print(p)

q=np.arange(1,37).reshape(2,18)
print(q)
print()
r=np.arange(1,37).reshape(3,12)
print(r)
print()
s=np.arange(1,37).reshape(4,9)
print(s)
print()
t=np.arange(1,37).reshape(6,6)
print(t)
print()
u=np.arange(1,37).reshape(18,2)
print(u)
print()
v=np.arange(1,37).reshape(12,3)
print(v)
print()
w=np.arange(1,37).reshape(9,4)
print(w)
print() 
