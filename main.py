from flask import render_template
from flask import Flask
from flask import request
from src import calories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'calculator'

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/calculator')
def calculator():
  return render_template('calculator.html')

@app.route('/calculator', methods=['POST'])
def calculator_submission():
  # What the server received from the HTML submission
  # Look at the terminal and try changing the values before submitting and see the difference
  print(request.form)
  gender = request.form["gender"]
  goal = request.form["goal"]
  change = request.form["change"]
  exercise = request.form["exercise"]
  mass = request.form["mass"] 
  height = request.form["height"]
  age = request.form["age"]
 

  # extract the rest of the values from the form, the key for the request.form[KEY] will
  # be the same as the values specified for the name attribute set in the HTML.

  # after you have extracted all the values, call your calorie counter script
  # Uncomment the next line and make sure the parameter variable names match the ones declared above
  result = calories.calculator(gender, exercise, goal, change, mass, height, age)
  print(result)
  # check what the result is printing out

  
  # Think, mhhmm how do I connect these result to the html file. I left you a hint with the 
  # line below, I declared a html varaible called `message` and then used it in the result.html
  # You gotta figure out how to show these results in the html file...
  return render_template('results.html',BMR=result['BMR'], CalsUsed=result['Total Cals used'], CalsNeed=result['Total Cals needed'],
   CalsCarbs=result['Cals of Which Carbs'], GramsCarbs=result['Grams of Carbs'], CalsFat=result['Cals of Which Fat'],
   GramsFat=result['Grams of Fat'], CalsPro=result['Cals of Which Protein'], GramsPro=result['Grams of Protein'])
  
if __name__ == "__main__":
    app.run(host='0.0.0.0')

