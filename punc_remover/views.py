from django.http import HttpResponse
from django.shortcuts import render
import string
result = string.punctuation


def index ( request ) :
    return render(request,'index.html')
def analyse(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    capatalise = request.GET.get('capatalise','off')
    newlineremover = request.GET.get('newlineremover', '9off')
    charactercount = request.GET.get('charactercount', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')


    if removepunc == 'on':
         analysed = ''
         for char in djtext:
             if char not in result:
                 analysed = analysed + char
         params={'analysed_text':analysed}
         djtext = analysed


    if capatalise == 'on':
        capatalised =''
        for char in djtext:
            capatalised = capatalised + char.upper()
        params = {'analysed_text': capatalised}
        djtext = capatalised


    if newlineremover == 'on':
        analysed=''
        for char in djtext:
            analysed = analysed+char
        params={'analysed_text':analysed}
        djtext = analysed


    if charactercount == 'on':
        char_count = len(djtext)
        params = {'char_count':char_count}
        djtext = char_count

    # if spaceremover == 'on':
    #     analysed=""
    #     for index, char in enumerate(djtext):
    #         if djtext[index] == " " and djtext[index+1] == " ":
    #             pass
    #         else:
    #             analysed = analysed + char
    #         params = { ' analysed_text ': analysed}


    #if(removepunc == "on" and newlineremover == 'on' and capatalise == 'on' and spaceremover == 'on' and charactercount == 'on'):
    return render(request,'analyse.html', params)






