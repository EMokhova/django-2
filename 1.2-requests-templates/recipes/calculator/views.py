from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home(request):
    msg = 'Книга рецептовя. Передайте в URL название блюда'
    return HttpResponse(msg)

def recipes(request, dish):
    if dish in DATA:
        data = DATA[dish]
        servings = request.GET.get('servings', None)

        if servings:
            calculate = dict()
            for key, value in data.items():
                new_value = value * int(servings)
                calculate[key] = new_value
            context = {
                'dish': dish,
                'recipe': calculate
            }
        else:
            context = {
                'dish': dish,
                'recipe': data
            }

    else:
        context = None

    return render(request, 'calculator/index.html', context)


