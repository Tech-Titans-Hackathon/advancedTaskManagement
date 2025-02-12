from django.db import models
# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    deadline = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="created_projects")

    def __str__(self):
        return self.name
class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('collaborator', 'Collaborator'),
        ('viewer', 'Viewer'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="project_members")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='collaborator')

    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.role})"