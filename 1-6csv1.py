import csv 
  
# csv file name 
filename = "1-6feb.csv"
date='2019-02-01'
uid_status='active'
  
  
dict1={}
dict2={}
# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	  
	# extracting field names through first row 
	fields = csvreader.next() 
  
	# extracting each data row one by one 
	for row in csvreader: 
		current_uid=row[1]
		#taking uid that are active and of 1st feb 	
		if(row[9]==uid_status and row[3][0:10]==date):
			dict2[current_uid]='1'
		#checking if this uid has same uid value as 1st feb and active
		if(dict2.get(current_uid)=='1'):
		#checking if dict1 vlaue for the uid exists or not 
			if(dict1.get(current_uid,None)==None):
				dict1[current_uid]=[0,0,0]
		# if the value for dictionary 1 is not none for any uid increment
		if(dict1.get(current_uid,None)!=None):
			#incementing the count
			dict1[current_uid][0]+=1
			# checking start and end time null
			if(row[6]!='NULL' and row[7]!='NULL'):
				dict1[current_uid][1]+=1
			# check reponse or not correct reponse =(52,200-299)
			if(dict1[current_uid][2]==0 and (row[4]=='52' or (int(row[4])>=200 and int(row[4])<=299))):
				dict1[current_uid][2]=1

	
#writting the file
with open('new.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(['UID','Total Count','Connected','is_confirmed'])
	for key, value in dict1.items():
		writer.writerow([key, value[0],value[1],value[2]])
csvFile.close()

