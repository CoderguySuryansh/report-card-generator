x=input("ENTER  YOUR NAME:")
y=input("ENTER CLASS :")
z=input("Enter SECTION :")
p=input("ENTER SCHOLAR NO.:")
q=input("AFFLIATION NO. :")

print("\n ENTER YOUR MARKS OF GIVEN SUBJECT ")
a=int(input("\nENTER MARKS OF ENGLISH :"))
b=int(input("ENTER MARKS OF HINDI :"))
c=int(input("ENTER MARKS OF SCIENCE :"))
d=int(input("ENTER MARKS OF MATHS :"))
e=int(input("ENTER MARKS OF COMPUTER :"))

print("-------------------------------------------------------------------------------------------------------------------")
print(   "\t\tSUBJECTS \t\t\t\t\t\t\tMARKS  \t\t GRADE   ")
print("-------------------------------------------------------------------------------------------------------------------")

if    a>=91 and a<=100 :
    print("\t\t ENGLISH                       \t\t\t\t:     ",a     ,"\t\tA+")

elif  a>=75 and a<=90 :
    print("\t\t ENGLISH                       \t\t\t\t:     ",a     ,"\t\tA")

elif  a>=60 and a<=74 :
    print("\t\t ENGLISH                       \t\t\t\t:     ",a     ,"\t\tB+")

elif  a>=60 and a<=69 :
    print("\t\t ENGLISH                       \t\t\t\t:     ",a     ,"\t\tB")
    
elif  a>=50 and a<=59 :
    print("\t\t ENGLISH                       \t\t\t\t:     ",a     ,"\t\tC")

elif  a>=40 and a<=49 :
    print("\t\t ENGLISH                       \t\t\t\t:     ",a     ,"\t\tD")
  
else  :
    print("\t\t ENGLISH                       \t\t\t\t:     ",a     ,"\t\tE")

if  b>=90 and b<=100 :
    print("\t\t HINDI                         \t\t\t\t:     ",b     ,"\t\tA+")

elif  b>=80 and b<=89 :
    print("\t\t HINDI                         \t\t\t\t:     ",b     ,"\t\tA")

elif  b>=70 and b<=79 :
    print("\t\t HINDI                         \t\t\t\t:     ",b     ,"\t\tB+")

elif  b>=60 and b<=69:
    print("\t\t HINDI                         \t\t\t\t:     ",b     ,"\t\tB")

elif  b>=50 and b<=59 :
    print("\t\t HINDI                         \t\t\t\t:     ",b     ,"\t\tC")

elif  b>=40 and b<=49 :
    print("\t\t HINDI                         \t\t\t\t:     ",b     ,"\t\tD")

else  :
    print("\t\t HINDI                         \t\t\t\t:     ",b     ,"\t\tE")


if  b>=90 and b<=100 :
    print("\t\t SCIENCE                       \t\t\t\t:     ",c     ,"\t\tA+")

elif  b>=80 and b<=89 :
    print("\t\t SCIENCE                       \t\t\t\t:     ",c     ,"\t\tA")

elif  b>=70 and b<=79 :
    print("\t\t SCIENCE                       \t\t\t\t:     ",c     ,"\t\tB+")

elif  b>=60 and b<=69:
    print("\t\t SCIENCE                       \t\t\t\t:     ",c     ,"\t\tB")

elif  b>=50 and b<=59 : 
    print("\t\t SCIENCE                       \t\t\t\t:     ",c     ,"\t\tC")

elif  b>=40 and b<=49 :
    print("\t\t SCIENCE                       \t\t\t\t:     ",c     ,"\t\tD")

else  :
    print("\t\t SCIENCE                       \t\t\t\t:     ",c     ,"\t\tE")

if  b>=90 and b<=100 :
    print("\t\t MATHS                         \t\t\t\t:     ",d     ,"\t\tA+")

elif  b>=80 and b<=89 :
    print("\t\t MATHS                         \t\t\t\t:     ",d     ,"\t\tA")

elif  b>=70 and b<=79 :
      print("\t\t MATHS                     \t\t\t\t:     ",d     ,"\t\tB+")

elif  b>=60 and b<=69:
    print("\t\t MATHS                         \t\t\t\t:     ",d     ,"\t\tB")

elif  b>=50 and b<=59 : 
    print("\t\t MATHS                         \t\t\t\t:     ",d     ,"\t\tC")

elif  b>=40 and b<=49 :
    print("\t\t MATHS                         \t\t\t\t:     ",d     ,"\t\tD")

else  :
    print("\t\t MATHS                         \t\t\t\t:     ",d     ,"\t\tE")

if  b>=90 and b<=100 :
    print("\t\t COMPUTER                        \t\t\t:     ",e     ,"\t\tA+")

elif  b>=80 and b<=89 :
    print("\t\t COMPUTER                        \t\t\t:     ",e     ,"\t\tA")

elif  b>=70 and b<=79 :
    print("\t\t COMPUTER                        \t\t\t:     ",e     ,"\t\tB+")

elif  b>=60 and b<=69:
    print("\t\t COMPUTER                        \t\t\t:     ",e     ,"\t\tB")

elif  b>=50 and b<=59 : 
    print("\t\t COMPUTER                        \t\t\t:     ",e     ,"\t\tC")
 
elif  b>=40 and b<=49 :
    print("\t\t COMPUTER                        \t\t\t:     ",e     ,"\t\tD")

else  :
    print("\t\t COMPUTER                        \t\t\t:     ",e     ,"\t\tE")

A=a+b+c+d+e
B=A/5


    
print("-------------------------------------------------------------------------------------------------------------------")
print(   "\t\tTOTAL:",A, "\t\t\t AVERAGE:",B ,"\t\t\t PERCENTAGE:",B,'%')
print("-------------------------------------------------------------------------------------------------------------------")    


if A>=420 and A<=500 :
    print("OVERALL REMARK : Excellent work , keep it up !")

elif A>=350 and A<=499 :
    print("OVERALL REMARK : Good work ! Still work hard")

elif A>=220 and A<=349 :
    print("OVERALL REMARK :Need to work hard ")

else  :
    print("OVERALL REMARK :Need to put extra effort to be the part of best  Good result ")


print("\U0001F917")










































