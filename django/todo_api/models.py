from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=1024, null=False, blank=False)
    status = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
    )
    due_date = models.DateTimeField(null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-created_at"]
