import sys 
from main import request

def stationary(mass,height,age,const):
    output = { }
    if request.form["gender"] == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.2 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def light(mass,height,age,const):
    output = { }
    if request.form["gender"] == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.25 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def moderate(mass,height,age,const):
    output = { }
    if request.form["gender"] == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.5 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def active(mass,height,age,const):
    output = { }
    if request.form["gender"] == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.6 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def extreme(mass,height,age,const):
    output = { }
    if request.form["gender"] == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.75 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def calculator(gender, exer, goal, change, mass, height, age):
    output = { }
    
#male,stationary
    if gender == "male" and exer == "stationary" and goal == "add" and change == "0.5":
        output.update(stationary(mass,height,age, 250))
    elif gender == "male" and exer == "stationary" and goal == "add" and change == "1":
        output.update(stationary(mass,height,age, 500))
    elif gender == "male" and exer == "stationary" and goal == "lose" and change == "0.5":
        output.update(stationary(mass,height,age, -250) )
    elif gender == "male" and exer == "stationary" and goal == "lose" and change =="1":
        output.update(stationary(mass,height,age, -500))
            
#female, stationary 
    elif gender == "female" and exer == "stationary" and  goal =="add" and change == "0.5":
        output.update(stationary(mass,height,age, 250))
    elif gender == "female" and exer == "stationary" and  goal =="add" and change == "1":
        output.update(stationary(mass,height,age, 500))
    elif gender == "female" and exer == "stationary" and  goal =="lose" and change == "0.5":
        output.update(stationary(mass,height,age, -250))
    elif gender == "female" and exer == "stationary" and  goal =="lose" and change == "1":
        output.update(stationary(mass,height,age, -500))

# male light
    elif gender == "male" and exer == "light" and goal == "add" and change == "0.5":
        output.update(light(mass,height,age, 250))
    elif gender == "male" and exer == "light" and goal == "add" and change == "1":
        output.update(light(mass,height,age, 500))
    elif gender == "male" and exer == "light" and goal == "lose" and change == "0.5":
        output.update(light(mass,height,age, -250))          
    elif gender == "male" and exer == "light" and goal == "lose" and change =="1":
        output.update(light(mass,height,age, -500))
            
#female, light  
    elif gender == "female" and exer == "light" and  goal =="add" and change == "0.5":
        output.update(light(mass,height,age,250))
    elif gender == "female" and exer == "light" and  goal =="add" and change == "1":
        output.update(light(mass,height,age,500))
    elif gender == "female" and exer == "light" and  goal =="lose" and change == "0.5":
        output.update(light(mass,height,age,-250))
    elif gender == "female" and exer == "light" and  goal =="lose" and change == "1":
        output.update(light(mass,height,age,-500))

# male moderate
    elif gender == "male" and exer == "moderate" and goal == "add" and change == "0.5":
        output.update(moderate(mass,height,age,250))
    elif gender == "male" and exer == "moderate" and goal == "add" and change == "1":
        output.update(moderate(mass,height,age,500))
    elif gender == "male" and exer == "moderate" and goal == "lose" and change == "0.5":
        output.update(moderate(mass,height,age,-250)  )
    elif gender == "male" and exer == "moderate" and goal == "lose" and change =="1":
        output.update(moderate(mass,height,age,-500))
            
#female, moderate 
    elif gender == "female" and exer == "moderate" and  goal =="add" and change == "0.5":
        output.update(moderate(mass,height,age,250))
    elif gender == "female" and exer == "moderate" and  goal =="add" and change == "1":
        output.update(moderate(mass,height,age,500))
    elif gender == "female" and exer == "moderate" and  goal =="lose" and change == "0.5":
        output.update(moderate(mass,height,age,-250))
    elif gender == "female" and exer == "moderate" and  goal =="lose" and change == "1":
        output.update(moderate(mass,height,age,-500))

# male active
    elif gender == "male" and exer == "active" and goal == "add" and change == "0.5":
        output.update(active(mass,height,age,250))
    elif gender == "male" and exer == "active" and goal == "add" and change == "1":
        output.update(active(mass,height,age,500))
    elif gender == "male" and exer == "active" and goal == "lose" and change == "0.5":
        output.update(active(mass,height,age,-250) )  
    elif gender == "male" and exer == "active" and goal == "lose" and change =="1":
        output.update(active(mass,height,age,-500))
            
#female, active 
    elif gender == "female" and exer == "active" and  goal =="add" and change == "0.5":
        output.update(active(mass,height,age,250))
    elif gender == "female" and exer == "active" and  goal =="add" and change == "1":
        output.update(active(mass,height,age,500))
    elif gender == "female" and exer == "active" and  goal =="lose" and change == "0.5":
        output.update(active(mass,height,age,-250))
    elif gender == "female" and exer == "active" and  goal =="lose" and change == "1":
        output.update(active(mass,height,age,-500))
            
# male extreme
    elif gender == "male" and exer == "extreme" and goal == "add" and change == "0.5":
        output.update(extreme(mass,height,age,250))
    elif gender == "male" and exer == "extreme" and goal == "add" and change == "1":
        output.update(extreme(mass,height,age,500))
    elif gender == "male" and exer == "extreme" and goal == "lose" and change == "0.5":
        output.update(extreme(mass,height,age,-250)  )
    elif gender == "male" and exer == "extreme" and goal == "lose" and change =="1":
        output.update(extreme(mass,height,age,-500))
            
#female extreme
    elif gender == "female" and exer == "extreme" and  goal =="add" and change == "0.5":
        output.update(extreme(mass,height,age,250))
    elif gender == "female" and exer == "extreme" and  goal =="add" and change == "1":
        output.update(extreme(mass,height,age,500))
    elif gender == "female" and exer == "extreme" and  goal =="lose" and change == "0.5":
        output.update(extreme(mass,height,age,-250))
    elif gender == "female" and exer == "extreme" and  goal =="lose" and change == "1":
        output.update(extreme(mass,height,age,-500))

    else:
        sys.exit("an unknown error has occured")

    if gender == "male":
        p_male = output["p"]
    else:
        p_female = output["p"]
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

