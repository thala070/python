#concatination,addition,string
#first_name="Bro"
#last_name="Code"
#full_name=first_name +" "+ last_name
#print("Hello "+full_name)
#print(type(first_name))
#integer
#age=21
#print(age)
#age += 1
#print(age)
#print(type(age))
#age=age+1
#print(age)
#print("your age is: " + str(age))
#float
#height=250.5
#print(height)
#print(type(height))
#print("your height is: "  +str(height)+"cm")
#print(type(height))
#boolean
#human=True
#print(human)
#print("are u human: " +str(human) +"thanku")
#print(type(human))
#multiple assignments
#name,age,height="ms",42,210
#print(name)
#print(age)
#print(height)
#ms=virat=rahul=30
#print(ms)
#print(virat)
#print(rahul)

#string methods
#name="dhoni"
#print(name.capitalize())
#print(len(name))
#print(name.upper())
#print(name.lower())
#print(name.isdigit()
#print(name.find("h"))
#print(name.isalpha())
#print(name.count("n"))
#print(name.replace("o","a"))
#print(name*3)

#typecasting=convert the datatype of value to another datatype
#x=1
#y=2.0
#z="3"
#x=float(x)
#y=int(y)
#print("x value is:" +str(x)) 
#print(y)
#print(float(z))

#user input
#name=input("what is your name?:")
#age= int(input("how old r u?:") )
#height=float(input("how tall are u?:"))
         
#age= age + 1
#print("hello"+ name)
#print( "you are"+str(age)+ "years old")
#print("you r" +str(height)+"cm tall")

# functions
##pi=3.14
#x=1
#a=2
#q=3.0
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,3))
#print(math.sqrt(4))
#print(max(x,a,q))
#print(min(x,a,q))

#slicing=create a substring by extracting elements from another string
#name= "ms dhoni"
#first_name=name[0:2]
#last_name=name[3:8]
#funky_name=name[::2]
#reverse_name=name[::-1]
#print(last_name)
#print(funky_name)
#print(reverse_name)

#slicing string
#name1="mahendrasinghdhoni"
#name2="venkatarrishiaju"
#slice = slice(7,-4)
#print(name1[slice])
#print(name2[slice])

#if statement a block of code that will excute if its condition is true
#age=int(input("how old r u?:"))
#if age<=18:
  #print("u r a major")
#elif age==100:
 # print("u r acenturian")
#else:
 # print("u r a major")
    
#logical operators(and,or,not)= used to check if two or more conditional statements(no)
#temp=int(input("what is the temperature outside"))
#if temp>=0 and temp<30:
#if not(temp>=0 and temp<=30):
 #   print("temperature is good today")
#elif temp<0 or temp>30:
 #   print("the temperature is bad todat")

 #while loop= a statement that will excute its block of code,as long as its condition remains same
#while 1==1:
#    print("hello! i am stuck in a loop!")
#name=""
#while len(name)==0:
 #     name=input("enter your name:")

  #    print("hello"+name)
      
#name= none
#while not name:
 #     name=input("enter your name:")

  #    print("hello"+name)
#for loop= a statement that will be excute its block of code a limited time
#whuile loop=unlimited
#for loop=limited times
#for i in range(10):
 #   print(i+1)
#for i in range(1,10,5):
 #   print(i)
#for i in "msdhoni":
#    print(i)
#import time
#for i in range(1,10,1):
 #   print(i)
  #  time.sleep(1)
#print("happy new year!")    

#nested loop=the inner loop will finish all iterations before finishing one iterations of the outer loop
#rows=int(input("enter no of rows"))
#columns=int(input("enter no of columns"))
#ymbol=(input("enter your symbol"))
#for i in range(rows):
 #   for j in range(columns):
  #      print(symbol,end="")
   # print()    

#loop control statements=change the loop excution from its normal sequence
#break=used to terminate loop permanently
#continue=skips to the next iteration of the loop
#pass=does nothing, acts as a placeholder
#while True:
 #   name=input("what is your name")
  #  if name !="_":
   #     break
#phone_number="123-456-789"
#for i in phone_number:
 #   if i=="-":
  #      continue
   # print(i,end="")
#for i in range (1,21):
 #   if i==12:
  #      pass
   # else:
     #    print(i)

