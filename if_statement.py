def find_age(age):
    if age <0 or age >100: 
        print("error") 
    elif age >= 0 and age <=3:
        print("toddler")
    elif age >= 4 and age <=12:
        print("child")
    elif age >= 13 and age <=17:
        print("teen")
    elif age == 18:
        print("debut")
    elif age >= 19 and age <=100:
        print("adult")
      
age = int(input("input your age: "))    
find_age(age) 
