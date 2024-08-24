# I Have Created This File - BRP
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get The Text
    global l
    dj_text = request.POST.get('text', 'Default')

    # Check Checkbox Values
    remove_punc = request.POST.get('remove_punc', 'off')
    full_cap = request.POST.get('full_caps', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')
    char_count = request.POST.get('char_count', 'off')
    # Check with checkbox is on
    if remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        dj_text = analyzed

    if full_cap == 'on':
        analyzed = ""
        for char in dj_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        dj_text = analyzed

    if new_line_remover == 'on':
        analyzed = " "
        for char in dj_text:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        dj_text = analyzed

    if extra_space_remover == 'on':
        analyzed = " "
        for index, char in enumerate(dj_text):
            if not (dj_text[index] == " " and dj_text[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        dj_text = analyzed

    if char_count == 'on':
        l = len(dj_text)
        params = {'purpose': 'Character Counter', 'analyzed_text': f"Total Characters are : {l},{analyzed}"}
    if remove_punc != 'on' and full_cap != 'on' and new_line_remover != 'on' and extra_space_remover != 'on' and char_count != 'on':
        return render(request, "error.html")
    return render(request, 'analyze.html', params)
