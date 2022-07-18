from secrets import choice
from unicodedata import name
def choose():
    print('Would you like accessible parking? ')
    print("1.Accessible parking")
    print("2.General parking")
    choice=input('Enter choice: ')
    while choice!="1" and choice!="2" and choice!="3":
        print('Choice not valid, only 1 or 2 allowed')
        choice=input('Enter choice: ')
    if choice=="1" or choice=="2":
        return int(choice)

parkingSpace=[] #this array will store all the parking spaces over 14 days, which is 20*14=280
parkingStatus=[]#this array will store the availability of each parking spot or Name and Car licence
days=[]##this array will store the days 1 to 14, first 20 indecies will store 1, second 20 will be day 2
count=0
parking='a'#this will store g for general parking space, and a for accessible parking space
d=1 #to store the days from 1 to 14 for including general and accessible parking
#day 1 has now 20 parking, 5 accessible and 13 general parking
for x in range(1,281): #store all the parking spots in different day arrays + genreal and accessible parking
    count=count+1 #stores the car spaces from 1 to 20
    parkingSpace.append(parking+str(count))
    parkingStatus.append('Available')
    days.append(d)
    if x==5: #day 1 general parking spaces from index 5-19
        d=1
        count=0
        parking='g'
    elif x==20: #day 2 accessible parking spaces from index 20-24
        d=2
        count=0
        parking='a'
    elif x==25: #day 2 general parking space from 25-39
        count=0
        d=2
        parking='g'
    elif x==40: #day 3 accessible parking from 40-44
        count=0
        d=3
        parking='a'
    elif x==45: #day 3 general parking space from 45-59
        count=0
        d=3
        parking='g'
    elif x==60: #day 4 accessible parking from 60-64
        count=0
        d=4
        parking='a'
    elif x==65: #day 4 general parking space from 65-79
        count=0
        d=4
        parking='g'
    elif x==80: #day 5 accessible parking from 80-84
        count=0
        d=5
        parking='a'
    elif x==85: #day 5 general parking space from 85-99
        count=0
        d=5
        parking='g'
    elif x==100: #day 6 accessible parking from 100-104
        count=0
        d=6
        parking='a'
    elif x==105: #day 6 general parking space from 105-119
        count=0
        d=6
        parking='g'
    elif x==120: #day 7 accessible parking from 120-124
        count=0
        d=7
        parking='a'
    elif x==125: #day 7 general parking space from 125-139
        count=0
        d=7
        parking='g'
    elif x==140: #day 8 accessible parking from 140-144
        count=0
        d=8
        parking='a'
    elif x==145: #day 8 general parking space from 145-159
        count=0
        d=8
        parking='g'
    elif x==160: #day 9 accessible parking from 160-164
        count=0
        d=9
        parking='a'
    elif x==165: #day 9 general parking space from 165-179
        count=0
        d=9
        parking='g'
    elif x==180: #day 10 accessible parking from 180-184
        count=0
        d=10
        parking='a'
    elif x==185: #day 10 general parking space from 185-199
        count=0
        d=10
        parking='g'
    elif x==200: #day 11 accessible parking from 200-204
        count=0
        d=11
        parking='a'
    elif x==205: #day 11 general parking space from 205-219
        count=0
        d=11
        parking='g'
    elif x==220: #day 12 accessible parking from 220-224
        count=0
        d=12
        parking='a'
    elif x==225: #day 12 general parking space from 225-239
        count=0
        d=12
        parking='g'
    elif x==240: #day 13 accessible parking from 240-244
        count=0
        d=13
        parking='a'
    elif x==245: #day 13 general parking space from 245-259
        count=0
        d=13
        parking='g'
    elif x==260: #day 14 accessible parking from 260-264
        count=0
        d=14
        parking='a'
    elif x==265: #day 14 general parking space from 265-279
        count=0
        d=14
        parking='g'   
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
    while er==1: 
        dayChoice=int(input('Enter the day for customer ' +str(count)+": "))
        #to store the day a customer wants to book
        while dayChoice<1 or dayChoice>14 and er==1: #validating the day entered
            print('Day entered not allowed, only days 1 to 14 allowed')
            dayChoice=int(input('Enter the day for customer ' +str(count)+": "))
            if dayChoice>=1 and dayChoice<=14:
                er=0 #change to 0 meaning the day entered is within the range
        if choose()==1:
            start=days.index(dayChoice) #store the starting index on that day for accessible parking
            end=days.index(dayChoice)+5#stores the ending index on that day for acceessible parking
            counter=1 #this will increase from 1 to 5 
        else:
            start=days.index(dayChoice)+19
            end=days.index(dayChoice)+4
            counter=-1 #this will decrease for loop from 20 to 6
        for x in range(start,end,counter):
            #loop through the parking spaces on that day
            if parkingStatus[x]=="Available":
                parkingStatus[x]="Name: "+input('Enter name: ')+" car Licence number: "+input("Enter car licence: ")
                #replace Availability with Name and Car licence number
                print("Day "+ str(days[x]) + " Booked by: ")
                print(parkingStatus[x])
                print("Parking space "+parkingSpace[x])
                er=0
                break
            elif x==end-1 or x==end+1: #compare x with end if it is Accessible, 
                #compare x with end+1 if it General parking
                print("No spaces availbe on this day")
                er=1               
        numberCustomer=numberCustomer-1 
print(parkingSpace)
print(parkingStatus)
print(days)


    