bangla = int(input("Enter mark for Bangla subject : "))
english = int(input("Enter mark for English subject : "))
math = int(input("Enter mark for Math subject : "))
science = int(input("Enter mark for Science subject : "))

averageMark = (bangla + english + math + science) / 4

if averageMark > 100:
    print("Average mark cannot be greater than 100 please recheck the marks")

elif averageMark < 0:
    print("Average mark cannot be less than 0 please recheck the marks")
    
else:
    if averageMark >= 91:
        print("This student have achive A+")
        
    elif averageMark >= 81:
        print("This student have achive A")

    elif averageMark >= 71:
        print("This student have achive B")
    
    elif averageMark >= 61:
        print("This student have achive C")
        
    elif averageMark >= 41:
        print("This student have achive D")
        
    else:
        print("This student have achive F")
