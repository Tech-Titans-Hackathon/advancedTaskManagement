from django.db import models

# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
            "users.User",  # ✅ Lazy reference
            on_delete=models.CASCADE,
            related_name="owned_workspaces"
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class WorkspaceMember(models.Model):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="workspace_members")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.workspace.name} ({self.role})"