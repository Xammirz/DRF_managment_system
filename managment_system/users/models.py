from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from managment_system.tasks.models import Task

class User(AbstractUser):
    """
    Default custom user model for managment_system.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField("Имя",max_length=100,null=True,blank=True)
    last_name = models.CharField("Фамилия",max_length=100,null=True,blank=True)
    age = models.PositiveSmallIntegerField("Возраст", null=True, blank=True)
    email = models.EmailField("Емайл")
    

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
