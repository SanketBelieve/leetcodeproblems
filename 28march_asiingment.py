class A:
    def day(self):
        print("have a good day")

obj=A()
obj.day() 
obj.day= 'monday'  #this how we define state of a object
#behaviour is a method defined in class      
#how we call the method --> object_name,method_name()
#how python internally call the class--> class_name.method_name.(object) 
#state is a unique property of a object
#behaviour is a common property for all the object that structured in a class
#class is a template or blueprint of a object
#object is areal entity, object is a instance of a class
#object can be anything
class car:
    def brake(self):
        print("air brake")
    def transmission(self):
        print('automatic')   

skoda=car()
skoda.color='blue'
skoda.brake()
skoda.transmission()
print(skoda.color)
       
class c:
    def add(self,a,b):
        res=a+b 
        print(res) 
         
a1=c()
a1.add(10,20)


#perform all the arithmetic operations in a class
class operations:
    def add(self,a,b):
        print(a+b) 
    def multi(self,a,b):
        print(a*b)
    def sub(self,a,b):
        print(a-b)
    def div(self,a,b):
        print(a/b)
    def mod(self,a,b):
        print(a%b)
    def floor(self,a,b):
        print(a//b)
    def expo(self,a,b):
        print(a**b)

a1=operations()
a1.add(10,20) 
a1.multi(10,4)
a1.sub(40,90)
a1.div(10,88)
a1.mod(10,50)
a1.expo(2,8)
a1.floor(100,887)                               


class loksabha:
    
    def elected(self):
        print("elected by the people")
    def house(self):
        print("lower house")

modi=loksabha()
modi.constituency='varanasi'
modi.party='bjp'

modi.elected()
modi.house()
print(modi.constituency)
print(modi.party)
print("****************")
sule=loksabha()
sule.constituency='baramati'
sule.party='ncp_sp'
sule.elected()
sule.house()
print(sule.constituency)
print(sule.party)
print("****************")

class State:
    def country(self):
        print("India")
    def prime_minister(self):
        print("Modi")
MH=State()
MH.capital="Mumbai"
MH.language="Marathi"
MH.area="350000sqkm"

KR=State()
KR.capital="banglore"
KR.language="kannada"
KR.area='250000sqkm'

TN=State()
TN.capital="chennai"
TN.area="200000sqkm"
TN.language="tamil"
MH.country()
MH.prime_minister()
print(MH.capital)
print(MH.language)
print(MH.area)
print("******")
KR.country()
KR.prime_minister()
print(KR.capital)
print(KR.language)
print(KR.area)
print("******")
TN.country()
TN.prime_minister()
print(TN.capital)
print(TN.language)
print(TN.area)
print("**************")
class Laptop:
    def screen(self):
        print("all laptop have screen")
    def ram(self):
        print("all laptop have ram") 
        
lenovo=Laptop()
lenovo.color='black'
lenovo.model='aspire'
lenovo.price=50000
dell=Laptop()
dell.color="blue"
dell.model="inspiration"       
dell.price=60000
lenovo.screen()
lenovo.ram()
print(lenovo.color)
print(lenovo.model)
print(lenovo.price)
print("*******")
dell.screen()
dell.ram()
print(dell.color)
print(dell.model)
print(dell.price)
print("**************")
class Bottle:
    def storage(self):
        print('all bottle have storage')
    def storage_type(self):
        print("all bottles are used to store liquid")  
        
orange=Bottle()
orange.material='metal'
orange.color='white'
orange.capasity='500ml'    

yellow=Bottle()
yellow.material='plastic'
yellow.color='yellow'
yellow.capasity='750ml'   

ruby=Bottle()
ruby.material='fibre'
ruby.color='black'
ruby.capasity='1000ml'
orange.storage()
orange.storage_type()
print(orange.material)
print(orange.color)
print(orange.capasity)
print("*****")
yellow.storage()
yellow.storage_type()
print(yellow.material)
print(yellow.color)
print(yellow.capasity)
print("*****")
ruby.storage()
ruby.storage_type()
print(ruby.material)
print(ruby.color)
print(ruby.capasity)
print("*****************")

class Router:
    def use(self):
        print("distribute the network")
    def lancable(self):
        print("all routers has lan cable port")    

tplink=Router()
tplink.bandwidth='1000mbps'
tplink.color='white'
tplink.shape='circle'

marcus=Router()
marcus.bandwidth='500mbps'
marcus.color='green'
marcus.shape='square'

jio=Router()
jio.bandwidth='200mbps'
jio.color='black'
jio.shape='hexa'

tplink.lancable()
tplink.use()
print(tplink.bandwidth)
print(tplink.color)
print(tplink.shape)
print("******")
marcus.lancable()
marcus.use()
print(marcus.bandwidth)
print(marcus.color)
print(marcus.shape)
print("*******")
jio.lancable()
jio.use()
print(jio.bandwidth)
print(jio.color)
print(jio.shape)
print("***************")

class Socialmedia:
    def fact(self):
        print("all are social networking site")
    def dependancy(self):
        print("all need internet for running")

insta=Socialmedia()
insta.feature='sharing photos'
insta.headquater='sanfransico'
insta.ceo='zukerberg'

twiter=Socialmedia()
twiter.feature='expressing thought'
twiter.headquater='seatle'
twiter.ceo='elon musk'

snap=Socialmedia()
snap.feature='sending updates'
snap.headquater='LA'
snap.ceo='arnold'
insta.fact()
insta.dependancy()
print(insta.feature)
print(insta.headquater)
print(insta.ceo)
print("******")
twiter.fact()
twiter.dependancy()
print(twiter.feature)
print(twiter.headquater)
print(twiter.ceo)
print("******")
snap.fact()
snap.dependancy()
print(snap.feature)
print(snap.headquater)
print(snap.ceo)
print("******************")


class Footballclub:
    def rules(self):
        print("rules for all teams are same")
    def region(self):
        print("all team playes in europe")    
madrid=Footballclub()
madrid.jercycolor='white'
madrid.homeground='bernebue'
madrid.worldrank=1

barca=Footballclub()
barca.jercycolor='red blue'
barca.homeground='camp neo'
barca.worldrank=20

m_united=Footballclub()
m_united.jercycolor='Red'
m_united.homeground='old trafford'
m_united.worldrank=6

madrid.region()
madrid.rules()
print(madrid.jercycolor)
print(madrid.homeground)
print(madrid.worldrank)
print("*****")
barca.region()
barca.rules()
print(barca.jercycolor)
print(barca.homeground)
print(barca.worldrank)
print("******")
m_united.region()
m_united.rules()
print(m_united.jercycolor)
print(m_united.homeground)
print(m_united.worldrank)
print("*******************")

class Datascience:
    def domain(self):
        print("all works with data")
    def aim(self):
        print("used to make desicion")
data_scientist=Datascience()
data_scientist.salary=1000000
data_scientist.tool='jupyter'
data_scientist.operation='develop solution'

data_engineer=Datascience()
data_engineer.salary=2000000
data_engineer.tool='airflow'
data_engineer.operation='manage data'

data_analyst=Datascience()
data_analyst.salary=1500000
data_analyst.tool='powerbi'
data_analyst.operation='find insight'
print("****data_scientist INFO****")
data_scientist.aim()
data_scientist.domain()
print(data_scientist.operation)
print(data_scientist.tool)
print(data_scientist.salary)

print("****Data_Engineer INFO****")
data_engineer.aim()
data_engineer.domain()
print(data_engineer.operation)
print(data_engineer.tool)
print(data_engineer.salary)

print("****Data analyst INFO****")
data_analyst.aim()
data_analyst.domain()
print(data_analyst.operation)
print(data_analyst.tool)
print(data_analyst.salary)

class Logistic:
    def work(self):
        print("Transportation of goods")
    def availability(self):
        print("Available all over the world")
planes=Logistic()
planes.mode='Air'
planes.cost='High'
planes.capasity='Low' 

ship=Logistic()
ship.mode='Waterways'
ship.cost="Low"
ship.capasity='High'  

truck=Logistic()
truck.mode='Roads'
truck.cost='High'
truck.capasity='High'
print("***Planes INFO***")
planes.availability()
planes.work()
print(planes.mode)  
print(planes.cost)
print(planes.capasity)  

print("***Ship INFO***")
ship.availability()
ship.work()
print(ship.mode)  
print(ship.cost)
print(ship.capasity)   

print("***Truck INFO***")
truck.availability()
truck.work()
print(truck.mode)  
print(truck.cost)
print(truck.capasity)      


class Irigation:
    def property(self):
        print('water supply systemt to the plant')
    def oparate(self):
        print("mainly in agriculture")
        
drip=Irigation()
drip.cost='High'
drip.area='small'
drip.impact='High'
                 
sprinkle=Irigation()
sprinkle.cost='Medium'
sprinkle.area='Large'
sprinkle.impact='Low'                 

surface=Irigation()
surface.cost='Low'
surface.area='Large'
surface.impact='High'

print("****Drip Info****")
drip.oparate()
drip.property()
print(drip.cost)
print(drip.area)
print(drip.impact)

print("****sprinkle Info****")
sprinkle.oparate()
sprinkle.property()
print(sprinkle.cost)
print(sprinkle.area)
print(sprinkle.impact)
