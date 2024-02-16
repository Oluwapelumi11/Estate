from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField("Name", max_length=50)
    email = models.CharField("Email", max_length=200)
    phone = models.CharField("Phone",max_length=50, null=True, blank=True)
    image = models.ImageField("Image",upload_to="agents/", null=True, blank=True)
    facebook = models.URLField("Facebook Profile Url", max_length=255, null=True, blank=True)
    x = models.URLField("X Profile Url", max_length=255, null=True, blank=True)
    whatsapp = models.CharField("Whatsapp Number", max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"