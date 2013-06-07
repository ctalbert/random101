from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from random101.models import Meeting, Chat101


class Command(BaseCommand):
    help = """Imports past 101 from a csv file"""
    args = '<filename>'

    def handle(self, *args, **options):
        start_date = raw_input(
            "Give me a date for the past meeting:(YYYYMMDD):"
        )

        meeting, _ = Meeting.objects.get_or_create(
            start_date=datetime.strptime(start_date, "%Y%m%d"))

        # there's one couple per line
        lines = open(args[0]).read().splitlines()
        for line in lines:
            if line:
                chat = Chat101.objects.create(meeting=meeting)
                for participant in line.split(','):
                    user, _ = User.objects.get_or_create(
                        username=participant.strip().lower())
                    meeting.attendants.add(user)
                    chat.users.add(user)
