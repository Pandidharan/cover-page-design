from django.shortcuts import render

# Create your views here.
def bookcover(request):
    return render(request,"bookcover/book.html")
