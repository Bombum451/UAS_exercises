print("Please enter biological sex.")

gender = str(input())
gender = gender.upper()

male = ["MALE", "MAN", "M", "MASCULINE", "MASC"]
female = ["FEMALE", "WOMAN", "W", "F", "FEMININE", "FEM"]

if gender in male:
    gender = "M"
elif gender in female:
    gender = "F"
else:
    gender = "invalid"
    print("Sorry, please try again.")
    
if gender != "invalid":
    print ("Please enter hemoglobin level (g/l).")
    hemoglobin = float(input())
    
if gender == "M":
    if hemoglobin < 134:
        level = "low"
    elif hemoglobin > 167:
        level = "high"
    else:
        level = "normal"
        
if gender == "F":
    if hemoglobin < 117:
        level = "low"
    elif hemoglobin > 155:
        level = "high"
    else:
        level = "normal"
        
if gender != "invalid":
    print("Hemoglobin level: " + level)