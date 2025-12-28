from django.contrib.auth.models import AbstractUser
from django_sqids import SqidsField

class User(AbstractUser):
    
    def __str__(self):
        return self.username

    sqid = SqidsField(real_field_name="id")