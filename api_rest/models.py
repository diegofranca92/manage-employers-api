from django.db import models

# Create your models here.

class User(models.Model):
  user_nickname = models.CharField(max_length=100, primary_key=True, default='')
  user_name = models.CharField(max_length=150, default='')
  user_email = models.EmailField(default='')

  def __str__(self) -> str:
    return f'Nickname: {self.user_nickname} | Email: {self.user_email}'