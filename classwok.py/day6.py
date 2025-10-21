
attendance = [18, 20, 19, 15, 21]

full_days = 0
total_attendance = 0


for students in attendance:
    total_attendance += students  

    
    if students >= 20:
        print("Full")
        full_days += 1
    else:
        print("Not Full")

print("\nNumber of full days:", full_days)
print("Total attendance over 5 days:", total_attendance)
