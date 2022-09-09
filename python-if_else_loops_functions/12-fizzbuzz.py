#!/usr/bin/python3
for fizzbuzz in range(1,101):
    if fizzbuzz % 15 == 0:
        print("FizzBuzz ", end="")                                        
    elif fizzbuzz % 3 == 0:    
        print("Fizz ", end="")                                        
    elif fizzbuzz % 5 == 0:        
        print("Buzz ",  end="")                                    
    else:
        print(f"{fizzbuzz} ", end="")
