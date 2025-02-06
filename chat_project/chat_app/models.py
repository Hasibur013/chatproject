from django.db import models

class ChatMessage(models.Model):
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    audio = models.FileField(upload_to="audio/", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} - {self.timestamp}"
