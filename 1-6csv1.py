import csv 
import math 
from datetime import datetime

# csv file name 
filename = "1-6feb.csv"
date='2019-02-01'
uid_status='active'
  
original_row=[]
  
dict1={}
dict2={}

def check_time_difference(t1,t2):
	#date and time format
    f = "%Y-%m-%d %H:%M:%S"
    t1 = datetime.strptime(t1, f)
    t2 = datetime.strptime(t2, f)
    t1_date = datetime(
        t1.year,
        t1.month,
        t1.day,
        t1.hour,
        t1.minute,
        t1.second)

    t2_date = datetime(
        t2.year,
        t2.month,
        t2.day,
        t2.hour,
        t2.minute,
        t2.second)

    t_elapsed = t1_date - t2_date
    #return time difference
    return t_elapsed

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	  
	# extracting field names through first row 
	fields = csvreader.next() 
  
	# extracting each data row one by one 
	for row in csvreader: 
		original_row.append(row)

	for i in original_row:
		current_uid=i[1]
		#taking uid that are active and of 1st feb 	
		if(i[9]==uid_status and i[3][0:10]==date):
			dict2[current_uid]='1'

	for j in original_row:
		current_uid=j[1]
		#checking if this uid has same uid value as 1st feb and active
		if(dict2.get(current_uid)=='1'):
		#checking if dict1 vlaue for the uid exists or not 
			if(dict1.get(current_uid,None)==None):
				dict1[current_uid]=[0,0,0,0]
		# if the value for dictionary 1 is not none for any uid increment
		if(dict1.get(current_uid,None)!=None):
			#incementing the count
			dict1[current_uid][0]+=1
			# checking start and end time null
			if(j[6]!='NULL' and j[7]!='NULL'):
				dict1[current_uid][1]+=1
				#Calculating minutes using check function
				minute=(check_time_difference(j[7],j[6]).seconds)/float(60)
				#ceiling minutes and conveting to int
				minute=int(math.ceil(minute))
				#minutes updated
				dict1[current_uid][3]+=minute
			# check reponse or not correct reponse =(52,200-299)
			if(dict1[current_uid][2]==0 and (j[4]=='52' or (int(j[4])>=200 and int(j[4])<=299))):
				dict1[current_uid][2]=1

	
#writting the file
with open('new12.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(['UID','Total Count','Connected','is_confirmed','Total Time'])
	#writing every row for uid and respetive values
	for key, value in dict1.items():
		writer.writerow([key, value[0],value[1],value[2],value[3]])
csvFile.close()
