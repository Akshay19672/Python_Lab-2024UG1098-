# Convert temperature from Farhenheit to Celcius and vice versa


def celcius_to_fahrenheit(celcius):

  farh=9/5*(celcius)+32

  return farh

def farhenheit_to_celcius(Farhenheit):

  celc= 5/9*(Farhenheit - 32)
  return celc   

choice =int(input("If you want to convert celcius to farhenheit : Press 1 \n else if you want to convert farhenheit to celcius Press 2 "))

if choice==1:
  celcius= float(input(" Enter the temperature in celcius ") )

  result= celcius_to_fahrenheit(celcius)
  print("After Conversion Temperature in farhenheit is :", result)

elif choice==2:

  farhenheit=float(input(" Enter the temperature in celcius ") )

  result2=farhenheit_to_celcius(farhenheit)
  print("After Conversion Temperature in Celcius is :", result2)


else:
  print("Invalid Choice ")


