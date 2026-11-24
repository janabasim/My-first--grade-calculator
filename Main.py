# My first project - Jana's grades
math = 93
physics = 95
english = 93
chemistry = 91
biology = 95

grades = [math, physics, english, chemistry, biology]
total = sum(grades)
average = total / len(grades)

print(f"My average is: {average:.1f}")

if average >= 95:
    print("Excellent! Qualified for Medicine")
elif average >= 90:
    print("Excellent! Qualified for Computer Science")
else:
    print("Good - keep going")
  
