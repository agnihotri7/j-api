import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group, Permission


class Project(models.Model):
    """
    """
    name = models.CharField(max_length=60)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='projects')
    members = models.ManyToManyField(User, related_name='project', null=True, blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)
    # progress = models.PositiveSmallIntegerField(max_length=3)

    class Meta:
        db_table = 'project1'
        permissions = (("create_project", "Can create Project"),)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    """
    name = models.CharField(max_length=60)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='all_tasks')
    created_by = models.ForeignKey(User, related_name='tasks_created')
    members = models.ManyToManyField(User, related_name='tasks', null=True, blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)
    progress = models.PositiveSmallIntegerField(max_length=3)

    class Meta:
        db_table = 'task1'
        permissions = (("create_task", "Can create Task"),)

    def __str__(self):
        return self.name
