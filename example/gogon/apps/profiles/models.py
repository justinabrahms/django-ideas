from django.db import models
from django.utils.translation import ugettext_lazy as _

from idios.models import ProfileBase

MAX_POINTS = 10

class Profile(ProfileBase):
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True, verify_exists=False)
    max_points = models.PositiveIntegerField(default=MAX_POINTS)
    available_points= models.PositiveIntegerField(default=MAX_POINTS)

    def recalculate_points(self):
        # @@@ possibly should be on the IdeasUsers manager
        from ideas.models import IdeasUsers, OPEN
        count = IdeasUsers.objects.filter(
            user=self.user,
            idea__status=OPEN,
        ).aggregate(models.Sum('points')).get('points__sum', 0)
        if count != (self.max_points - self.available_points):
            self.available_points = self.max_points - count
            self.save()
