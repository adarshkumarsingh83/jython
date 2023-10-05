
def welcomeFromFunction(name):
    print "Hello "+name
    return "welcome from espark "+name;

def main_function_executor():
    result = welcomeFromFunction("adarsh kumar")
    print(result)

if __name__ == '__main__':
    main_function_executor()