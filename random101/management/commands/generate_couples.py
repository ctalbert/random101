from datetime import date

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from random101.models import Meeting, Chat101


class Command(BaseCommand):
    help = """Generates random couples from a given list of participants.
The only argument is a filename containing  a list names, one per line."""
    args = '<filename>'

    def handle(self, *args, **options):
        meeting, _ = Meeting.objects.get_or_create(start_date=date.today())

        names = open(args[0]).read().splitlines()
        names = map(lambda x: x.strip().lower(), names)
        for name in names:
            user, _ = User.objects.get_or_create(username=name)
            meeting.attendants.add(user)

        couples = meeting.generate_101()

        print "Couples generated:"
        for couple in couples:
            print "{0} -> {1}".format(*[c.username for c in couple])

        save_it = raw_input("""do you wanna save these couples?[yes/no](no)""")

        if save_it == "yes":
            for couple in couples:
                chat = Chat101.objects.create(meeting=meeting)
                for participant in couple:
                    chat.users.add(participant)
