from django.shortcuts import render
from blog.models import category,Article

# Create your views here.

def home(request):
    categories= category.objects.all()
    articles = Article.objects.all()
    context = {'categories':categories,'articles':articles}
    return render(request,'index.html',context)