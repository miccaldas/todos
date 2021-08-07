#  Module to write a todo and create an associated cron job

from crontab import CronTab
import click


def todo():

    texto = input(click.style(' What is yout to-do? » ', fg='green', bold=True))

    cron = CronTab('mic')
    job = cron.new(command='/usr/bin/dunstify "' + texto + '"')
    job.minute.every(59)
    cron.write()


todo()
