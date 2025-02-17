for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        #where % is a modulus operator (gives the remainder numbers are divided)
        print("FizzBuzz")
    else:
        if i % 3 == 0:
            print("Fizz")
        else:
            if i % 5 == 0:
                print("Buzz")
            else:
                print(i)