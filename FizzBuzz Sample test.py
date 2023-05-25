def fizzBuzz(n):
    for i in range(1,n+1,1):
        if(i%3 == 0 and i%5 == 0):
            print("FizzBuzz")
        elif(i%3 == 0 and not i%5 == 0):
            print("Fizz")
        elif(not i%3 == 0 and i%5 == 0):
            print("Buzz")
        else:
            print(i)
        
