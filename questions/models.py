from django.db import models

class Question(models.Model):
    title = models.CharField(max_length = 120)
    question = models.TextField()
    answer = models.CharField(max_length = 120)
    date = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__(self):
        return self.title
