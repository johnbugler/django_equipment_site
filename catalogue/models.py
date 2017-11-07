from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    """
    Model representing a device
    """
    equipment = models.CharField(max_length=200, help_text="Type of equipment, make, model, etc.")
    description = models.TextField(max_length=1000, help_text="A brief description of equipment.")
    location = models.CharField(max_length=200, help_text="Lab/university address")
    email = models.EmailField(max_length=100, help_text="Email address")

 #   researcher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#    creation_date = models.DateTimeField(auto_now_add = True, editable=False)
#
#    class Meta:
#        ordering = ["-creation_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.equipment