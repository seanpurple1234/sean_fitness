def calculator(gender, exer, goal, change, mass, height, age):
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


#male,stationary
    if (gender == "male" or gender == "female"
        and exer == "stationary" or exer ==  "light" or exer == "moderate" or exer ==  "active" or exer ==  "extreme"
        and goal =="add" or goal == "lose"
        and change == "0.5" or change == "1"): 
        
        if gender == "male" and exer == "stationary" and goal == "add" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.2 * p_male #cals used per day
            cal_need = cal + 250


        elif gender == "male" and exer == "stationary" and goal == "add" and change == "1":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.2 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "stationary" and goal == "lose" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.2 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "stationary" and goal == "lose" and change =="1":
            p_male = (13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362) #BMR
            cal =  1.2 * p_male #cals used per day
            cal_need = cal - 500
            
#female, stationary 
        elif gender == "female" and exer == "stationary" and  goal =="add" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.2 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "stationary" and  goal =="add" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.2 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "stationary" and  goal =="lose" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.2 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "stationary" and  goal =="lose" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.2 * p_female #cals per day
            cal_need = cal - 500






            

# male light
        elif gender == "male" and exer == "light" and goal == "add" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.25 * p_male  #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "light" and goal == "add" and change == "1":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.25 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "light" and goal == "lose" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.25 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "light" and goal == "lose" and change =="1":
            p_male = (13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362) #BMR
            cal =  1.25 * p_male #cals used per day
            cal_need = cal - 500
            
#female, light  
        elif gender == "female" and exer == "light" and  goal =="add" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.25 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "light" and  goal =="add" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.25 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "light" and  goal =="lose" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.25 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "light" and  goal =="lose" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.25 * p_female #cals per day
            cal_need = cal - 500








# male moderate
        elif gender == "male" and exer == "moderate" and goal == "add" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.5 * p_male #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "moderate" and goal == "add" and change == "1":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.5 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "moderate" and goal == "lose" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.5 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "moderate" and goal == "lose" and change =="1":
            p_male = (13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362) #BMR
            cal =  1.5 * p_male #cals used per day
            cal_need = cal - 500
            
#female, moderate 
        elif gender == "female" and exer == "moderate" and  goal =="add" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.5 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "moderate" and  goal =="add" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.5 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "moderate" and  goal =="lose" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.5 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "moderate" and  goal =="lose" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.5 * p_female #cals per day
            cal_need = cal - 500







# male active
        elif gender == "male" and exer == "active" and goal == "add" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.6 * p_male  #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "active" and goal == "add" and change == "1":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.6 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "active" and goal == "lose" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.6 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "active" and goal == "lose" and change =="1":
            p_male = (13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362) #BMR
            cal =  1.6 * p_male #cals used per day
            cal_need = cal - 500
            
#female, active 
        elif gender == "female" and exer == "active" and  goal =="add" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.6 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "active" and  goal =="add" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.6 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "active" and  goal =="lose" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.6 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "active" and  goal =="lose" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.6 * p_female #cals per day
            cal_need = cal - 500





# male extreme
        elif gender == "male" and exer == "extreme" and goal == "add" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.75 * p_male #cals used per day
            cal_need = cal + 250

        elif gender == "male" and exer == "extreme" and goal == "add" and change == "1":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.75 * p_male  #cals used per day
            cal_need = cal + 500

        elif gender == "male" and exer == "extreme" and goal == "lose" and change == "0.5":
            p_male = 13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362 #BMR
            cal = 1.75 * p_male  #cals used per day
            cal_need = cal - 250    

        elif gender == "male" and exer == "extreme" and goal == "lose" and change =="1":
            p_male = (13.397*float(mass) + 4.799*float(height) - 5.677*float(age) + 88.362) #BMR
            cal =  1.75 * p_male #cals used per day
            cal_need = cal - 500
            
#female extreme
        elif gender == "female" and exer == "extreme" and  goal =="add" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.75 * p_female  #cals per day
            cal_need = cal + 250
            
        elif gender == "female" and exer == "extreme" and  goal =="add" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.75 * p_female  #cals per day
            cal_need = cal + 500
            
        elif gender == "female" and exer == "extreme" and  goal =="lose" and change == "0.5":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
            cal = 1.75 * p_female #cals per day
            cal_need = cal - 250

        elif gender == "female" and exer == "extreme" and  goal =="lose" and change == "1":
            p_female = (9.247*float(mass) + 3.098*float(height) - 4.330*float(age) + 447.593) #cal/day
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


    return { "BMR": round(p_male) if gender =="male" else round(p_female),
             "Total Cals used": round(cal),
             "Total Cals needed": round(cal_need),
             "Cals of Which Carbs": round(carbs),
             "Grams of Carbs": round(g_carbs),
             "Cals of Which Fat": round(fat),
             "Grams of Fat": round(g_fat),
             "Cals of Which Protein": round(pro),
             "Grams of Protein": round(g_pro)
             }