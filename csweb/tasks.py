from csweb.celery import app
from django_slack import slack_message

@app.task
def slack_msg(msg):
    # task: send slack message
    slack_message('meal_msg.slack',attachments = [{'text': msg,},])