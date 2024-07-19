from django.db import models
from django.urls import reverse


# Create your models here.
class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    profile_summary = models.TextField()
    education = models.TextField(blank=True)
    skills = models.TextField()
    work_experience = models.TextField(blank=True)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('ResumePage:detail', kwargs={'pk': self.pk})
