from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(
        ContentType, null=True, blank=True, related_name='target_obj')
    target_id = models.PositiveIntegerField(
        null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']
