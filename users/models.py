from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    USERS_ROLES = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
    )
    email = models.EmailField(
        'электронная почта',
        max_length=250,
        unique=True,
    )
    first_name = models.CharField(
        'имя',
        max_length=150,
    )
    last_name = models.CharField(
        'фамилия',
        max_length=150,
    )
    role = models.CharField(
        'пользовательская роль',
        max_length=max(len(role) for role, none_ in USERS_ROLES),
        choices=USERS_ROLES,
        default=USER,
    )
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('id',)
        indexes = [
            models.Index(fields=['role', ], name='role_idx'),
        ]
