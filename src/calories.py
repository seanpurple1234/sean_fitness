import sys 
from main import request

def _stationary(gender,mass,height,age,const):
    output = { }
    if gender == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.2 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def _light(gender,mass,height,age,const):
    output = { }
    if gender == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.25 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def _moderate(gender,mass,height,age,const):
    output = { }
    if gender == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.5 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def _active(gender,mass,height,age,const):
    output = { }
    if gender == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.6 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def _extreme(gender,mass,height,age,const):
    output = { }
    if gender == "male":
        output["p"] = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
    else:
        output["p"] = 9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593 #BMR
    output["cal"] = 1.75 * output["p"]
    output["cal_need"] = output["cal"] + const
    return output

def calculator(gender, exer, goal, change, mass, height, age):
    output = { }
    
#stationary
    if exer == "stationary" and goal == "add" and change == "0.5":
        output.update(_stationary(gender,mass,height,age, 250))
    elif exer == "stationary" and goal == "add" and change == "1":
        output.update(_stationary(gender,mass,height,age, 500))
    elif exer == "stationary" and goal == "lose" and change == "0.5":
        output.update(_stationary(gender,mass,height,age, -250) )
    elif exer == "stationary" and goal == "lose" and change =="1":
        output.update(_stationary(gender,mass,height,age, -500))

#light
    elif exer == "light" and goal == "add" and change == "0.5":
        output.update(_light(gender,mass,height,age, 250))
    elif exer == "light" and goal == "add" and change == "1":
        output.update(_light(gender,mass,height,age, 500))
    elif exer == "light" and goal == "lose" and change == "0.5":
        output.update(_light(gender,mass,height,age, -250))          
    elif exer == "light" and goal == "lose" and change =="1":
        output.update(_light(gender,mass,height,age, -500))

#moderate
    elif exer == "moderate" and goal == "add" and change == "0.5":
        output.update(_moderate(gender,mass,height,age,250))
    elif exer == "moderate" and goal == "add" and change == "1":
        output.update(_moderate(gender,mass,height,age,500))
    elif exer == "moderate" and goal == "lose" and change == "0.5":
        output.update(_moderate(gender,mass,height,age,-250)  )
    elif exer == "moderate" and goal == "lose" and change =="1":
        output.update(_moderate(gender,mass,height,age,-500))

#active
    elif exer == "active" and goal == "add" and change == "0.5":
        output.update(_active(gender,mass,height,age,250))
    elif exer == "active" and goal == "add" and change == "1":
        output.update(_active(gender,mass,height,age,500))
    elif exer == "active" and goal == "lose" and change == "0.5":
        output.update(_active(gender,mass,height,age,-250) )  
    elif exer == "active" and goal == "lose" and change =="1":
        output.update(_active(gender,mass,height,age,-500))
            
#extreme
    elif exer == "extreme" and goal == "add" and change == "0.5":
        output.update(_extreme(gender,mass,height,age,250))
    elif exer == "extreme" and goal == "add" and change == "1":
        output.update(_extreme(gender,mass,height,age,500))
    elif exer == "extreme" and goal == "lose" and change == "0.5":
        output.update(_extreme(gender,mass,height,age,-250)  )
    elif exer == "extreme" and goal == "lose" and change =="1":
        output.update(_extreme(gender,mass,height,age,-500))

    else:
        sys.exit("an unknown error has occured")

    #if gender == "male":
    p_male = output["p"]
    #else:
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

