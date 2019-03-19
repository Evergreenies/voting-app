from django.db import models
from django.core.validators import MaxValueValidator
import datetime
from . import parties

panels = parties.panels


class VoterDetail(models.Model):
    voter_id = models.CharField('Voter ID', primary_key=True, null=False, max_length=10)
    uidi = models.BigIntegerField('Aadhar Number ', unique=True, validators=[MaxValueValidator(9999999999999999)])
    voter_name = models.CharField('Voter Name', max_length=150, null=False)
    voted_to = models.CharField('Vote To', max_length=150, choices=panels, null=False)
    vote_time = models.DateTimeField(auto_now=datetime.datetime.now(), null=False)

    def __str__(self):
        return self.voter_name

    class Meta:
        db_table = 'PollsApp'


