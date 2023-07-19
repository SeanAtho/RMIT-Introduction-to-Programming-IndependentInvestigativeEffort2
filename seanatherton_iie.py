#imports sys module

import sys

#The average working hours
averagehourday = 8

#List of hours, likely unnecessary
hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#Prompt for user to input their chosen Name which will be assigned to "name" 
sys.stdout.write("Enter your name:")
name = sys.stdin.readline().strip()

#Greetings containing the the the user input which was assigned to "name" and a print function asking for how many hours worked today
sys.stdout.write("Hello "+name+" ! How many hours did you work today? ")

#Takes the users input to the previous print function and assigns it to "hours", then comparing it against the average work hours or "averagehourday" which is given the value of 8. 
hours = int(sys.stdin.readline().strip())
if hours > averagehourday:
    sys.stdout.write("You worked more than the average hours today. \n")
if hours < averagehourday:
    sys.stdout.write("You worked under the average hours today. \n")
if hours == 8:
    sys.stdout.write("Youve worked the average hours today, no wasted effort.\n")

#Checking of users original name input which was assigned to "name" and then compares it against the what was assigned to "response"
sys.stdout.write("Just to check, whats your name again?")
response = sys.stdin.readline().strip()
#If "name" and "response" are different it displays to the user both what they was inputted and assigned to the "name" and "response" to assist with trouble-shooting 
while response != name:
    sys.stdout.write(" Are you sure? According to our system it should be "+name+" not "+response+"\n")
#If the user has inputted a different response than the one given to "name" the system will ask them to try again
    sys.stdout.write("Please enter your original name\n")
    response = (sys.stdin.readline().strip())
#When the response and original name input are the same or have been resolved
if response == name:
    sys.stdout.write("Glad we got that sorted out, have a nice day!")
