from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title + " by " + self.author
