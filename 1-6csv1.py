import csv 
  
# csv file name 
filename = "1-6feb.csv"
  
# initializing the titles and rows list 
rows = [] 
active_row=[]
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader: 
    	rows.append(row)
    #taking only active and 1st feb data 
    for q in rows:
    	if(q[3][0:10]=='2019-02-01'):
    		active_row.append(q)


    prev_uid=''
    curent_uid=''
    report=[]
    j=0

    for i in active_row:
		curent_uid=i[1]
		if(curent_uid!=prev_uid ):
			report.append(i)
			# adding three dummy rows
			report[j].append(0)
			report[j].append(0)
			report[j].append(0)
			#counter tracking unique uid
			j+=1
			#intializing all counts for one uid
			count=0
			confirmed=0
			is_confirmed=0
			count+=1
			# checking start and end time null
			if(i[6]!='NULL' and i[7]!='NULL'):
				confirmed+=1
			# check reponse or not correct reponse =(52,200-299)
			if(i[4]=='52' or (int(i[4])>=200 and int(i[4])<=299)):
				is_confirmed=1

		

		if(curent_uid==prev_uid):
			#if uid are same
			count+=1
			# checking start and end time null
			if(i[6]!='NULL' and i[7]!='NULL'):
				confirmed+=1
			# check reponse or not correct reponse =(52,200-299)
			if(is_confirmed==0 and (i[4]=='52' or (int(i[4])>=200 and int(i[4])<=299) )):
				is_confirmed=1
		#updating the counts in the uniquie uid .(j-1) coz counter already incremented
		report[j-1][10]=count
		report[j-1][11]=confirmed
		report[j-1][12]=is_confirmed
		#setting the current uid as previous
		prev_uid=curent_uid

#writting the file
with open('new.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(report)

csvFile.close()


    		
