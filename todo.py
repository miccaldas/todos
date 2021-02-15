#  Module to write a todo and create an associated cron job

from crontab import CronTab
import click


def todo():

    texto = input(click.style(' What is yout to-do? » ', fg='green', bold=True))

    cron = CronTab(user='mic')
    job = cron.new(command='export DISPLAY=:0.0 && XDG_RUNTIME_DIR=/run/user/$(id -u) /usr/bin/notify-send "' + texto + '"')
    job.minute.every(59)
    cron.write()


todo()
