from django.db import models
from django.contrib.auth.models import User
from random import shuffle


class Meeting(models.Model):
    start_date = models.DateField()
    attendants = models.ManyToManyField(User, related_name='meetings_attended')

    def generate_101(self):

        attendants = self.attendants.all()
        # we don't want to generate chats for less than 5 people
        assert attendants.count() >= 5

        # all past chats were 101, so this is a set of couples
        past_chats = set(
            tuple(chat.users.all())
            for chat in Chat101.objects.all().prefetch_related('users')
        )

        attendants_list = list(attendants)
        num_retries = 0

        # if we cannot find a set of couples in 10000 retries
        # we must be very unlucky (or there's a bug)
        while num_retries < 10000:
            num_retries += 1

            # shuffle the list of participants
            shuffle(attendants_list)

            # split the participants into couples
            selection = set(zip(*[iter(attendants_list)] * 2))

            # if there's no conflict with past chats
            if not selection.intersection(past_chats):
                return selection

        # if the num of retries is over a fixed limit, raise an exception
        raise Exception("This is taking longer than expected...")

    def __unicode__(self):
        return u'{0}'.format(self.start_date)


class Chat101(models.Model):
    meeting = models.ForeignKey(Meeting, related_name='chats')
    users = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return u'{0}|{1}'.format(self.meeting, self.users.all())
