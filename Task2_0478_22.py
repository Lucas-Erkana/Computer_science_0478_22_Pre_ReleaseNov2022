from secrets import choice
from unicodedata import name
def choose():
    print('Please choose one of the options below:')
    print("1.Accessible")
    print("2.General")
    choice=input('Enter choice: ')
    while choice!="1" and choice!="2":
        print('Choice not valid, only 1 or 2 allowed')
        choice=input('Enter choice: ')
    if choice=="1" or choice=="2":
        return int(choice)

parkingSpace=[] #this array will store all the parking spaces over 14 days, which is 20*14=280
parkingStatus=[]#this array will store the availability of each parking spot or Name and Car licence
days=[]##this array will store the days 1 to 14, first 20 indecies will store 1, second 20 will be day 2
count=0
d=1 #to store the days from 1 to 14
for x in range(1,281): #store all the parking spots in different day arrays
    count=count+1 #stores the car spaces from 1 to 20
    parkingSpace.append('s'+str(count))
    parkingStatus.append('Available')
    days.append(d)
    if x==20: #day 1 car spaces from index 0-19
        d=d+1
        count=0
    elif x==40: #day 2 car space from index 20-39
        count=0
        d=d+1
    elif x==60: #day 3 car space from index 40-59
        count=0
        d=d+1
    elif x==80:#day 4 car space from index 60-79
        count=0
        d=d+1
    elif x==100:#day 5 car space from index 80-99
        count=0
        d=d+1
    elif x==120:#day 6 car space from index 100-119
        count=0
        d=d+1
    elif x==140: #day 7 car space from index 120-139
        count=0
        d=d+1
    elif x==160: #day 8 car space from index 140-159
        count=0
        d=d+1
    elif x==180: #day 9 car space from index 160-179
        count=0
        d=d+1
    elif x==200: #day 10 car space from index 180-199
        count=0
        d=d+1
    elif x==220: #day 11 car space from index 200-219
        count=0
        d=d+1
    elif x==240: #day 12 car space from index 220-239
        count=0
        d=d+1
    elif x==260: #day 13 car space from index 240-259
        count=0
        d=d+1
    elif x==280: #day 14 car space from index 260-279
        count=0
        d=d+1
numberCustomer=int(input('How many customers? :'))
#to store the number of customers making a booking
count=0 #to count each customer upo data entry
maxCustomer=280
#constant that stores the maximum number of customers
#that can make a booking
while numberCustomer>280: #limit check, make sure that not more than 280 customers
    print("Not enough spots available for 14 days")
    numberCustomer = int(input('How many customers? :'))
while numberCustomer>0:
    count=count+1
    er=1 #stores the status of an error, 1 no error, 0 error found 
    spaces=20 #constant that store the number of parking spaces on a day
    while er==1: 
        dayChoice=int(input('Enter the day for customer ' +str(count)+": "))
        #to store the day a customer wants to book
        option=choose()
        access=5
        general=5
        while dayChoice<1 or dayChoice>14 and er==1: #validating the day entered
            print('Day entered not allowed, only days 1 to 14 allowed')
            dayChoice=int(input('Enter the day for customer ' +str(count)+": "))
            if dayChoice>=1 and dayChoice<=14:
                er=0 #change to 0 meaning the day entered is within the range
        for x in range(days.index(dayChoice),days.index(dayChoice)+spaces):
            #loop through the parking spaces on that day
            if parkingStatus[x]=="Available" :
                if option==1 and parkingStatus[x]=="Available":
                    parkingStatus[x]="Name: "+input('Enter name: ')+" car Licence number: "+input("Enter car licence: ")
                    #replace Availability with Name and Car licence number
                elif parkingStatus[x+general]=="Available" and option==2:
                    parkingStatus[x+general]="Name: "+input('Enter name: ')+" car Licence number: "+input("Enter car licence: ")
                    #replace Availability with Name and Car licence number
                print("Day "+ str(days[x]) + " Booked by: ")
                print(parkingStatus[x])
                print("Parking space "+parkingSpace[x])
                er=0
                break
            elif x==days.index(dayChoice)+spaces-1:
                print("No spaces availbe on this day")
                er=1
    numberCustomer=numberCustomer-1 
    #to indicate that we are done with one customer


    