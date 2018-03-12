 # -*- coding: utf-8 -*-

this_year=2017
user="jack"

counter=0
while True:
	counter=counter+1
	if counter>3:
		print "诚心的，是不？"
		quit();
	name = raw_input("Please input your name:").strip()
	if len(name)==0:
		print "empty value,write again"
		continue
	elif user != name:		
		print "u r not the right user,go out"
		continue
	else:
		break

age = int(raw_input("how old are you?"))
sex=raw_input("please input your sex:")
dep=raw_input("which deportment:")

message='''this is our compony staff info
	name: %s
	age : %d
	sex : %s
	dep : %s
	'''%(name,age,sex,dep)

print '\n',message
if age<=28:
	print "Congratulations!You have half days public holiday!"
else:
	print "BAD!You have not half days holiday."

print "----------------------"
if user==name:
	print "welcome ,%s"%(name),". Let's go!"
else:
	print "u r not the right user,go out"
