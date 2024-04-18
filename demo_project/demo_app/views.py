from django.shortcuts import render, HttpResponse
import random
# Create your views here.

def random_int(requests):
    random_integer = random.randint(0, 100)
    return HttpResponse(f"random Integer: {random_integer}")


