from django.shortcuts import render

# Create your views here. 

def trees(request):
    return render(request,'trees.html') 
def mountains(request):
    return render(request,'mountains.html')
