from django.urls import path
from . import views

urlpatterns = [
    path('',views.pages_lists,name="pages"),
    path('<slug:slug>',views.pages_page,name="page"),
]