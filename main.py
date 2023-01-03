from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie_back import calories
from calorie_back import temperature

app = Flask(__name__)


class HomePage(MethodView):
    """Home page of the web application.
    """
    def get(self):
        return render_template('index.html')


class CaloriePage(MethodView):
    """Calculator interface which takes some input variables about the user and
    then outputs number of calories on the same page.
    """
    def get(self):
        calorie = CalorieForm()
        return render_template('calculate_page.html', calorie_form=calorie)

    def post(self):
        calorie = CalorieForm(request.form)
        weight = calorie.weight.data
        height = calorie.height.data
        age = calorie.age.data
        country = calorie.country.data
        city = calorie.city.data

        calories_input = calories.Calories(float(weight), float(height), float(age))
        temperature_input = temperature.Temperature(country, city)
        num_calories = calories_input.calculate(temperature_input)
        return render_template('calculate_page.html', calorie_form = calorie,
                               num_calories=num_calories, result = True)


class CalorieForm(Form):
    """All input information is saved in this class.
    """
    weight = StringField("Weight: ", default=80)
    height = StringField("Height: ", default=180)
    age = StringField("Age: ", default=20)
    country = StringField("Country: ", default="Italy")
    city = StringField("City: ", default="Rome")
    button = SubmitField("Calculate calories")


app.add_url_rule("/", view_func=HomePage.as_view('home_page'))
app.add_url_rule("/calorie_page", view_func=CaloriePage.as_view('calorie_page'))

app.run()
