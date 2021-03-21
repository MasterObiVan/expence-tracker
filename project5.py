def add_money():
	addmo=0
	print("\n\n")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    ADD MONEY TO WALET    ")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t**************************")
	print("\n")
	addM=int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tENTER THE AMOUNT FOR ADDING TO THE WALET :"))
	sql = "SELECT BALANCE FROM t_balance ORDER BY SERIAL_NO DESC LIMIT 1"
	mycursor.execute(sql)
	res = mycursor.fetchone()
	addmo=addM+res[0]
	sql="INSERT INTO t_balance (BALANCE) VALUES (%s)", (addmo,)
	#val=(addmo)
	mycursor.execute(*sql)
	mydb.commit()
	print('\n')
	print("THE AMOUNT IS ADDED TO THE BALANCE".center(columns))


def add_expence():
	bal=0
	mulval=0
	print("\n\n")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t        ADD EXPENCE       ")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t**************************")	
	print("\n\n")
	expenditure=input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ENTER THE NAME OF THE EXPENDITURE :")
	EXamt=int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    ENTER THE AMOUNT OF THE EXPENDITURE :"))
	sql = "SELECT BALANCE FROM t_balance ORDER BY SERIAL_NO DESC LIMIT 1 "
	mycursor.execute(sql)
	res = mycursor.fetchone()
	if EXamt>res[0]:
		print("\n")
		print("INSUFFICENT BALANCE!!!!!".center(columns))
	else:
		sql="SELECT EXPENCE FROM t_expence WHERE EXPENDITURE=%s", (expenditure,)
		#val=(expenditure)
		mycursor.execute(*sql)
		resu=mycursor.fetchone()
		print(resu)
		if resu:
			mulval=EXamt+resu[0]
			sql="UPDATE t_expence SET EXPENCE = %s WHERE EXPENDITURE=%s", (mulval,expenditure,)
			#val=(mulval)
			mycursor.execute(*sql)
			mydb.commit()
		else:
			sql="INSERT INTO t_expence (EXPENDITURE,EXPENCE) VALUES (%s,%s)"
			val=(expenditure,EXamt)
			mycursor.execute(sql,val)
			mydb.commit()
			bal=res[0]-EXamt
			sql="INSERT INTO t_balance (BALANCE) VALUES (%s)", (bal,)
			#val=(res[0]-EXamt)
			mycursor.execute(*sql)
			mydb.commit()
			#result=mycursor.fetchone()
			#print(result[2])
			


def view_expence():
	totEX=0
	print("\n\n")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t         VIEW EXPENCE      ")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t **************************")	
	print("\n\n")
	print("\t\t\t\t\t\t\t\t=========================================")	
	mycursor.execute("SELECT * FROM T_EXPENCE")
	myresult = mycursor.fetchall()
	for x in myresult:
  		print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",x)

	print("\t\t\t\t\t\t\t\t=========================================")
	print("\n")	
			


def view_balance():
	print("\n\n")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t           BALANCE         ")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t **************************")	
	print("\n")
	sql = "SELECT BALANCE FROM t_balance ORDER BY SERIAL_NO DESC limit 1 "
	mycursor.execute(sql)
	res = mycursor.fetchone()
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   THE BALANCE AMOUNT IS :",res[0])

		


import shutil
columns = shutil.get_terminal_size().columns
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="expence",
)
mycursor = mydb.cursor()




print("\n")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t       EXPENCE TRACKER     ")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  *************************")
print("\n")

op='y'
while(op=='y'):
	print("\n")
	print("\t\t\t\t\t=================================================================================================")
	print("\n")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*******************************")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 1 : ADD MONEY TO ACCOUNT  **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 2 : ADD EXPENCE           **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 3 : VIEW EXPENCE          **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 4 : VIEW BALANCE          **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 5 : EXIT                  **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*******************************")
	print("\n")
	print("\n")
	try:
		n=int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  ENTER YOUR OPTION :"))
	except:
		print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t               ONLY USE APPROPRIATE INPUTS!!!!")

	if n==1:
		add_money()
	elif n==2:
		add_expence()
	elif n==3:
		view_expence()	
	elif n==4:
		view_balance()
	elif n==5:
		exit()	
	else:
		print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t              INVALID OPTION ")

	op=input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDO YOU WISH TO CONTINUE (y/n) :")



