from countdowntimer_model.models import CountdownTimer
from django.db import models


class Poll(CountdownTimer):
    question = models.CharField(max_length=200)

    @property
    def seconds_remain(self):
        print(self.remaining_time().seconds % 60)
        return self.remaining_time().seconds % 60

    @property
    def minutes_remain(self):
        print(self.remaining_time().seconds // 60)
        return self.remaining_time().seconds // 60

    @property
    def is_time_expired(self):
        print(not self.remaining_time().seconds)
        return not self.remaining_time().seconds

    def __str__(self):
        return f'Poll(question={self.question}, duration={self.duration_in_minutes}, state={self.state})'


class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    votes = models.IntegerField(default=0, blank=True)

    def dict(self):
        return {'id': self.id, 'poll': self.poll, 'option': self.option, 'votes': self.votes}
