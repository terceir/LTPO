# data type practice
# String
firstname = "LTPO"
lastname = "LTPO"
type(fristname)
print(fristname  +" "+ lastname)
# integer
num = 2
# float = 6.9
 num2 = 6.9
type(num2)
calculate = num + num2
type(calculate)
calculate = int(calculate)
type(calculate)
#boolean
check = False
print (check)
type(check)
# addition and substraction
deposit = 1000 # I deposit $1000
withdraw = 200 # I withdraw $200
seconddeposit = 5000 # this is my second deposit
cb = deposit - withdraw + seconddeposit
print(cb)
(12) # multiplication division
# 25% discount
discount = 25/100
print(discount)
price = 560
newprice = price - (price + discount)
print(newprice)
import math
a = 8
power = 5
answer = a**power
print(answer)
import math
power = 6
answer = math.exp(power)
print(answer)
import math
number = 676
answer = math.sqrt(number)
print(answer)
# conditional statement (if/else)
username = "LTPO"
password = "LTPO567"
type(password)
if username == "LTPO"  and  password == "LTPO567":
print("welcome to the app!")
else:
print("wrong username or wrong password")
cb = 600 
withdraw = 700
check = cb - withdraw 
print(check)
if check >= 0:
 print("withdraw succesful")
       else:
       print('balance is not sufficient')
       n = 90
       if n % 2 == 0:
       print("even")
       else:
       print("odd")
       # for loop
       lista =("LTPO", "LUIS", "DUDA","MARCELL","BOB","donald")
       for x in lista:                                              
           print(x)
          # for loop
           listl = list()
           for i in range(0,7):
              listl.append(i)
              print(listl)
              b = 9
              while b < 11:
                 b = b + 1
                 print("apple")
                 # Getting input/data from users
                 password = str(input("Enter your password here"))
                 Enter your password here "LTPO"
                 # database
                 password = "abcdefg"
                 userpassword = str(input{"Enter your password here"})
                 if  userpassword  == password:
                    print("welcome to the app")
                 else:
                    print("password is incorrect, please, reenter your password ")
                    Enter your password "hereabcdefg"
                    welcome to the app
                    # Functions in Python
                    def passwordlength(password):
                        password = str(password) 
                        length = len(password)                                    
                         return length  

                          password = "abcfgk"
                           print(passwordlength(password))
                           # Another example
                           def passwordcheck(password):
                             if len(password) < 7:
                                print("The password has to be consisted with more than or equal 7 digits")
                             else:
                                print("The account has been created")

                                password = "r"
                                print(passwordcheck(password))
                                 import math                                 
                                 print("welcome to the online banking application")
                                def signin():
                                     global name # username
                                     global pin  # password
                                     global cb   # current balance
                                     name = str(input("Please create your username"))
                                      pin = str(input("Please create your 6 digitas pin"))
                                     if len(pin) == 6:
                                        pin = pin
                                     else:
                                        print("The pin has to be in 6 digits")
                                        newpin = str(input("Please create your 6 digitas pin"))
                                        if len(newpin) != 6:
                                           print("The pin has to be in 6 digits")
                                           sign()
                                        else:
                                           pin = newpin
                                           print("Thanks for creating your bank account")
                                           
                                           signin()                             
                                           