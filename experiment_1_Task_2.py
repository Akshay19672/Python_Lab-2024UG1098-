# Create a program to compute student marks(Average , Grade , Classification )



total_marks = 500

marks1= int(input("Enter subject 1 marks"))
marks2= int(input("Enter subject 2 marks"))
marks3= int(input("Enter subject 3 marks"))
marks4= int(input("Enter subject 4 marks"))
marks5= int(input("Enter subject 5 marks"))

marks_obtained=marks1+marks2+marks3+marks4+marks5

average=(marks_obtained)/5
percentage=(marks_obtained/total_marks)*100



print("Percentage Obtained :", percentage)

if percentage>=90:
  print("GRADE : A")

elif percentage>=80 and percentage<=89:
  print("GRADE : B")  

elif percentage>=70 and percentage<=79:
  print("GRADE : C")  

elif percentage>=60 and percentage<=69:
  print("GRADE : D")

else:
  print("GRADE : F")  
