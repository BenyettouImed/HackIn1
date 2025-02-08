from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    hour = models.TimeField()
    organizer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='organized_events'
    )
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date', '-hour']
