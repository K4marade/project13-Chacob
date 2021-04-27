import sys
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from accounts.models import UserAuth
from mycalendar.models import Event
from datetime import datetime

import environ

from mypet.models import Pet

env = environ.Env()
environ.Env.read_env(env_file='chacob.settings')


class Email:

    def __init__(self):
        pass

    @staticmethod
    def send_mail_alert():

        # Get the current date in a string
        now = str(datetime.now()).split()[0]

        # Find today events from the current date
        today_events = Event.objects.filter(date__icontains=now, mail_alert=True)

        # If one or more events are found :
        if len(today_events) != 0:
            for event in today_events:
                user_email = UserAuth.objects.get(id=event.user_id_id).email
                pet_name = str(Pet.objects.get(name=event.pet_name))
                reason = event.reason
                send_mail("Rappel de rendez-vous vétérinaire",
                          "Bonjour,\n\nNous vous rappelons que vous avez rendez-vous aujourd'hui "
                          "pour " + pet_name + ".\n\nMotif : " + reason,
                          env("GMAIL_USER"),
                          [user_email])
        else:
            sys.stdout.write("No events this day")


class Command(BaseCommand):
    help = "Send an email to users to remind their appointments"

    def add_arguments(self, parser):
        parser.add_argument('send_email', type=str)

    def handle(self, *args, **options):
        if options['send_email']:
            email = Email()
            email.send_mail_alert()
