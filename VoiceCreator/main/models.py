from django.db import models
from django.db.models import aggregates

# Create your models here.
class Voice(models.Model):
    gender = models.CharField(verbose_name="성별", max_length=20)
    age_group = models.CharField(verbose_name="나이 그룹", max_length=20)
    preference = models.CharField(verbose_name="선호도", max_length=20)
    voice_code = models.CharField(max_length=20)
    audio_url = models.URLField(verbose_name="S3_URL")
    def __str__(self) -> str:
        return self.voice_code

class UserInput(models.Model):
    gender = models.CharField(verbose_name="성별", max_length=20)
    age_group = models.CharField(verbose_name="나이 그룹", max_length=20)
    breathiness = models.CharField(verbose_name="breathiness",max_length=20)
    smoothness = models.CharField(verbose_name="smoothness",max_length=20)
    hoarseness = models.CharField(verbose_name="hoarseness",max_length=20)
    variation = models.CharField(verbose_name="variation",max_length=20)
    url = models.TextField(verbose_name="URL_list")
    def __str__(self) -> str:
        return str(self.age_group + self.breathiness + self.smoothness + self.hoarseness + self.variation)
    def url_split(self):
        return self.url.split(',')