from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello this is the main page of the syte!')
