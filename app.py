from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def bmi():
    Bmi = None
    if request.method== "POST" :
        weight = request.form.get('weight')
        height = request.form.get('height')
        if weight and height:  # Ensure values are not None
            try:
                weight = float(weight)
                height = float(height)

                if height > 0:  # Prevent division by zero
                    Bmi = weight / ((height / 100) ** 2)
                else:
                    Bmi = "Invalid height"
            except ValueError:
                Bmi = "Invalid input"
    return render_template('index.html', Bmi =Bmi)
app.run()