#get()
#it return a value of specified key
d={'a':101,'b':102,'c':103,'d':104}
print(d.get('a'))
print(d.get('e')) #None

#update()
#it is use to add multiple element to thr list
d={'a':101,'b':102,'c':103,'d':104}
d.update({'e':105,'f':106})
print(d)

#pop()
#it is used to use remove specified keys
d={'a':101,'b':102,'c':103,'d':104}
d.pop('b')
print(d)

#popitem()
#it is used to remove last inserted keys
d={'a':101,'b':102,'c':103,'d':104}
d.popitem()
print(d)

#values()
#it is return the list of values in form of list
d={'a':101,'b':102,'c':103,'d':104}
print(d.values())

#keys()
#itb returns the keys form a dictionary in a list
d={'a':101,'b':102,'c':103,'d':104}
print(d.keys())

#items()
#it return the list of all the pairs from the list
d={'a':101,'b':102,'c':103,'d':104}
print(d.items())

#setdefault()
#it used to add pair at the end of thr list
d={'a':101,'b':102,'c':103,'d':104}
print(d.setdefault('e',105))
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)


#clear()
#it return the empty dictionary by removing all the items
d={'a':101,'b':102,'c':103,'d':104}
print(d.clear())

#copy()
#it create he copy of the existing dictiinary
d={'a':101,'b':102,'c':103,'d':104}
d1=d.copy()
print(d1)

#iterating dictionary
d={'a':101,'b':102,'c':103,'d':104}
for i in d:
    print(i) #accses keys()
    
for i in d.keys():
    print(i)    #get keys
    
for i in d.values():
    print(i)    #access values
    
for k,v in d.items():
    print(k,v) #to access both keys and values
    
    
d={'a':101,'b':{'b1':155,'b12':109},'c':103,'d':104}
print(d['a'])    
print(d['b']['b12']) #to access value of b12


#fromkeys()
x=('key1','key2','key3')
y=[11,22,33]
newdict=dict.fromkeys(x,y)
print(newdict)