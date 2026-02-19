# University Admission Eligibility
percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ")
entrance_score = int(input("Enter entrance exam score: "))

if percentage < 75:
    print("Not Eligible: Minimum 75% required in 12th grade. - universityadmission.py:7")

elif maths != "yes":
    print("Not Eligible: Mathematics subject is required. - universityadmission.py:10")

elif entrance_score < 80:
    print("Not Eligible: Entrance exam score must be at least 80. - universityadmission.py:13")

else:
    print("Congratulations! You are Eligible for Admission. - universityadmission.py:16")