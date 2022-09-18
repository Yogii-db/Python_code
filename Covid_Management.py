
import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="12345",
    database="yogii_db"
)
mycursor=mydb.cursor()
#mycursor.execute("create table vaccine(id int,name varchar(255),age int,dosename int,doseno int,address varchar(255))" )
#print("table created successfully")
print("Welcome to INDIA COVID19 Data Management System \nWe Have All South Indian State covid details")
def tamilnadu():
    print("Please select the District\nChennai\nCoimbatore\nSalem\nNamakkal")
    district=input("Enter the District Name : ")
    if district=="chennai":
        print("Welcome to Chennai COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 251\t\t  2145\t\t159\t    43\t\t79")
    elif district=="coimbatore":
        print("Welcome to Coimbatore COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 165\t\t  1597\t\t118\t    23\t\t60")
    elif district=="salem":
        print("Welcome to Salem COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 149\t\t  1276\t\t 98\t    35\t\t52")
    elif district=="namakkal":
        print("Welcome to Namakkal COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 180\t\t  1864\t\t170\t    39\t\t70")
    else:
        print("Enter the correct District")
def kerala():
    print("Please select the District\nIdukki\nKollam\nPalakkad\nThrissur")
    district=input("Enter the District Name : ")
    if district=="idukki":
        print("Welcome to Idukki COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 251\t\t  2145\t\t159\t    43\t\t79")
    elif district=="kollam":
        print("Welcome to Kollam COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 165\t\t  1597\t\t118\t    23\t\t60")
    elif district=="palakkad":
        print("Welcome to Palakkad COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 149\t\t  1276\t\t 98\t    35\t\t52")
    elif district=="thrissur":
        print("Welcome to Thrissur COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 180\t\t  1864\t\t170\t    39\t\t70")
    else:
        print("Enter the correct District")
def karnataka():
    print("Please select the District\nBangalore\nGadag\nHaveri\nKolar")
    district=input("Enter the District Name : ")
    if district=="bangalore":
        print("Welcome to Bangalore COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 251\t\t  2145\t\t159\t    43\t\t79")
    elif district=="gadag":
        print("Welcome to Gadag COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 165\t\t  1597\t\t118\t    23\t\t60")
    elif district=="haveri":
        print("Welcome to Haveri COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 149\t\t  1276\t\t 98\t    35\t\t52")
    elif district=="kolar":
        print("Welcome to Kolar COVID Data Management Details")
        print(f"Updated in \nNewly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 180\t\t  1864\t\t170\t    39\t\t70")
    else:
        print("Enter the correct District")
def andhrapradesh():
    print("Please select the District\nSrikakulam\nManyam\nAnakapalli\nEast Godavari")
    district=input("Enter the District Name : ")
    if district=="srikakulam":
        print("Welcome to Srikakulam COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 251\t\t  2145\t\t159\t    43\t\t79")
    elif district=="manyam":
        print("Welcome to Manyam COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 165\t\t  1597\t\t118\t    23\t\t60")
    elif district=="anakapalli":
        print("Welcome to Anakapalli COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 149\t\t  1276\t\t 98\t    35\t\t52")
    elif district=="eastgodavari":
        print("Welcome to East Godavari COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 180\t\t  1864\t\t170\t    39\t\t70")
    else:
        print("Enter the correct District")
def telangana():
    print("Please select the District\nHyderabad\nKhammam\nAdilabad\nJagtial")
    district=input("Enter the District Name : ")
    if district=="hyderabad":
        print("Welcome to Hyderabad COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 251\t\t  2145\t\t159\t    43\t\t79")
    elif district=="khammam":
        print("Welcome to Khammam COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 165\t\t  1597\t\t118\t    23\t\t60")
    elif district=="adilabad":
        print("Welcome to Adilabad COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 149\t\t  1276\t\t 98\t    35\t\t52")
    elif district=="jagtial":
        print("Welcome to Jagtial COVID Data Management Details")
        print("Newly Appointed||Active Cases||Discharges||Dead Count||Home Quaratine\n 180\t\t  1864\t\t170\t    39\t\t70")
    else:
        print("Enter the correct District")
print("Select the your preferance\n1.State and District wise Cases List\n2.vaccination Register\n3.Display the Dose Wise Candidate List")
selection=int(input("Enter the Your Selection : "))
if selection==1:
    print("Select the state for your Refrence \n1.Tamilnadu\n2.Kerala\n3.Karnataka\n4.Andhra pradesh\n5.Telangana")
    state=int(input("Enter the your State Selection number : "))
    if state==1:
        print("Welcome to Tamilnadu COVID Data Management Details")
        tamilnadu()
    elif state==2:
        print("Welcome to Kerala COVID Data Management Details")
        kerala()
    elif state==3:
        print("Welcome to Karnataka COVID Data Management Details")
        karnataka()
    elif state==4:
        print("Welcome to Andhra pradesh COVID Data Management Details")
        andhrapradesh()
    elif state==5:
        print("Welcome to Telangana COVID Data Management Details")
        telangana()
    else:
        print("Select the Correct state number")

        #Here the data will stored in database
elif selection==2:
    print("Welcome to Vaccine Registration")
    sql="insert into vaccine(id,name,age,dosename,doseno,address) values(%s,%s,%s,%s,%s,%s)"
    id=int(input("Enter the Id number : "))
    name=input("Enter your name : ")
    age=int(input("Enter the Age : "))
    dosename=int(input("Enter your dosename: "))
    doseno=int(input("Enter the Dose Number (1st or 2nd) : "))
    address=input("Enter your Address : ")
    val=(id,name,age,dosename,doseno,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Vaccination Booked")
elif selection==3:
    print("Welcome to Dose wise list")
    dosetype=int(input("Select the Does (1 or 2) : "))
    if dosetype==1:
        print("1st Dose Candidates are : ")
        mycursor.execute("select * from vaccine where doseno=1")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
    elif dosetype==2:
        print("2nd Dose Candidates are : ")
        mycursor.execute("select * from vaccine where doseno=2")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
    else:
        print("You Enter the Wrong Dose Number")
else:
    print("Enter the Correct Input")                                                   


