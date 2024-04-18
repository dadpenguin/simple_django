from django.shortcuts import render, HttpResponse
import random
import json
# Create your views here.

def random_int(requests):
    penguin = {"penguin": []}

    pengy = {
        "name": "Pengy",
        "species": "Emperor Penguin",
        "age": 5,
        "sex": "Male",
        "location": "Antarctica",
        "favorite_food": "Fish",
        "weight_kg": 35,
        "height_cm": 122
    }
    chilly = {
        "name": "Chilly",
        "species": "Adélie Penguin",
        "age": 3,
        "sex": "Female",
        "location": "Antarctica",
        "favorite_food": "Krill",
        "weight_kg": 4,
        "height_cm": 46
    }
    fluffy = {
        "name": "Fluffy",
        "species": "Gentoo Penguin",
        "age": 2,
        "sex": "Male",
        "location": "Antarctica",
        "favorite_food": "Squid",
        "weight_kg": 5,
        "height_cm": 51
    }
    waddle = {
        "name": "Waddle",
        "species": "Rockhopper Penguin",
        "age": 4,
        "sex": "Female",
        "location": "Antarctica",
        "favorite_food": "Crustaceans",
        "weight_kg": 3.5,
        "height_cm": 52
    }

    penguins = [pengy, chilly, fluffy, waddle]
    random_penguin = random.choice(penguins)
    penguin["penguin"].append(random_penguin)

    return HttpResponse(json.dumps(penguin))


