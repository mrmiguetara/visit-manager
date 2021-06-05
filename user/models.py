from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import base
from django.utils.translation import gettext_lazy as _
from clubs.models import Club
# Create your models here.

class User(AbstractUser):
    class Types(models.TextChoices):
        MEMBER = 'MEMBER', 'Member'
        ADMIN = 'ADMIN', 'Admin'
        OWNER = 'OWNER', 'Owner'
        GUARD = 'GUARD', 'Guard'
    
    base_type = Types.MEMBER

    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    name = models.CharField(_("Name of user"), blank=True, max_length=255)

    club = models.ForeignKey(Club, on_delete=models.SET_NULL,null=True, related_name='users')
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class MemberManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.MEMBER)

class Member(User):
    objects = MemberManager()
    class Meta:
        proxy = True



class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)

class Admin(User):

    objects = AdminManager()

    def invite_member(self):
        pass 
    
    def uninvite_member(self):
        pass 
    
    class Meta:
        proxy = True


class OwnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.OWNER)


class Owner(User):
    objects = OwnerManager()
    class Meta:
        proxy = True



class GuardManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.GUARD)

class Guard(User):
    objects = GuardManager()
    class Meta:
        proxy = True