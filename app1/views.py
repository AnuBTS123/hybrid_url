from django.shortcuts import render

# Create your views here.
def jk(request):
    return render(request,'jk.html')

def BTS(request):
    return render(request,'BTS.html')