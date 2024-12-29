from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    # description null=True, blank=True
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    


# signal
# moghe e ke User e sakhte shavad ba estefade az code paeein be soorat khodkar profile on User sakhte mishavad
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) 
    