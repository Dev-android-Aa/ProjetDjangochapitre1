from django.shortcuts import render
from .models import Page

# Create your views here.
def pages_lists(request):
    #pages = Page.objects.all()
    pages = Page.objects.all().order_by('date')
    return render(request,'pages/pages_lists.html',{'pages':pages})