from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyMemo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    memo = models.TextField(blank=True)
    favourite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
