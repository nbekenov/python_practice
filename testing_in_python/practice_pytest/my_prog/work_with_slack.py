import requests
import json
import os


def post_to_slack(alarm_name, reason, config):
    """ Send message text to slack channel
        INPUTS:
        * alarm_name - subject of the message
        * reason - message text
    """
    # get params from config file
    proxy_server = config['proxy_server']
    if proxy_server !='':
        os.environ['HTTP_PROXY'] = proxy_server
        os.environ['HTTPS_PROXY'] = proxy_server
    slack_webhook_url = config['slack_webhook_url']

    slack_message = build_pr_message(alarm_name,reason)
    data={"text":slack_message['text'], "attachments" : slack_message['attachments'] }
    reponse=requests.post(slack_webhook_url, json=data)
    return reponse.text


def build_pr_message(headline_txt,reason_txt):
    message_dict = {}
    message_dict['text'] = "`"+headline_txt+"`"
    message_dict['attachments'] = build_pr_attachment(reason_txt)
    return message_dict

def build_pr_attachment(reason_txt):
    attachment_dict = {}

    attachment_dict['title'] = "Reason"
    attachment_dict['color'] = 'danger'

    # This setting allows us to use markdown in text (to bold, italicize, etc.)
    attachment_dict['mrkdwn_in'] = ['text']
    attachment_dict["text"] = reason_txt

    # Since attachment is in a JSON-formatted list, I'll create a list here to return
    attachment_list = [attachment_dict]
    return attachment_list
