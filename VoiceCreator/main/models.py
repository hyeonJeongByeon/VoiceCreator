from django.db import models

# Create your models here.
class Voice(models.Model):
    gender = models.CharField(verbose_name="성별", max_length=20)
    age_group = models.CharField(verbose_name="나이 그룹", max_length=20)
    preference = models.CharField(verbose_name="선호도", max_length=20)
    voice_code = models.CharField(max_length=20)
    audio_url = models.URLField(verbose_name="S3_URL")
    def __str__(self) -> str:
        return self.voice_code