import csv 
import math 
import datetime
import os

# csv file name 
#filename = '21-31jan.csv'
uid_status='active'

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date_text
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def check_time_difference(t1,t2):
	#date and time format
	f = "%Y-%m-%d %H:%M:%S"
	t1 = datetime.datetime.strptime(t1, f)
	t2 = datetime.datetime.strptime(t2, f)

	t1_date = datetime.datetime(
			t1.year,
			t1.month,
			t1.day,
			t1.hour,
			t1.minute,
			t1.second
		)

	t2_date = datetime.datetime(
			t2.year,
			t2.month,
			t2.day,
			t2.hour,
			t2.minute,
			t2.second
		)
	#return time difference
	t_elapsed = t1_date - t2_date
	#Calculating minutes using check function
	minute=(t_elapsed.seconds)/float(60)
	#ceiling minutes and conveting to int
	minute=int(math.ceil(minute))
	#minutes return
	return minute

def cal_all_dates(d1,d2):
	newdate1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
	newdate2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
	while(newdate1<=newdate2):
		c=newdate1.strftime('%Y-%m-%d')
		d=processing_file(c)
		write_file(d,c+'.csv')
		newdate1=newdate1+ datetime.timedelta(days=1)



def processing_file(date):

	dict1={}	
	dict2={}


	# reading csv file 
	with open(filename, 'r') as csvfile: 
		# creating a csv reader object 
		csvreader = csv.reader(csvfile) 
		  
		# extracting field names through first row 
		fields = next(csvreader) 
	  
		# extracting each data row one by one 
		for row in csvreader: 
			current_uid=row[1]
			#taking uid that are active and of 1st feb 	
			if(row[9]==uid_status and row[3][0:10]==date):
				dict2[current_uid]='1'
		csvfile.seek(0)
		for j in csvreader:
			current_uid=j[1]
			#checking if this uid has same uid value as 1st feb and active
			if(dict2.get(current_uid)=='1'):
			#checking if dict1 vlaue for the uid does not exist
				if(dict1.get(current_uid,None)==None):
					dict1[current_uid]=[0,0,0,0]
			# if the value for dictionary 1 exist for any uid increment
			if(dict1.get(current_uid,None)!=None):
				#incementing the count
				dict1[current_uid][0]+=1
				# checking start and end time null
				if(j[6]!='NULL' and j[7]!='NULL'):
					dict1[current_uid][1]+=1
					#Calculating minutes using check function
					minutes=check_time_difference(j[7],j[6])
					#adding minutes to current total
					dict1[current_uid][3]+=minutes
				# check reponse or not correct reponse =(52,200-299)
				if(dict1[current_uid][2]==0 and (j[4]=='52' or (int(j[4])>=200 and int(j[4])<=299))):
					dict1[current_uid][2]=1

	return dict1


def write_file(d13,filename):
	#writting the file
	with open(filename, 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(['UID','Total Count','Connected','is_confirmed','Total Time'])
		#writing every row for uid and respetive values
		for key, value in d13.items():
			writer.writerow([key, value[0],value[1],value[2],value[3]])
		csvFile.close()


if __name__ == '__main__':

	print("\033[1;34;40m Enter start date")
	date1=validate(input())
	print("Enter end date ")
	date2=validate(input())
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	print("--FILE OPTIONS--")
	for f in files:
		print(f,end=" ")
	print(" \n Enter File name ")
	filename=input()
	if filename.endswith('.csv'):
		pass
	else:
		print("Not a csv file ")

  
	cal_all_dates(date1,date2)
