# I have created this file - ronit
from django import http
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalizeall = request.POST.get('capitalizeall', 'off')
    rmnewline = request.POST.get('rmnewline', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    purpose = ""

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"”“\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose = "Removed Punctuations"
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        djtext = analyzed

    if capitalizeall == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose = purpose + " | Capitalized"
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        djtext = analyzed

    if rmnewline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose = purpose + " | Removed new lines"
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        djtext = analyzed

    if removeextraspace == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        purpose = purpose + " | Removed extra spaces"
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        djtext = analyzed

    if(removepunc != "on" and removeextraspace != "on" and capitalizeall != "on" and rmnewline != "on"):
        return render(request, 'error.html')
    
    return render(request, 'analyze.html', params)