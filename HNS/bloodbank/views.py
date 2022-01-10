from django.shortcuts import render

# Create your views here.


def blood_reg(request):
    return render(request, "bloodbank/blood_reg.html")