#!/usr/bin/env python
"""
This module checks SAS Viya services status
and send slack and sns notifications in case of one of the service is down
"""

import csv
import subprocess
import logging
import socket
import logging.config
from notifications.slack_notification import *
from notifications.sns_notification import *

def create_status_file():
    """
    Parse viya status file and save it in data frame
    """
    in_file_name = 'status_file.csv'
    cmd = 'sudo /etc/init.d/sas-viya-all-services status > status_file.csv'
    subprocess.call([cmd], shell=True)
    out_file_name = 'parsed_' + in_file_name
    logger.info(f' started modifying status_file {in_file_name}')
    try:
        with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
            csv_reader = csv.reader(in_file)
            csv_writer = csv.writer(out_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 1 and row != [] and len(row[0].split()) > 4:
                     #exclude summary from the status file
                    csv_writer.writerow(row[0].split()[0:2])
                    line_count += 1
                else:
                    line_count += 1
    except FileNotFoundError:
        logger.error(f'status file {in_file_name} is not found!', exc_info=True)
    return out_file_name


def viya_healthcheck():
    """
    Parse status file and check if any service is down
    In case of issue send notifications to slack and sns
    """
    status_file = create_status_file()
    slack_reponse, sns_response = 200, 200
    logger.info(f' got the status_file {status_file}')
    slack_alarm_name = socket.gethostname()
    logger.info(f'executing on the  {slack_alarm_name}')
    try:
        with open(status_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            failed_lst = []
            for line in csv_reader:
                if line[1] not in ('up', 'completed'):
                    failed_sas_service = line[0]
                    failed_lst.append(failed_sas_service)
            if len(failed_lst) >= 1:
                reason_txt = f'sas viya services :{failed_lst}  are down. Please check the logs'
                logger.info(f'Status check: {reason_txt}')
                slack_reponse = post_to_slack(alarm_name=slack_alarm_name, reason=reason_txt)
                sns_response = send_to_sns(reason_txt)
            else:
                logger.info('Everythin os OK')
    except FileNotFoundError:
        logger.error(f'status file {status_file} is not found!', exc_info=True)
    return [slack_reponse, sns_response]


if __name__ == "__main__":
    # configure loging
    log_file = 'logs/viya_monitoring.log'
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    f_handler = logging.FileHandler(log_file, 'a')
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('[%(asctime)s] %(module)s - %(levelname)s: %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    viya_healthcheck()
