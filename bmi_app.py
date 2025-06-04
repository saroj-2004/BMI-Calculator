from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        height_m = height / 100 
        bmi = round(weight / (height_m ** 2), 2)
        category = ""
        if bmi < 18.5:
            category = "Underweight 😟"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight 🙂"
        elif 25 <= bmi < 29.9:
            category = "Overweight 😐"
        else:
            category = "Obese 😟"

        return render_template('index.html', bmi=bmi, category=category, weight=weight, height=height)
    except:
        return render_template('index.html', error="Invalid input! Please enter valid numbers.")
    
if __name__ == '__main__':
    app.run(debug=True)

