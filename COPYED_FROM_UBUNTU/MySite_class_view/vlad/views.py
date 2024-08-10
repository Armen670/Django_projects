import django.http
from django.shortcuts import render

# Create your views here.
def main(request):
    context = {

    }
    return render(request,'vlad/index.html',context = context)