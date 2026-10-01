#xbreak,continue,pass are jump statements
'''s = range(10)
for i in s:
    if i == 3:
        break
        print(i)'''

'''
for i in s:
    if i == 3:
        continue
    print(i)'''
    
'''  #assignment
   #1.prime number greater than 100
n = int(input("enter a number:")) 
count = 0
i = 1
s = range(1,n+1)
for i in s:
    if i >100:
        if n%i == 0:
            count += 1
            if   count ==2:
                break
            print(i," is a prime  number greater than 100") 
            else:
            print("not a prime number")
     else:
     print("number is less than 100")'''
         
#2.sum of 100 numbers except 3 and 5 multiples
'''s = range(1,101)
sum = 0
for i in s:
    if i % 3==0 and i% 5 ==0:
        continue
    sum = sum+i
print("sum=",sum)'''
        
''' #3.password and username
user_name = input("enter a user name:") 
password = input("enter password:")
count = 0
for i in range(3):
    if password == "shannu":
        print("login successful")
        break
    else:
     password = input("try again:")
else:
    print("your 3 attempts are over")'''
    
''' #4.first 10 even numbers except 3 multiples
s = range(2,21,2)
count = 0
for i in s:
    if i%3==0:
     continue
    count = count +1
    print(i)        '''                                                                                                                                                                                                                                                                                                            
 
''' #5.print and count vowels
s = "shanmukha priya kuncha"
count = 0
for i in s:
    if i in "aeiouAEIOU":
     count = count+1
     print(i)
    else:
        continue

print ("count of vowels:",count)'''
'''
#6.prime numbers from 1 to 100
n = 2
while n <=100:
  count=0
  while i <=n:
    i =1
    if n%i==0:
      count = count+1
      i=i+1
      n=n+1
    if count==2:
        print(n)
    
    else:
      break'''