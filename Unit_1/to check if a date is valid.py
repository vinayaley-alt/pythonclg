d = int(input("Enter you date : "))
m = int(input("Enter your month : "))
y = int(input("Enter your year : "))

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    if d>=1 and d<=31:
        print("Valid date")
    else:
        print("Invalid Date")
elif m==4 or m ==6 or m==9 or m ==11:
    if d>=1 and d<=30:
      print("Valid Date")
    else: 
     print("Invalid Date")

elif m==2:
   if d>=1 and d<=29:
      if y % 400==0:
          print("Valid Date")
      elif y % 100==0:
         print("Invalid Date")
      elif y % 4==0:
         print("Valid Date")
      else:
         print("Invalid Date")
else:
   print("Invalid Date")           
