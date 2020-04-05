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
import sys 

def calorie(p_male,p_female,cal,cal_need,fat,carbs,pro,g_carbs,g_fat,g_pro):
    gender = "male"#{}
    exer = "extreme"# no matter what i put in this doesnt do anytthing 
    goal = "add"#{}
    up = "1"
    down = "0.5" #{}
    m = {1: 100}
    h = {1: 180}
    y = {1: 23}

    #male,stationary
    if (gender == "male" or gender == "female"
        and exer == "stationary" or exer ==  "light" or exer == "moderate" or exer ==  "active" or exer ==  "extreme"
        and goal =="add" or goal == "lose"
        and up == "0.5" or up == "1"
        and down == "0.5" or down == "1"): 
        
        if gender == "male" and exer == "stationary" and goal == "add" and up == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.2 * p_male #cals used per day
            cal_need = cal + 250


        elif gender == "male" and exer == "stationary" and goal == "add" and up == "1":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.2 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "stationary" and goal == "lose" and down == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.2 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "stationary" and goal == "lose" and down =="1":
            p_male = (13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362) #BMR
            cal =  1.2 * p_male #cals used per day
            cal_need = cal - 500
            
#female, stationary 
        elif gender == "female" and exer == "stationary" and  goal =="add" and up == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.2 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "stationary" and  goal =="add" and up == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.2 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "stationary" and  goal =="lose" and down == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.2 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "stationary" and  goal =="lose" and down == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.2 * p_female #cals per day
            cal_need = cal - 500






            

# male light
        elif gender == "male" and exer == "light" and goal == "add" and up == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.25 * p_male  #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "light" and goal == "add" and up == "1":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.25 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "light" and goal == "lose" and down == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.25 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "light" and goal == "lose" and down =="1":
            p_male = (13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362) #BMR
            cal =  1.25 * p_male #cals used per day
            cal_need = cal - 500
            
#female, light  
        elif gender == "female" and exer == "light" and  goal =="add" and up == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.25 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "light" and  goal =="add" and up == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.25 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "light" and  goal =="lose" and down == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.25 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "light" and  goal =="lose" and down == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.25 * p_female #cals per day
            cal_need = cal - 500








# male moderate
        elif gender == "male" and exer == "moderate" and goal == "add" and up == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.5 * p_male #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "moderate" and goal == "add" and up == "1":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.5 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "moderate" and goal == "lose" and down == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.5 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "moderate" and goal == "lose" and down =="1":
            p_male = (13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362) #BMR
            cal =  1.5 * p_male #cals used per day
            cal_need = cal - 500
            
#female, moderate 
        elif gender == "female" and exer == "moderate" and  goal =="add" and up == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.5 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "moderate" and  goal =="add" and up == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.5 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "moderate" and  goal =="lose" and down == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.5 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "moderate" and  goal =="lose" and down == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.5 * p_female #cals per day
            cal_need = cal - 500







# male active
        elif gender == "male" and exer == "active" and goal == "add" and up == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.6 * p_male  #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "active" and goal == "add" and up == "1":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.6 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "active" and goal == "lose" and down == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.6 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "active" and goal == "lose" and down =="1":
            p_male = (13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362) #BMR
            cal =  1.6 * p_male #cals used per day
            cal_need = cal - 500
            
#female, active 
        elif gender == "female" and exer == "active" and  goal =="add" and up == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.6 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "active" and  goal =="add" and up == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.6 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "active" and  goal =="lose" and down == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.6 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "active" and  goal =="lose" and down == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.6 * p_female #cals per day
            cal_need = cal - 500





# male extreme
        elif gender == "male" and exer == "extreme" and goal == "add" and up == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.75 * p_male #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "extreme" and goal == "add" and up == "1":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.75 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "extreme" and goal == "lose" and down == "0.5":
            p_male = 13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362 #BMR
            cal = 1.75 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "extreme" and goal == "lose" and down =="1":
            p_male = (13.397*m[1] + 4.799*h[1] - 5.677*y[1] + 88.362) #BMR
            cal =  1.75 * p_male #cals used per day
            cal_need = cal - 500
            
#female extreme
        elif gender == "female" and exer == "extreme" and  goal =="add" and up == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.75 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "extreme" and  goal =="add" and up == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.75 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "extreme" and  goal =="lose" and down == "0.5":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.75 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "extreme" and  goal =="lose" and down == "1":
            p_female = (9.247*m[1] + 3.098*h[1] - 4.330*y[1] + 447.593) #cal/day
            cal = 1.75 * p_female #cals per day
            cal_need = cal - 500


        else:
            sys.exit("an unknown error has occured")

    else:
        sys.exit("an unknown error has occured")

    carbs = 0.5 * cal_need#cals in carbs
    g_carbs = carbs/4
    fat = 0.3 * cal_need #cals in fat
    g_fat = fat/9
    pro = 0.2 * cal_need #cals in pro
    g_pro = pro/4


    return { "BMR": round(p_male) if gender =="male" else round(p_female),#how to get output to be p_male or p_female depending on condition met ???
             "Total Calories used per day": round(cal),
             "Total Calories needed per day": round(cal_need),
             "Calories of Which Carbs": round(carbs),
             "Grams of Carbs": round(g_carbs),
             "Calories of Which Fat": round(fat),
             "Grams of Fat": round(g_fat),
             "Calories of Which Protein": round(pro),
             "Grams of Protein": round(g_pro)
             }


output = calorie(p_male,
        p_female,
        cal,
        cal_need,
        fat,
        carbs,
        pro,
        g_fat,
        g_carbs,
        g_pro)

print(output)


