from django.db import models
from accounts.models import User

class Squad(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='squad_created_by')
    updated_at = models.DateTimeField()
    updated_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='squad_updated_by')
    
    def __str__(self):
        return self.name

class Home(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    squad = models.ForeignKey(
        Squad,
        on_delete=models.CASCADE,
        related_name='home'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='home_created_by')
    updated_at = models.DateTimeField()
    updated_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='home_updated_by')

    def __str__(self):
        return self.name


class Member(models.Model):
    home = models.ForeignKey(
        Home,
        on_delete=models.CASCADE,
        related_name='members'
    )
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15, blank=True)
    is_head = models.BooleanField(default=False)
    joined_at = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='member_created_by')
    updated_at = models.DateTimeField()
    updated_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='member_updated_by')

    def __str__(self):
        return self.full_name
