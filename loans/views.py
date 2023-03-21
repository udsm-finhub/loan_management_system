from django.shortcuts import render


def sign_in(request):
    return render(request, 'signin.html')


def okay(request):
    return render(request, 'okay.html')


def index(request):
    return render(request, 'index.html')


def blank(request):
    return render(request, 'blank.html')


def notify(request):
    return render(request, 'notify.html')