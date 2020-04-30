import sys 
p_male = { }
p_female = { }
cal = { }
cal_need = { }
fat = { }
carbs = { }
pro = { }
g_fat = { }
g_carbs = { }
g_pro = { }
output = { }

def male_stationary(mass,height,age,const):
    output["p_male"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    output["cal"] = 1.2 * output["p_male"]
    output["cal_need"] = output["cal"] + const
    return output

def female_stationary(mass,height,age,const):
    output["p_female"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.2 * output["p_female"]
    output["cal_need"] = output["cal"] + const
    return output

def male_light(mass,height,age,const):
    output["p_male"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    output["cal"] = 1.25 * output["p_male"]
    output["cal_need"] = output["cal"] + const
    return output

def female_light(mass,height,age,const):
    output["p_female"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.25 * output["p_female"]
    output["cal_need"] = output["cal"] + const
    return output

def male_moderate(mass,height,age,const):
    output["p_male"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    output["cal"] = 1.5 * output["p_male"]
    output["cal_need"] = output["cal"] + const
    return output

def female_moderate(mass,height,age,const):
    output["p_female"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.5 * output["p_female"]
    output["cal_need"] = output["cal"] + const
    return output

def male_active(mass,height,age,const):
    output["p_male"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    output["cal"] = 1.6 * output["p_male"]
    output["cal_need"] = output["cal"] + const
    return output

def female_active(mass,height,age,const):
    output["p_female"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.6 * output["p_female"]
    output["cal_need"] = output["cal"] + const
    return output

def male_extreme(mass,height,age,const):
    output["p_male"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    output["cal"] = 1.76 * output["p_male"]
    output["cal_need"] = output["cal"] + const
    return output

def female_extreme(mass,height,age,const):
    output["p_female"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.75 * output["p_female"]
    output["cal_need"] = output["cal"] + const
    return output
    

def calculator(gender, exer, goal, change, mass, height, age):

#male,stationary
    if (exer == "stationary" or exer ==  "light" or exer == "moderate" or exer ==  "active" or exer ==  "extreme"
        and goal =="add" or goal == "lose"
        and change == "0.5" or change == "1"): 
        
        if gender == "male" and exer == "stationary" and goal == "add" and change == "0.5":
            male_stationary(mass,height,age, 250)
        elif gender == "male" and exer == "stationary" and goal == "add" and change == "1":
            male_stationary(mass,height,age, 500)
        elif gender == "male" and exer == "stationary" and goal == "lose" and change == "0.5":
            male_stationary(mass,height,age, -250) 
        elif gender == "male" and exer == "stationary" and goal == "lose" and change =="1":
            male_stationary(mass,height,age, -500)
            
#female, stationary 
        elif gender == "female" and exer == "stationary" and  goal =="add" and change == "0.5":
            female_stationary(mass,height,age, 250)
        elif gender == "female" and exer == "stationary" and  goal =="add" and change == "1":
            female_stationary(mass,height,age, 500)
        elif gender == "female" and exer == "stationary" and  goal =="lose" and change == "0.5":
            female_stationary(mass,height,age, -250)
        elif gender == "female" and exer == "stationary" and  goal =="lose" and change == "1":
            female_stationary(mass,height,age, -500)

# male light
        elif gender == "male" and exer == "light" and goal == "add" and change == "0.5":
            male_light(mass,height,age, 250)
        elif gender == "male" and exer == "light" and goal == "add" and change == "1":
            male_light(mass,height,age, 500)
        elif gender == "male" and exer == "light" and goal == "lose" and change == "0.5":
            male_light(mass,height,age, -250)            
        elif gender == "male" and exer == "light" and goal == "lose" and change =="1":
            male_light(mass,height,age, -500)
            
#female, light  
        elif gender == "female" and exer == "light" and  goal =="add" and change == "0.5":
            female_light(mass,height,age,250)
        elif gender == "female" and exer == "light" and  goal =="add" and change == "1":
            female_light(mass,height,age,500)
        elif gender == "female" and exer == "light" and  goal =="lose" and change == "0.5":
            female_light(mass,height,age,-250)
        elif gender == "female" and exer == "light" and  goal =="lose" and change == "1":
            female_light(mass,height,age,-500)

# male moderate
        elif gender == "male" and exer == "moderate" and goal == "add" and change == "0.5":
            male_moderate(mass,height,age,250)
        elif gender == "male" and exer == "moderate" and goal == "add" and change == "1":
            male_moderate(mass,height,age,500)
        elif gender == "male" and exer == "moderate" and goal == "lose" and change == "0.5":
            male_moderate(mass,height,age,-250)  
        elif gender == "male" and exer == "moderate" and goal == "lose" and change =="1":
            male_moderate(mass,height,age,-500)
            
#female, moderate 
        elif gender == "female" and exer == "moderate" and  goal =="add" and change == "0.5":
            female_moderate(mass,height,age,250)
        elif gender == "female" and exer == "moderate" and  goal =="add" and change == "1":
            female_moderate(mass,height,age,500)
        elif gender == "female" and exer == "moderate" and  goal =="lose" and change == "0.5":
            female_moderate(mass,height,age,-250)
        elif gender == "female" and exer == "moderate" and  goal =="lose" and change == "1":
            female_moderate(mass,height,age,-500)

# male active
        elif gender == "male" and exer == "active" and goal == "add" and change == "0.5":
            male_active(mass,height,age,250)
        elif gender == "male" and exer == "active" and goal == "add" and change == "1":
            male_active(mass,height,age,500)
        elif gender == "male" and exer == "active" and goal == "lose" and change == "0.5":
            male_active(mass,height,age,-250)   
        elif gender == "male" and exer == "active" and goal == "lose" and change =="1":
            male_active(mass,height,age,-500)
            
#female, active 
        elif gender == "female" and exer == "active" and  goal =="add" and change == "0.5":
            female_active(mass,height,age,250)
        elif gender == "female" and exer == "active" and  goal =="add" and change == "1":
            female_active(mass,height,age,500)
        elif gender == "female" and exer == "active" and  goal =="lose" and change == "0.5":
            female_active(mass,height,age,-250)
        elif gender == "female" and exer == "active" and  goal =="lose" and change == "1":
            female_active(mass,height,age,-500)
            
# male extreme
        elif gender == "male" and exer == "extreme" and goal == "add" and change == "0.5":
            male_extreme(mass,height,age,250)
        elif gender == "male" and exer == "extreme" and goal == "add" and change == "1":
            male_extreme(mass,height,age,500)
        elif gender == "male" and exer == "extreme" and goal == "lose" and change == "0.5":
            male_extreme(mass,height,age,-250)  
        elif gender == "male" and exer == "extreme" and goal == "lose" and change =="1":
            male_extreme(mass,height,age,-500)
            
#female extreme
        elif gender == "female" and exer == "extreme" and  goal =="add" and change == "0.5":
            female_extreme(mass,height,age,250)
        elif gender == "female" and exer == "extreme" and  goal =="add" and change == "1":
            female_extreme(mass,height,age,500)
        elif gender == "female" and exer == "extreme" and  goal =="lose" and change == "0.5":
            female_extreme(mass,height,age,-250)
        elif gender == "female" and exer == "extreme" and  goal =="lose" and change == "1":
            female_extreme(mass,height,age,-500)

        else:
            sys.exit("an unknown error has occured")

    else:
        sys.exit("an unknown error has occured")
        
    if gender == "male":
        p_male = output["p_male"]
    else:
        p_female = output["p_female"]
    cal = output["cal"]
    cal_need = output["cal_need"]
    carbs = 0.5 * output["cal_need"] #cals in carbs
    g_carbs = carbs/4
    fat = 0.3 * output["cal_need"] #cals in fat
    g_fat = fat/9
    pro = 0.2 * output["cal_need"] #cals in pro
    g_pro = pro/4


    return { 'BMR': round(p_male) if gender =="male" else round(p_female),
             "Total Cals used": round(cal),
             "Total Cals needed": round(cal_need),
             "Cals of Which Carbs": round(carbs),
             "Grams of Carbs": round(g_carbs),
             "Cals of Which Fat": round(fat),
             "Grams of Fat": round(g_fat),
             "Cals of Which Protein": round(pro),
             "Grams of Protein": round(g_pro)
             }

