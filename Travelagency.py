#Tourism Package
print("*--->Welcome to Yogii Tourism<---*")
tour=[]
def goapackage():
    print("**Welcome to Goa Package**")
    print("Package List :\n1.2Night/3Days -> 5000\n2.3Night/4Days -> 7500\n3.4Night/5Days -> 10000")
    pack=int(input("Select Your Package : "))
    if pack==1:
        print("Visited Places Are : Fort Aguada, The Basilica of Bom Jesus Church, Baga Beach, Coco Beach")
        tour.append(5000)
    elif pack==2:
        print("Visited Places Are : Fort Aguada, The Basilica of Bom Jesus Church, Baga Beach, Coco Beach, Goa is a haven for water sports, Dudhsagar Falls")
        tour.append(7500)
    elif pack==3:
        print("Visited Places Are : Fort Aguada, The Basilica of Bom Jesus Church, Baga Beach, Coco Beach, Goa is a haven for water sports, Dudhsagar Falls, scuba diving, Titos lane, Mambos")
        tour.append(10000)
    else:
        print("Select the Package")
    goaguide()
def maldivespackage():
    print("**Welcome to Maldives Package**")
    print("Package List :\n1.2Night/3Days -> 5000\n2.3Night/4Days -> 7500\n3.4Night/5Days -> 10000")
    pack=int(input("Select Your Package : "))
    if pack==1:
        print("Visited Places Are : Male City,COMO Cocoa Island, Vaadhoo Island, Addu Atoll, Maafushi Island")
        tour.append(5000)
    elif pack==2:
        print("Visited Places Are : Male City,COMO Cocoa Island, Vaadhoo Island, Addu Atoll, Maafushi Island, Addu City, Artificial Beach")
        tour.append(7500)
    elif pack==3:
        print("Visited Places Are : Male City,COMO Cocoa Island, Vaadhoo Island, Addu Atoll, Maafushi Island, Addu City, Artificial Beach, Fulhadhoo, Conrad Maldives resort")
        tour.append(10000)
    else:
        print("Select the Package")
    maldivesguide()
def kullimanalipackage():
    print("**Welcome to Kullimanali Package**")
    print("Package List :\n1.2Night/3Days -> 5000\n2.3Night/4Days -> 7500\n3.4Night/5Days -> 10000")
    pack=int(input("Select Your Package : "))
    if pack==1:
        print("Visited Places Are : Rohtang Pass, Manikaran Sahib, Solang Valley, Hampta Pass or Hamta Pass, Parvati Valleyh")
        tour.append(5000)
    elif pack==2:
        print("Visited Places Are : Rohtang Pass, Manikaran Sahib, Solang Valley, Hampta Pass or Hamta Pass, Parvati Valley, Bhrigu Lake, Malana Village")
        tour.append(7500)
    elif pack==3:
        print("Visited Places Are : Rohtang Pass, Manikaran Sahib, Solang Valley, Hampta Pass or Hamta Pass, Parvati Valley, Bhrigu Lake, Malana Village, Kasol, Old Manali, Jogni Waterfalls")
        tour.append(10000)
    else:
        print("Select the Package")
    kullimanaliguide()
def coorgpackage():
    print("**Welcome to Coorg Package**")
    print("Package List :\n1.2Night/3Days -> 5000\n2.3Night/4Days -> 7500\n3.4Night/5Days -> 10000")
    pack=int(input("Select Your Package : "))
    if pack==1:
        print("Visited Places Are : Abbey falls or Abbi Falls, Chiklihole Reservoir, Dubare Elephant Camp, Harangi dam")
        tour.append(5000)
    elif pack==2:
        print("Visited Places Are : Abbey falls or Abbi Falls, Chiklihole Reservoir, Dubare Elephant Camp, Harangi dam, Honnamana Kere (Honnama Lake), Kotebetta")
        tour.append(7500)
    elif pack==3:
        print("Visited Places Are : Abbey falls or Abbi Falls, Chiklihole Reservoir, Dubare Elephant Camp, Harangi dam, Honnamana Kere (Honnama Lake), Kotebetta, Madikeri Fort, Mallalli Falls, Mandalpatti")
        tour.append(10000)
    else:
        print("Select the Package")
    coorgguide()
def goaguide():
    print("Guide : Fransis\t6547893210")
def maldivesguide():
    print("Guide : David\t4578691023")
def kullimanaliguide():
    print("Guide : Gokul\t9876543210")
def coorgguide():
    print("Guide : Nanda\t8795462130")
#Main
print("We Have Tourist packeages are\nGoa\nMaldives\nKulli Manali\nCoorg")
location=input("Enter Your Tourist Place : ")
if location=="goa":
    print("Welcome to Goa Trip Plan")
    goapackage()
elif location=="maldives":
    print("Welcome to Maldives Trip Plan")
    maldivespackage()
elif location=="kullimanali":
    print("Welcome to Kulli Manali Trip Plan")
    kullimanalipackage()
elif location=="coorg":
    print("Welcome to Coorg Trip Plan")
    coorgpackage()
else:
    print("Enter the Correct Location")
#Transport
print("Select the Trasport\nBus\nTrain\nFlight")
transport=input("Enter the Transport Type : ")
if transport=="bus":
    print("Sleeper Bus Transport Ticket Rate is 2500")
    person=int(input("Enter the Travel Persons(below 5 age babys no ticket) : "))
    ticket=person*2500
    tour.append(ticket)
elif transport=="train":
    print("Train Ticket Rates are :\n1.Third AC(3A)   :   1320\n2.Second AC(2A)    :   1890\n3.Sleeper    :   490")
    coach=int(input("Select the Coach : "))
    if coach==1:
        print("Ticket rate is 1320")
        person=int(input("Enter the Travel Persons(below 5 age babys no ticket) : "))
        ticket=person*1320
    elif coach==2:
        print("Ticket rate is 1890")
        person=int(input("Enter the Travel Persons(below 5 age babys no ticket) : "))
        ticket=person*1890
    elif coach==3:
        print("Ticket rate is 490")
        person=int(input("Enter the Travel Persons(below 5 age babys no ticket) : "))
        ticket=person*490
    tour.append(ticket)
elif transport=="flight":
    print("Flight Transport Ticket Rate is 4000")
    person=int(input("Enter the Travel Persons(below 5 age babys no ticket) : "))
    ticket=person*4000
    tour.append(ticket)
else:
    print("Select one Transport")
#Total Amount
print("Bill is :")
print(f"Your Selected Package is : {tour[0]}")
print(f"Your Transport Charge is : {tour[1]}")
total=0
for i in tour:
    total=total+i
print(f"Your Total Amount is {total}")