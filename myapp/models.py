from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('TO DO', 'TO DO'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('ON HOLD', 'ON HOLD'),
        ('TESTING', 'TESTING'),
        ('DEPLOYMENT', 'DEPLOYMENT'),
        ('DONE', 'DONE'), 
        ('MAINTENANCE', 'MAINTENANCE'),
    ] 

    project = models.ForeignKey(Project, related_name='tickets', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='TO DO'
    )
    assigned_to = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
