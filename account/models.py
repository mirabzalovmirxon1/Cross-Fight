from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Account(AbstractUser):
    """
    Asosiy foydalanuvchi modeli. 
    Student, Trainer, Admin rolini belgilash mumkin.
    """
    ROLES = (
        ('student', 'Student'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='student')

    # Related names to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='account_groups',
        blank=True,
        help_text='Groups for Account'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_permissions',
        blank=True,
        help_text='Permissions for Account'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"