#list=used to store multiple items in a single variable
#functions in list
#append=to add item
#remove=to remove item
#pop=to remove last item
#insert=to insert at certain index
#sort=gives u in ascending order
#clear=clear the item
#food=["pizza","biryani","burger","samosa"]
#print(food[0])
#food.append("idli")
#food.remove("biryani")
#food.pop()
#food.insert(0,"plate")
#food.sort()
#food.clear()
#for x in food:
 #   print(x)
#2d lists
#drinks = ["cola","cofee","tea"]
#rice = ["biryani","friedrice","curry"]
#desserts = ["icecream","sweet"]
#food = [drinks,rice,desserts]
#print(food[0][1])

#tuple=collection which is ordered and unchangeble used to group together related data
#methods of tuple=count,index 
#student=("bro",21,"male")
#print(student.count("bro"))
#print(student.index("male"))
#for x in student:
 #   print(x)
  #  if "bro" in student:
   #     print("bro is here!")

#set=collection which is unordered,unindexed,no duplicate values
#methods=add,remove,clear,update,union,difference,intersection=common
#utensils={"fork","spoon","knife"}
#dishes={"bowl","plate","cup","knife"}
#print(utensils)
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table=utensils.union(dishes)
#for i in dinner_table:
     #print(i)
#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))
        
 #dictionary=A changeble,unordeed collection of unique key:value pairs fast because they use hashing,allow us to access a value quickly
#capitals={"andhra":"visakapatnam","telangana":"hyderabad","tamilnadu":"chennai"}
#capitals.update({"kerala":"thiru"})
#capitals.update({"andhra":"am"})
#capitals.pop("telangana")
#capitals.clear
#print(capitals["andhra"])
#print(capitals.get("kerala"))
#print(capitals.keys())
#print(capitals.values())
#for key_values in capitals:
 #   print(key_values)
 
#index operator[]=gives access to a sequence's(str,list,tuples)
#name="bro code"
#if(name[0].islower()):
 #   name=name.capitalize()
#print(name)
#first_name=name[::2].upper()
#last_name=name[0:1].lower()
#print(first_name)
#print(last_name)

#function=  block of code which is executed only when it is called
#whenever function need to be defines we have to write def
#def hello(first_name,last_name,age):
   # print("hello "+first_name+" "+last_name)
  #  print("you are"+str(age)+"years old")
 #   print("have a nice day")

#hello("bro","code",21)

#return statement=functions send python values/objects back to the caller. these values/objects are known as the function return value
#def multiply(number1,number2):
#    result=number1*number2
 #   return number1*number2
#x=multiply(6,8)  
#print(x)

#keyword argument=arguments preceded by an identifier when we pass them to a function the order of the arguments doesnot matter,unlike positional and python knows the names of the arguments that our function
#def hello(first,middle,last):
 #   print("hello" +  first+" "+middle+" "+last)

#hello(last="code",middle="dude",first="bro")

#NESTED FUNCTIONS CALLS=FUNCTION CALLS INSIDE OTHER FUNCTION calls innermost function calls are resolved first returned value is used as argument for the next outer function
#num=input("enter a whole number:")
#num =float(num)
#num=abs(num)
#num=round(num)
#print(num)
#print(round(abs(float(input("enter a whole positive number")))))

#scope=the region that a variable is recognized
       #a variable is only available from inside the region it is created
#a global and locally scopped versions of a variable can be created
#name="bro" #global scope(available inside and outside function)

#def display_name():
 #   name="code" #local scope
  #  print(name)

#display_name()
#print(name)

#*args=parameter that will pack all arguments into a tuple
#      useful so that a function can accept a varying amount of arguments
#def add(*stuff):
 #   sum=0
  #  stuff=list(stuff) =tuple object is not supported by the item assignment
   # stuff[0]=0
    #for i in stuff:
     #   sum +=i
    #return  
#print(add(1,2,3,4,5,5,6)) 

#**kwargs= parameter that will pack all argument into a dictionary
#          usefl so that a function can accept a varying amount of keyword argument
 
#def hello(**kwargs):
#    print("hello"+ kwargs['first']+" "+ kwargs['last'])
     #print("hello",end="")
     #for key,value in kwargs.items():
      #    print(value,end=" ")
#hello(first="bro",middle="dude",last="code")


#str.format()=optional method that gives users more control when displaying output

animal="cow"
item="moon"
#print("the "+animal+" jumped over the moon")
#print("the {} jumped over {}".format(animal,item))
#print("the {1} jumped over the {1}".format(animal,item))

#text="the {} jumped over the {}"
#print(text.format(animal,item))






