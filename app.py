from flask import Flask, render_template
import random

app = Flask(__name__)

# Add your name in this list!
trainees = [
<<<<<<< HEAD
"Yousif"
]
# Add a food you like (or don't!) in this list!
foods = [
    "kebab"
=======
    "Harry",
    "Bestami",
    "Yusuf",
    "Rhys",
]
# Add a food you like (or don't!) in this list!
foods = [
    "pizza",
    "lasagne",
    "lahmacun",
    "Ramen",
>>>>>>> 5bb9c90f957aa37f33b27d039f3d1d6b8c504c2a
]

@app.route('/')
def home():
    trainee = random.choice(trainees)
    food = random.choice(foods)
    return render_template("index.html", trainee=trainee, food=food)

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)
