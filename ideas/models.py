import datetime
from django.db import models

OPEN = 0
CLOSED = 1
STATUS_CHOICES = (
    (OPEN, "Open"),
    (CLOSED, "Closed"),
)


class IdeaActiveManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        return super(IdeaActiveManager, self).get_query_set(*args, **kwargs)


class Idea(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=OPEN)
    submitted_by = models.ForeignKey("auth.User")
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    objects = models.Manager()
    active = IdeaActiveManager()

    def __unicode__(self):
        return "Idea: %s" % (self.name)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        if not self.id:
            self.date_added = now
        self.date_modified = now
        return super(Idea, self).save(*args, **kwargs)


class IdeasUsers(models.Model):
    idea = models.ForeignKey("Idea")
    user = models.ForeignKey("auth.User")
    points = models.IntegerField()

    def __unicode__(self):
        return "User %s -> Idea %s" % (self.user, self.idea)
