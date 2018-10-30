# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:44:20 2018

@author: Akhil
"""
import re
'''
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search("My number is 415-555-4242")
print(mo.group())
'''

#================================================


'''
pr2=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2=pr2.search("My number is 412-453-4567")
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(0))
areaCode,mainNumber=mo2.groups()
print("Area Code: ",areaCode)
print("Main Number: ",mainNumber)
'''


#================================================


'''
phoneNumRegex=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search("My phone number is (415) 555-4242")
print(mo.group(1))
print(mo.group(2))
'''

#================================================


'''
batRegex = re.compile(r'(Bat|bat)(man|mobile|copter|bat)')
mo=batRegex.search("batmobile lost a wheel")
print(mo.group())
'''


#================================================


'''
batRegex = re.compile(r'Bat(wo)?man')
mo=batRegex.search("adventures of Batman and Batwoman")
print(mo.group())
'''


#================================================

# * is used for zero or many repitions. if u want
#one or more use +
'''
batRegex=re.compile(r'Bat(wo)*man')
mo=batRegex.search("Batwowoman is here")
print(mo.group())
'''


#=================================================


'''
haRegex=re.compile(r'(Ha|ha){3}')
mo=haRegex.search("HaHaha")
print(mo.group())
'''



#=================================================


'''
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
l=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(l)
'''


#==================================================

# \d=======(0--9)
# \D=======(characters except 0 to 9)
# \W=======(letter ,numeric digit or underscore)
# \s=======(space, tab or newline character)
# \S=======(any character that is not space,tab or underscore)

#Make own character class:
'''
vowelRegex=re.compile(r'[aeiouAEIOU]')
l=vowelRegex.findall('Robocop eats baby food.')
print(l)
'''
# character class also given as
#[a-zA-Z0-9]
# if u give ^ symbol at start inside square bracket
#creates negative character class that gives everything 
#other than that mentioned



#=================================================


'''
beginsWithHello=re.compile(r'^hello')
#^ sign checks whether it starts with hello
mo=beginsWithHello.search("hello world")#returns Boolean
print(mo==False)

#Similarly dollar sign at end checks whether it ends with
#word or not
'''


#==================================================




#WILDCARD CHARACTER '.' dot is any character except newline
'''
atRegex=re.compile(r'.at')
mo=atRegex.findall("the cat and the bat sat on the mat")
print(mo)
'''



#==================================================


#Match Anything using (.*) except newline
'''
nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
mo=nameRegex.search("First Name: Akhil Last Name: Eppa")
print(mo.group())
'''



#=================================================


#Match newline with  dot star using DOTALL
'''
newLineRegex=re.compile(r'.*',re.DOTALL)
mo=newLineRegex.search("Serve the public trust.\nProtect the innocent.")

print(mo.group())
'''


#================================================


#Match Regex ignoring uppercase or lowercase with 
#re.I or re.IGNORECASE
'''
robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())
'''


#================================================




#substitute strings with sub method
'''
namesRegex=re.compile(r'(A|a)gent \w+')
x="Agent Alice gave secret documents to agent Bob"
print(namesRegex.sub("Censored",x))
'''
'''
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent\
\Eve knew Agent Bob was a double agent.'))
'''


#=================================================



#When making complicated regex we can use re.verbose 
#to ignore spaces and comments in regex expression only

#phoneRegex = re.compile(r'''(
#    (\d{3}|\(\d{3}\))?                # area code
#    (\s|-|\.)?                        # separator
#    (\d{3})                           # first 3 digits
#    (\s|-|\.)                         # separator
#    (\d{4})                           # last 4 digits
#    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
#    )''', re.VERBOSE)



#Using pyperclip module to build project
