



# def calculate(r,unit,a,n):
#     if n==0:
#         return -1

#     totalFoodRequired=r*unit
#     foodTillNow=0
#     house=0

#     for house in range(n):
#         foodTillNow+=a[house]
#         if foodTillNow >= totalFoodRequired:
#             break

#     if totalFoodRequired > foodTillNow:
#         return 0

#     return house+1

# r = int(input("Enter the number:"))
# unit = int(input("Enter the number"))
# n = int(input("Enter the number"))

# # arr=int(input("enter the  tot number: "))
# a=[]
# for i in range(n):
#     b=int(input('Enter the number: '))
#     a.append(b)

# print(calculate(r,unit,a,n))