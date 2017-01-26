from django.db import models
from django.contrib.auth.models import User


# User profile model.

class UserProfile(models.Model):
	user = models.OneToOneField(User)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=0)[0])