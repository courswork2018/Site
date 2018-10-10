from django.shortcuts import render


def post_list(request):
    n = ['Карвцова Анастасия : документальное руководство АС','Васильева Мария : разработчик АС','Грохотова Екатерина : тестировщик АС']
    return render(request,'mysite/index.html', context={'names':n})
