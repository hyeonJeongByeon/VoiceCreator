from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from .models import Voice, UserInput
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

def situation_search():
    situation_list =['당신은 명절을 맞아 멀리 떨어져 지내는 가족/친구와 오랜만에 안부인사와 근황을 전하려고 합니다. 앞서 설명한 플랫폼을 통해 맞춤형 목소리를 제작하여 원하는 목소리로 통화를 할 수 있다면 당신은 어떤 목소리로 소통하고 싶으십니까?','당신은 한 학기동안 실시간 온라인 수업에 학생으로 참여하려고 합니다. 수업은 매번 질의응답, 발표 및 토론이 활발히 진행되고, 교수자(예: 교수, 교사, 강사) 외 수업을 함께 듣는 다른 학생들과는 이미 서로 얼굴을 알고 있다고 가정합시다. 앞서 설명한 플랫폼을 통해 맞춤형 목소리를 제작하여 원하는 목소리로 수업에 참여를 할 수 있다면 당신은 어떤 목소리로 소통하고 싶으십니까?','당신은 다른 유저와 협력하며 즐기는 게임(예: 오버워치, 배틀그라운드)에서 같은 팀 내 다른 멤버들과 소통하려고 합니다. 이 때, 키보드로 입력하고 화면의 글을 읽어야하는 채팅 대신 보이스톡 기능을 활용하여 참여하기로 합니다. 앞서 설명한 플랫폼을 통해 맞춤형 목소리를 제작하여 원하는 목소리로 게임에 참여를 할 수 있다면 당신은 어떤 목소리로 소통하고 싶으십니까?','당신이 배송받은 물품이 파손된 상태로 도착하여 해당 물품 생산 업체 콜센터 상담원에게 문의하려고 합니다. 앞서 설명한 플랫폼을 통해 맞춤형 목소리를 제작하여 원하는 목소리로 민원상담을 할 수 있다면 당신은 어떤 목소리로 소통하고 싶으십니까?','당신은 당신이 잘 아는 분야에 대한 정보전달용 유튜브 콘텐츠(예: 다큐멘터리)를 제작하려고 합니다. 따라서 당신은 영상 클립, 자막, 목소리를 넣어 영상을 구성하려고 하고 이 영상은 유튜브를 사용하는 불특정 다수에게 보여질 수 있습니다. 앞서 설명한 플랫폼을 통해 맞춤형 목소리를 제작하여 원하는 목소리로 영상을 만들 수 있다면 당신은 어떤 목소리로 소통하고 싶으십니까?']

def voice_search(request,gender,voice_code):
    voice_list = Voice.objects.filter(gender=gender,voice_code=voice_code)
    url_list =[]
    for voice in voice_list:
        preference = voice.preference
        if preference in ['5','4','3','2','1']:
            url = voice.audio_url
            url_list.append(url)
    url_list = list(set(url_list)) 
    return JsonResponse({"url_list":url_list})

def save_user_input(request):
    if request.method == "POST":
        test_id = request.POST.get('test_id')
        situation = request.POST.get('situation')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        breathiness = request.POST.get('breathiness')
        smoothness = request.POST.get('smoothness')
        hoarseness = request.POST.get('hoarseness')
        variation = request.POST.get('variation')
        url_list = request.POST.getlist('checkbox[]')
        url_text = ''
        for url in url_list:
            url_text += (url+',')
        new_input = UserInput()
        new_input.test_id = test_id
        new_input.situation = situation
        new_input.gender = gender
        new_input.age_group = age
        new_input.breathiness = breathiness
        new_input.smoothness = smoothness
        new_input.hoarseness = hoarseness
        new_input.variation = variation
        new_input.url = url_text
        new_input.save()
        return redirect("page_renderer")
    return redirect("page_renderer")

def user_input_list(request):
    user_inputs = UserInput.objects.all()
    return render(request, "survey_result.html",{"survey_result":user_inputs})
