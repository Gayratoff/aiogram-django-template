from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TelegramUser(models.Model):
    full_name = models.CharField(
        max_length=200,
        verbose_name='full_name'
    )
    user_id = models.BigIntegerField(
        unique=True,
        validators=[MinValueValidator(0)],
        verbose_name='user_id'
    )

    def __str__(self):
        return str(self.user_id)

    def get_user(self):
        try:
            return User.objects.get(telegramusers=self)
        except User.DoesNotExist:
            return None

    def set_user(self, user):
        self.user = user
        self.save()
