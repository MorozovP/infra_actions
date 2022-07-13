from django.http import HttpResponse


def index(request):
    return HttpResponse('я все сломал')


def second_page(request):
    return HttpResponse('А это вторая страница!')
