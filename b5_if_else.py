marks = int(input("Enter the marks: "))  

if marks >= 80:  
   print("A+")
elif 75 <= marks < 80:
   print("A")
elif 70 <= marks < 75:
   print("A-")
elif 65 <= marks < 70:
   print("B+")
elif 60 <= marks < 65:
   print("B")
elif 55 <= marks < 60:
   print("B-")
elif 50 <= marks < 55:
   print("C+")
elif 45 <= marks < 50:
   print("C")
elif 40 <= marks < 45:
   print("D")
else:  
   print("F")  