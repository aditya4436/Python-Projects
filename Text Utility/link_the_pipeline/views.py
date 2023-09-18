from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')

    #Check which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:,."\<>/?'|*&^%$#@!_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Removed Punctions', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Space', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(charactercount == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = len(djtext)
        params = {'purpose':'Number of Characters', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercount != "on"):
        return HttpResponse("Error")
    
    return render(request, 'analyze.html', params)