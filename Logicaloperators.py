#Using AND operator to check college admission eligiblity
Marks = 85
Entrance_exam_eligible = True

if Marks >= 60 and Entrance_exam_eligible:
    print("You are eligible for college admission")
else:
    print("You are not eligible for college admission")



#Using OR operator to checkif a person is eligible for a driving license
Age = 20
Has_special_permit = False

if Age >= 18 and not Has_special_permit:
    print("You are eligible for a driving license")
else:
    print("You are not eligible for a driving license")



#Using NOT operator to check if a mobile phone is on or off
phone_on = True
if not phone_on:
    print("Phone is off,turn it on")
else:
    print("Phone is on,you can use it")

