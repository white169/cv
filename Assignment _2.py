#!/usr/bin/env python
# coding: utf-8

# In[3]:


stri1 = "this is string example.....wow!!!"
print (stri1.capitalize())


# In[4]:


stri1 = "this is string example.....wow!!!"
print (stri1.center(40,'a'))


# In[14]:


stri1 = "this is string example.....wow!!!"
sub = "i"
print("stri1.count(sub,4,40) : ",
stri1.count(sub))
sub = "wow"
print("stri1.count(sub,4,40) : ",
stri1.count(sub))


# In[21]:


city = "Dusseldorf"
utf8_encoded = city.encode('utf-8')
print(type(utf8_encoded))
print(utf8_encoded)

decoded_city = utf8_encoded.decode('utf8')
print(type(decoded_city))
print(decoded_city)


# In[23]:


str1 = "this is string.....wow!!!"
suffix ="wow!!!"
print (str1.endswith(suffix))
print(str1.endswith(suffix,20))
suffix = "is"
print(str1.endswith(suffix,2,4))
print(str1.endswith(suffix,2,6))


# In[24]:


str1 = "this is\tstring example...wow!!!"
print("original string: " + str1)
print("Default expanded tab: " + str1.expandtabs())
print("Default expanded tab: " + str1.expandtabs(16))


# In[25]:


str1 = "this is\tstring example...wow!!!"
str2 = "exam"
print(str1.index(str2))
print(str1.index(str2,10))
print(str1.index(str2,40))


# In[26]:


str1 = "this2009";
print (str1.isalnum())

str1 = "this is string example...wow!!!"
print(str1.isalnum())


# In[27]:


str1 = "123456"
print (str1.isdigit())
str2 = "this is string example...wow!!!"

print(str2.isdigit())


# In[28]:


str1 = "THIS IS string example...wow!!!"
print(str1.islower())
str2 = "this is string example...wow!!!"
print(str2.islower())


# In[29]:


str1 = u"this2009"
print (str1.isnumeric())
str2 = u"233232322"
print(str2.isnumeric())


# In[33]:


str1 = "          "
print(str1.isspace())
str2 = "this is string example...wow!!!"


# In[34]:


str1 = "This Is String Example...Wow!!!"
print(str1.istitle())
str2 = "This is string example...wow!!!"
print(str2.istitle())


# In[38]:


str1 = "THIS IS STRING EXAMPLE...WOW!!!"
print (str1.isupper())
str2 = "THIS is string example...wow!!!"
print(str2.isupper())


# In[39]:


s ="_"
seq = ("a","b","c");
print(s.join(seq))


# In[40]:


str1 = "this is string example...wow!!!"
print("length ofthe string: ",len(str1))


# In[42]:


str1 = "this is string example...wow!!!"
print(str1.ljust(50, '0'))


# In[43]:


str1 = "THIS IS STRING EXAMPLE...WOW!!!"
print (str1.lower())


# In[44]:


str1 = "this is string example...wow!!!"
print (str1.lstrip())
str2 = "88888888this is string example.....wow!!!888888888"
print (str2.lstrip('8'))


# In[46]:


intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab,outtab)
str1 = "this is string example....wow!!!"
print(str1.translate(trantab))


# In[47]:


str1 = "this is really string example...wow!!!"
print ("Max character: " + max(str1))

str2 = "this is a string example...wow!!"
print ("max character: " + max(str2))


# In[48]:


str1 = "this-is-real-string-example....wow!!!"
print("min character: "+ min(str1))

str2 = "this-is-a-string-example...wow!!!"
print("min character: " +min(str2))


# In[49]:


str1 = "this is really string example...wow!!!"
print (str1.replace("is","was"))
print (str1.replace("is","was",3))


# In[53]:


str1 = "this-is-real-string-example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2,10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))


# In[54]:


str1 = "this is string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))
print (str1.index(str2))


# In[55]:


str1 = "this is string example....wow!!!"
print (str1.rjust(50, '0'))


# In[56]:


str1 = "       this is string example....wow!!!"
print (str1.rstrip())
str2 = "88888888this is string example.....wow!!!888888888"
print(str2.rstrip('8'))


# In[59]:


str1 = "Line1-abcdef \nLine2-abc\nLine4-abcd"
print (str1.split())
print (str1.split(' ', 1))


# In[60]:


str1 = "Line1-a b c d e f\nLine2- a b  c d"

print (str1.splitlines())
print (str1.splitlines(0))
print (str1.splitlines(3))
print (str1.splitlines(4))
print (str1.splitlines(5))


# In[61]:


str1 = "00000000this is string example....wow!!!00000000"
print (str1.strip('0'))


# In[62]:


str1 = "this is string example....wow!!!"
print (str1.swapcase())
str1 = "THIS IS STRING EXAMPLE...WOW!!!"
print (str1.swapcase())


# In[63]:


str1 = "this is string example....wow!!!"
print (str1.title())


# In[65]:


intab = "aieou"
outtab = "12345"
str1 = "this is string example....wow!!!"

trantab = str.maketrans(intab,outtab)

print(str1.translate(trantab))

trantab = str.maketrans(intab,outtab,'xm')


# In[67]:


str1 = "this is string example....wow!!!"
print("str1.capitalize(): ",str1.upper())


# In[69]:


str1 = "this is string example....wow!!!"
print(str1.zfill(40))
print(str1.zfill(50))     


# In[70]:


str1 = u"this2009"
print (str1.isdecimal())
str2 = u"2343434"
print (str2.isdecimal())


# In[72]:


#Question 2


# In[74]:


name = str(input("please enter your name"))
yob = int(input("please enter your year of your birth"))
salary = float(input("please enter your salary"))

age = (2021 - yob) + (2030-2021)
tax = (12.3/100)*salary

print("goodday {0}!!, your year of birth is {1} and your age is {2}".format(name,yob,salary))
print(" from your salary of {0} the computed tax of 12.3% is {1:.1f}".format(salary,tax))


# In[90]:


people = int(input("total people"))
name_ = []
score_ = []
num = 0

for i in range(people):
             name =input("enter name: ")
             score = int(input("enter score"))
             num+1
             
             name_.append(name)
             score_.append(score)
             num+1
             
avge = sum(score_)/people
all_ = [name_,score_]
             
print ("name and score is ",all_)
print( "average score is: ",avge)
             
             


# In[80]:


import textwrap

svname = input("enter employee name")
name = input("enter applicant name")
contact =input("enter apllicant contact number")


print("APPLICATION FOR TRAINEE POSITION\n\nDear",svname,",")
print(textwrap.fill("\n\n I am writing to you to apply for the trainee position for Perantis Iskandar Programme. I come across the advertisement on\nthe Internet and am very excited to learn more about the program. \n\n "))
print(textwrap.fill("\n\n2. I am a bachelor graduate from UTM in Degree of Electrical-Electronic. Artificial Inteligence program has caught my eyes as it has been my genuine passion and it has been my longest dream to become a software programmer. I am an eager and responsible person that will make sure I have the credibility to strive my dream. \n\n"))
print(textwrap.fill("\n\n3. I hope you will contact me at your earliest convenience to discuss the program and arrange an interview. Thank you for \nyour time and consideration."))
print(" \n\n\n Sincerely,\n", name,"\n",contact)

