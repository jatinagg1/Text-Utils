# I have created this file - Jatin
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''hello <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"><p>Django Playlist</a>''')
#
# def about(request):
#     return HttpResponse("about me")

def index(request):
    return render(request,'index.html')
    #return HttpResponse("HOME")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    elif(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount == 'on'):
        count = 0
        for index,char in enumerate(djtext):
            if (djtext[index] >= 'a' and djtext[index] <= 'z') or (djtext[index] >= 'A' and djtext[index] <= 'Z'):
                count = count + 1
        params = {'purpose': 'Count of Characters', 'analyzed_text': count}
        djtext = count

    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
            return HttpResponse("Error! Please select an option and try again!!")

    return render(request, 'analyze.html', params)