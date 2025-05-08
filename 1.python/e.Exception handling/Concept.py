# x = input("Enter a number 1:\n")
# y = input("Enter a number 2:\n")

# try:
#     r = int(x)/int(y)
# except ZeroDivisionError as e:
#     print("The error occured :",e)
#     r = 0

# print("The division is : ",r)


lst = [int(x) for x in input().split()]

try:
    i = int(input("Enter Index: "))
    print(lst[i])
except Exception as e:
    print("The Exception occured :",e)
finally:
    print("Give Within range")









