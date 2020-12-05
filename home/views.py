from django.shortcuts import render
from django.views import View
from home import models
class Index(View):
    def get(self,req):
        allBooks=models.Books.objects.all()
        return render(req,"index.html",{"books":allBooks})
# Create your views here.
