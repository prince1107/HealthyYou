from flask import Flask, render_template, request, redirect
from random import randint

app = Flask(__name__)

'''
Note: this sample code does NOT store the dogs data to a database.
Instead, we store the dogs data in memory in the below "dogs" Python object.
Consequently, the dogs data is reset every time the application is restarted.
If you would like, you can replace this dogs data structure with your own database connection logic.
'''

food = [
    {
        "id": 1,
        "name": "Spot",
        "cuisine": "Boston Terrier",
        "calories": 2,
        "photo_name": "dog_1.jpg",
        "available_for_adoption": True
    },
    {
        "id": 2,
        "name": "Pixie",
        "breed": "Pug",
        "age": 7,
        "photo_name": "dog_2.jpg",
        "available_for_adoption": True
    },
    {
        "id": 3,
        "name": "Ellie",
        "breed": "Golden Retriever",
        "age": 3,
        "photo_name": "dog_3.jpg",
        "available_for_adoption": True
    }
]


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/dogs', methods=['GET'])
@app.route('/dogs/<food_id>', methods=['GET'])
def all_food(food_id=None):
    if food_id:  # show single dog
        single_dog = [food[int(food_id)]] if len(food)-1 >= int(food_id) else []
        return render_template('dogs.html', food=single_dog)
    else:  # show all dogs
        return render_template('dogs.html', food=food)


@app.route('/random-dog', methods=['GET'])
def random_dog():
    random_food_index = randint(0, len(food)-1)  # generate a random index in the dogs array
    random_food = food[random_food_index]
    return render_template('random_dog.html', food=random_food)


@app.route('/create-dog', methods=['GET', 'POST'])
def create_dog():
    food_name = request.form['food_name']
    food_cuisine = request.form['food_cuisine']
    food_calories = request.form['food_calories']
    food_is_available_for_adoption = True

    new_food = {
        "id": len(food),
        "name": food_name,
        "cuisine": food_cuisine,
        "calories": food_calories,
        "photo_name": "placeholder_dog.png",
        "available_for_adoption": food_is_available_for_adoption
    }

    food.append(new_food)

    return redirect('/dogs')


if __name__ == "__main__":
    app.run(debug=True)
