from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_date = models.DateTimeField(default=timezone.now)
    choices = ((True, 'Boast'), (False, 'Roast'))
    roast_or_boast = models.BooleanField(choices=choices, default=True)
        
    @property
    def votes(self):
        return self.up_votes + self.down_votes
