from django.db import models
from account.models import Account

class Group(models.Model):
    """
    Trainerlar guruh yaratadi, o'quvchilar shu guruhga qo'shiladi.
    """
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='groups_as_trainer'
    )

    def __str__(self):
        return f"{self.name} ({self.trainer.username})"

class Assignment(models.Model):
    """
    Har bir o'quvchi uchun mashq/vazifa
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    total_tasks = models.PositiveIntegerField(default=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='assignments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.group.name})"

class Submission(models.Model):
    """
    O'quvchi topshiriqni videoga olib yuboradi
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='submissions')
    video_url = models.FileField()  # yoki FileField / Media
    is_approved = models.BooleanField(default=False)
    points = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title} ({'Approved' if self.is_approved else 'Pending'})"