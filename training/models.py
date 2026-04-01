from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.lesson}"