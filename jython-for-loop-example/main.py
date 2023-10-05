def element_in_tuple_printing_func():
    print "Execution Start"
    names = ('adarsh', 'radha',  'shakti')
    for name in names:
        print 'Current library :', name
    print "Execution End"

def element_in_list_printing_func():
    print "Execution Start"
    names = ['adarsh', 'radha',  'shakti']
    for name in names:
        print 'Current library :', name
    print "Execution End"

def letter_printing_func():
    print "Execution Start"
    for letter in 'adarsh kumar singh':
        print 'Current Letter :', letter
    print "Execution End"

def number_printing_func():
    print "Execution Start"
    for num in range(5):
        print num
    print "Execution End"

def main_function_executor():
    number_printing_func();
    letter_printing_func();
    element_in_list_printing_func()
    element_in_tuple_printing_func()

if __name__ == '__main__':
    main_function_executor()