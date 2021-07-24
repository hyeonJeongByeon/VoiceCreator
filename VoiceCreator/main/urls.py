from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.page_renderer,name="page_renderer"),
    path("voice_save/",views.voice_save,name="voice_save"),
    path("voice_search/<str:gender>/<str:voice_code>/", views.voice_search,name='voice_search'),
]