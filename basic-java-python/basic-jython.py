#  java -jar jython-standalone-2.7.2.jar basic-jython.py
# "java -jar ../jython-standalone-2.7.2.jar basic-jython.py"

from java.lang import System # Java import

print('Running on Java version: ' + System.getProperty('java.version'))
print('Unix time from Java: ' + str(System.currentTimeMillis()))