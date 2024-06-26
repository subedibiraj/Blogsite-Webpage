from django.shortcuts import render
from blog.models import category

# Create your views here.

def home(request):
    categories= category.objects.all()
    context = {'categories':categories}
    return render(request,'index.html',context)