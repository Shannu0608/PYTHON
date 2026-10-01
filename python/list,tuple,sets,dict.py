'''a = [ 3,4,5,6,7,8,8,9]
a.append(10)
print(a.pop())
print(a.remove(3))
print(len(a))
print(a)'''

'''#tuple
t = (10,20,30,40,40)
t2 = ('set','tuple')
t1 = tuple(sorted(t))
print(type(t))
print(t[1])#index
print(reversed(t))#reverse tuple
print(min(t))
print(max(t))
print(t.count(40))
print(t.index(30))
print(t1)
print(t[1:4])
print(t1+t2)'''

'''#sets
s = {2,4,5,8,3,6}
print(type(s))
print(s)
#it  does not support slicing'''

'''#dict
d1 = dict({100:'avinash',200:'srikhar',300:'kiran'})
print(d1)
d2 = dict([(333,'mohit'),(666,'sai charan'),(999,'abhi')])
print(d2)
d3 = dict((('l','siddu'),('r','karthik'),('s','sai')))
print(d3)'''
'''
#len
d1 = dict({100:'mohit',200:'sai charan',300:'abhi'})
print(len(d1))

#clear
print(d1.clear())'''

'''#get
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d[100])
#print(d[400])#keyerror
print(d.get(100))
#print(d.get(400))#none
print(d.get(100,'mohit'))
print(d.get(400,'mohit'))'''

'''#pop
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.popitem())
d = {}
print(d.popitem())#keyerror'''

'''#keys
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.keys())
for k in d.keys():
    print(k)
    #values
    d = {100:'mohit',200:'bunny',300:'abhi'}
    print(d.values())
    for k in d.values():
     print()
        
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.items())
for k,v in d.items():
    print(k,'--->',v)'''
    
    #copy
'''d ={100:'mohit',200:'bunny',300:'abhi'} 
d1 '''





#update
d = {100:'mohit',200:'bunny',300:'abhi'}
d1 = {'a','apple'}
d.update(d1)#value error
print(d)
d.update([(333,'A')])
print(d)

#set default
d = { 100:'mohit',200:'bunny',300:'abhi'}
print(d.setdefault(100,'mohit'))
print(d.setdefault(400,"vamsi"))