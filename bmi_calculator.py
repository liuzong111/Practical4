#this program aims to identify whether you are too heavy or too thin
#the two critical value are 18.5 and 30
#bmi is equal to weight/height**2

weight=float(input("w="))
height=float(input("h="))
bmi=weight/(height**2)
a="Your bmi="
if bmi<18.5:
    b="underweight"
elif bmi<30:
    b="normal weight"
else:
    b="overweight"
c=". You are "
print (a+str(bmi)+c+b)
