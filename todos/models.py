from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    # when we call __str__() we will
    # get a text (string) with a title
    def __str__(self):
        return self.title