''' 1. Create a list of your friends' names and now create a list of tuples. 
The tuple should contain the friend’s name and the length of the name. 
For Example: if someone’s name is Aditya, the tuple would be: (‘Aditya’, 6)
'''
f_n = ['eve','perry','smriti','kerr']
for i in f_n:
    print((i,len(i)))
    
'''
2.You and your wife argued about expenses last night. You both want to know who is spending more in a month. 
Now you both go to the Little Yoda he is a good python programmer.
He suggested that both of you add an entry in a dictionary next time you spend money. 
So that you can have a clear picture of your expenses and plan to reduce them. Both dictionaries are as below-

Your expenses -

Clothes - 1100
Shoes - 1000
Watch - 900
Mobile Recharge - 699
Petrol - 1980

Your Wife’s expenses -

Mobile Recharge - 799
DTH recharge - 999
Clothes - 2310
Makeup - 3670
Shoes - 999
Find out the total expenses for each of you.
Find out who spending more
Find out which thing you and your wife spending more
'''

me = {'Clothes': 1100,
'Shoes': 1000,
'Watch': 900,
'Mobile_Recharge': 699,
'Petrol': 1980}

wife = {'Mobile_Recharge': 799,
'DTH_recharge' : 999,
'Clothes' : 2310, 
'Makeup':3670,
'Shoes':999}

a = list(me.values())

def total_expenses(per):
    return sum(list(per.values()))

def max_expenses(pe):
    return max(list(pe.values()))

def max_thing(pe):
    val = max_expenses(pe)
    for i,j in pe.items():
        if j == val:
            return i
print(f'The total expenses of husband {total_expenses(me)} and wife {total_expenses(wife)}')

if(max_expenses(me) > max_expenses(wife)):
    print("The max expenses of husbandd are more")
else:
    print("The max expenses of wife are more")
    
print(f'The max expenses of husband on {max_thing(me)} and wife {max_thing(wife)}')    
             



    
    



        








    


