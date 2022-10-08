# Write a Python script to create a list of city names taken from the user.
list,i,n=[],0,int(input("Enter how many cities you want to store : "))
while(i<n):
    list.append(input("Enter city name : "))
    i=i+1
print(list)