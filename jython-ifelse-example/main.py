def calculation(amount):
    result ='';
    if amount > 0 and amount < 100:
        result ="amount is in between 0 to 100 "
    elif  amount > 100 and amount < 200:
        result ="amount is in between 100 to 200 "
    else:
        result ="amount is in greater then 200 "
    return result

def main_function_executor():
    amount = input("enter Amount")
    result = calculation(amount)
    print(result)

if __name__ == '__main__':
    main_function_executor()