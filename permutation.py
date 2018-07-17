# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:56:07 2018

f(n) = n * f(n-1)

and if a is a string variable
a = "hello"
b = a
b = b+" world"
print(b): hello world
print(a): hello
so "=" equal "copy"
and creat a new date

@author: lele
"""

a = "1234"
#def permutation(a,size,n):
#    if n == 1:
#        print(new_array)
#        return
#    for i in range(size):
#        pass
#        
#def main(a):
#    a = input("please input a string of integer:")
#    permutation(a,sizeof(a)/sizeof(int),n)


print("size:",size)


ls = range(1,size+1)
minimum = 0
for figure in ls:
    minimum += figure * (10 ** (size-1-ls.index(figure)))
maximum = list(str(minimum))
maximum.reverse()
maximum = "".join(maximum)


def swap(temp,a,b):
    temp = list(temp)
    
    temp[a],temp[b] = temp[b],temp[a]
    return temp
    
#temp_ls = list(str(minimum))
temp_ls = list("123")
size = len(temp_ls)

print("a:",a)
print("original temp_ls:",temp_ls)
count = 0
while(1):
    if("".join(temp_ls) == maximum):
        break
    for i in range(size):
        if(temp_ls[size-i-1]>temp_ls[size-i-2]):
            roi = temp_ls[size-i-2:]
            a = size-i-2
            
            a_value = temp_ls[a]
            second = []
            for j in roi:
                if(j>a_value):
                    second.append(j)
            print("second",second)
        
            b_value = min(second)
            b = temp_ls.index(b_value)
            print("a",a)
            print("b",b)            
            temp_ls = swap(temp_ls,a,b)
            print("swap:",temp_ls)
            rest = temp_ls[size-i-1:]
            print("rest",rest)            

            rest.reverse()
            
            temp_ls[size-i-1:] = rest
            print("finally temp_ls",temp_ls)
            count += 1
            print("count:",count)
            print("--------------")

            break    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    