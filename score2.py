import random

x=random.randint(1,6)
y=random.randint(1,6)
z=random.randint(1,6)
o=random.randint(1,6)
p=random.randint(1,6)

k=[x,y,z,o,p]

print k


sum=0
val=0
sal=0

if k.count(1)==5:
  sum+=1200
if k.count(1)==4:
  sum=1100
if k.count(1)==3:
  sum=1000
if k.count(1)==2:
  sum=200
if k.count(1)==1:
  sum=100
  

if k.count(2)==3:
  val=200
if k.count(2)==4:
  val=0
if k.count(2)==5:
  val=0  
if k.count(3)==3:
  val=300
if k.count(3)==4:
  val=0
if k.count(3)==5:
  val=0
if k.count(4)==3:
  val=400
if k.count(4)==4:
  val=0
if k.count(4)==5:
  val=0
if k.count(6)==3:
  val=600
if k.count(6)==4:
  val=0
if k.count(6)==5:
  val=0    

if k.count(5)==1:
  sal=50
if k.count(5)==2:
  sal=100
if k.count(5)==3:
  sal=500
if k.count(5)==4:
  sal=550
if k.count(5)==5:
  sal=600
  
  




print sum + val + sal
