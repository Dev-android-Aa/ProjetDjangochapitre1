from django.shortcuts import render

# Create your views here.
def pages_lists(request):
    return render(request,'pages/pages_lists.html')