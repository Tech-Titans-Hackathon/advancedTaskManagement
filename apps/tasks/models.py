from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("critical", "Critical"),
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    deadline = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name="tasks")

    # Attachments using ImageKit
    attachment = ProcessedImageField(
        upload_to="task_attachments/",
        processors=[ResizeToFit(800, 800)],
        format="WebP",
        options={"quality": 90},
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.project.name}"


class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="assignments")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="task_assignments")
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.task.name}"