'''
#1. Write a python function to check if any given number is a prime number and odd number?

n = int(input("Enter a number:\n"))

if(n%2 !=0):
    for i in range(2,int(n*0.5)+1):
        if (n%i==0):
            print("It is not a prime NUmber and it is a Odd Number")
            break
    else:
        print("It is a Prime Number and Odd number")
else:
    print('It is a even number')
    


# 2.Master Yoda speaks a sentence in a different order. Let's say you want to convert a sentence to Yoda’s speech.  Write a function named master_yoda which will take a string as input and return the output after reversing the words of the sentence.

y_w =  input("Enter a sentence that yoda speaks :\n").split(' ')

def master_yodha(st,stack=[]):
    for word in st:
        stack.append(word)
    print("After reversing the words of the sentence")
    for i in range(len(stack)):
        print(stack.pop())
master_yodha(y_w)

#3. 

    '''
'''
Write a function pay_bill which will take a list of expenses, percent commission, and a special offer amount

If you don’t pass percent_comission it should be always 9.8%

The Last argument special_offer_amount is not a required argument, you don’t need to pass it. Make it an optional parameter.

If you want to give a special offer to the user, then you have to pass the third argument special_offer_amount. If the user makes the purchase greater than special_offer_amount, then give him an extra commission of 1.2%.

Calculate the final payable price of the bill and return it from the function.
 '''
 

def pay_bill(expenses, comm_per=9.8, **spe_off_am):
   
    if(spe_off_am["offer"] and sum(expenses) >= spe_off_am["offer"]):
        return sum(expenses) * ((comm_per + 1.2) // 100)
    else:
        return sum(expenses) * (comm_per // 100)

expenses = [1000,200,3003, 400,10000]
print(pay_bill(expenses, offer=1000))

    





