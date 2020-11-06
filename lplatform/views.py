from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("Hello  World !")

def runoob(request):
    # name_list = ['mike','admin','noob']
    name_list=[]
    return render(request,'runoob.html',{"name":name_list})