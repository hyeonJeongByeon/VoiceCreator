from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Voice
import os
import csv

# Create your views here.
def page_renderer(request):
    return render(request,"voice_search.html")

def voice_save(request):
    csv_path = os.path.dirname(os.path.abspath(__file__))
    f = open(csv_path+"/voice.csv",'r')
    reader = csv.reader(f)
    count = 0
    for line in reader:
        gender = line[0]
        age_group = line[1]
        preferences = line[2]
        voice_code = line[3]
        url = line[4]
        new_voice = Voice(gender=gender,age_group=age_group,preference=preferences,voice_code=voice_code, audio_url=url)
        new_voice.save()
        count += 1
    return render(request,"success.html",{"msg":f"{count}개의 Voice를 저장하였습니다"})

def voice_search(request,gender,voice_code):
    voice_list = Voice.objects.filter(gender=gender,voice_code=voice_code)
    url_list =[]
    for voice in voice_list:
        preference = voice.preference
        if preference in ['5','4','3','2','1']:
            url = voice.audio_url
            url_list.append(url)
    url_list = list(set(url_list))
    if request.method == "POST":
        gender = request.POST.get('gender')    
    
    return JsonResponse({"url_list":url_list})