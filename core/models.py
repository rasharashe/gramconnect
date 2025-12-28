from django.db import models
from django_sqids import SqidsField
from accounts.models import User

class Squad(models.Model):
    sqid = SqidsField(real_field_name="id")
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='squad_created_by')
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='squad_updated_by', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Home(models.Model):
    sqid = SqidsField(real_field_name="id")
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, null=True, blank=True)
    squad = models.ForeignKey(
        Squad,
        on_delete=models.CASCADE,
        related_name='home'
    )
    number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='home_created_by')
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='home_updated_by', null=True, blank=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )

    sqid = SqidsField(real_field_name="id")
    home = models.ForeignKey(
        Home,
        on_delete=models.CASCADE,
        related_name='members'
    )
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_head = models.BooleanField(default=False)
    guardian_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    sec_id = models.CharField(max_length=50, blank=True)
    booth = models.SmallIntegerField(default=1)
    punchayath_sl_no = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='member_created_by')
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='member_updated_by',
            null=True, blank=True)

    def __str__(self):
        return self.full_name
