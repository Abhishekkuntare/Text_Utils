#I have created this file Abhishek

from calendar import c
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

# request is the argument to give the function 
def home(request):
    params = {'name' : 'Abhishek' , 'place' : 'Dubai'}
    return render(request, 'index.html',params)

def analyze(request):
    # this will be print your given text or default 

    # get the text 
    djtext = (request.POST.get('text', 'default'))

    removepunc  = (request.POST.get('removepun', 'off'))
    uppercase  = (request.POST.get('uppercase', 'off'))
    lowercase = (request.POST.get('lowercase','off'))
    newlineremove = (request.POST.get('newlineremove','off'))
    extraspaceremove = (request.POST.get('extraspaceremove','off'))
    charcount = (request.POST.get('charcount','off'))


    # punctuation
    if removepunc == "on":
        punctuation  = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        new_text = ""

        for char in djtext:
            if char not in punctuation:
                new_text = new_text+ char
    
    # sending the parameters to analze.html 
        params = {'purpose' : 'Remove Puntuations', 'analyzed_text' : new_text}
        djtext = new_text
    # final return to html page with analize the text 

    # UPPERCASE
    if( uppercase == "on"):
        new_text = ""
        for char in djtext:
            new_text = new_text + char.upper()
        
        params = {'purpose' : 'UPPERCASE',  'analyzed_text' : new_text }
        djtext = new_text

#lowercase
    if(lowercase == "on"):
        new_text =""
        for char in djtext:
            new_text = new_text + char.lower()

        params = {'purpose': 'lowercase', 'analyzed_text': new_text}
        djtext = new_text

#new_line
    if(newlineremove == "on"):
        new_text =""
        for char in djtext:
            if(char !="\n" and char!="\r"):
               new_text = new_text + char;
  
        params = {'purpose': 'New Line Remover', 'analyzed_text': new_text}
        djtext = new_text

# extra space 
    if(extraspaceremove == "on"):
        new_text =""
        for index,char in enumerate(djtext):
            if not(djtext[index] == "  " and djtext[index+1]=="  "):
                new_text = new_text  + char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': new_text}
        djtext = new_text

# char count 
    if(charcount == "on"):
     for i in djtext:
        count = len(djtext)

        params = {'purpose': 'Charcter Count', 'analyzed_text':  count }
        djtext = count

    if uppercase != "on" and lowercase != "on" and newlineremove != "on" and extraspaceremove != "on"and charcount != "on": 

        return render(request,'error.html')

    return render(request, 'analze.html',params)


    