from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .numtoword import Words

def index(request):
    return render(request,"NumtoWordApp/index.html")

def convert(request):
    inpNum = request.POST['inputNumber']
    word = Words(int(inpNum))
    return JsonResponse({'word':word})