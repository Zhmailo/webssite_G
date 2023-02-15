from django.shortcuts import render


def more(request):
    return render(request, 'about/more.html')