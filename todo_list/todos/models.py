from django.db import models

# Create your models here.
class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
