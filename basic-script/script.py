"https://www.jython.org/index"
"$ java -jar jython-standalone-2.7.2.jar"
"java -jar jython-standalone-2.7.2.jar script.py"
"java -jar ../jython-standalone-2.7.2.jar script.py"
counter=0

while counter < 3:
	print('inside loop')
	counter = counter+1

else:
	print('inside else')