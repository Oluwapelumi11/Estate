from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField("Name", max_length=50)
    email = models.CharField("Email", max_length=200)
    phone = models.IntegerField("Phone")
    image = models.ImageField("Image",upload_to="agents/")
    facebook = models.URLField("Facebook Profile Url", max_length=255)
    x = models.URLField("X Profile Url", max_length=255)
    whatsapp = models.CharField("Whatsapp Number", max_length=255)

    def __str__(self):
        return f"{self.name}"