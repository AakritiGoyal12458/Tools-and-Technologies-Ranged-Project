import os 

os.system("tput setaf 3")

print("\t\t\tWELCOME TO OUR MENU")

print("\t\t\t___________________")

os.system("tput setaf 2")



print("""
press 1 - linux
press 2 - Data structure 
press 3 - Networking 
print 4 - DevOps
press 5 - Machine Learning
""")

print("Enter your choice",end=" ")

a = int(input())
print(a)

os.system("tput setaf 4")

if(a==1) :
	print("""
	press 1 - Basic commands 
	press 2 - Zenity command
	press 3 - Espeak-NG commands
	press 4 - Fun commands
	press 5 - Install software 
	""")

	aa = int(input())
	os.system("tput setaf 7")
	if (aa==1) :
		print("""
		press 1 - Date
		press 2 - Calender 
		""")
		aaa = int(input())
		if(aaa==1) :
			os.system("date")
		if(aaa==2) :
			os.system("cal")

	if (aa==2) :
		print("""
		press 1 - info
		press 2 - calendar                                   
		press 3 - entry
		press 4 - error
		press 5 - file-selection  
		press 6 - list   
		press 7 - notification
		press 8 - question
		press 9 - color-selection  
		press 10 - forms 
		""")
		aaa = int(input())
		if(aaa==1) :
			os.system("""zenity --info --text='ZENITY INFORMATION BOX' --no-wrap --title='ZENITY' --width=60 --height=30 --ok-label=close """)
		if(aaa==2) :
			os.system("""zenity --calendar --text='ARTH 2.0 CALENDAR' --title='ZENITY CALENDAR'""")
		if(aaa==3) :
			os.system("""zenity --entry --text="Name" --entry-text="enter your name" --title='Name entry'""")
		if(aaa==4) :
			os.system('zenity --error --text="PLS TRY AGAIN" --no-wrap ')
		if(aaa==5) :
			os.system("""zenity --file-selection --title="SELECT YOU PIC TO BE UPLOADED" --window-icon="question" --filename="/root/Downloads" --multiple --save """)
		if(aaa==6) :
			os.system(""" zenity --list --text="TEAM MEMBERS NAME" --column=NAME AAKRITI BHAVESH HARSHAL TANMAYE """)
		if(aaa==7) :
			os.system("""zenity --notification --window-icon=THANK.jpg  --text  "HAVE A GOOD DAY!" """)
		if(aaa==8) :
			os.system("""zenity   --question  --title  "Alert" --text "ARE YOU SURE TO SUBMIT THE FORM?"\ """)
		if(aaa==9) :
			os.system(""" zenity --color-selection --show-palette --title="select your fav colour" """)
		if(aaa==10) :
			os.system("""zenity --forms --title=Registration Form --forms --add-entry=FirstName --forms --add-entry=LastName --forms --add-entry=Age --forms --add-entry=Height --forms --add-entry=Weight --add-password=Password --add-calendar=Date_of_joining """)
		


		




input()














	
