#programme of creating calculactor 🧮

m1 = int(input("give the value of a ")) 
                                                    #m1 stores the entered value
m2 = int(input("give the vlaue of b "))
                                                #m2 store the entered value
tool  = (input("what you need to calculate "))
                                               # tool 1  work what user want 
if tool == "+":    #it indicates addtion
    print(f"the addition of the  two numbers is:{m1 + m2}") 

elif tool== "-":  #it indicates subtraction
    print(f"the subtraction of the two numbers is :{m1 - m2}")

elif tool == "*": #it indicates multiplication
    print(f"the multiplication of the two numbers is:{m1 * m2}")

elif tool == "/": #it indicates divison 
    print(f"the division of the two numbers is:{m1/m2}")
    
else:
    print("they olny comands me  given to  calculations based on  +,-,*,/ only thankyou!")
    







