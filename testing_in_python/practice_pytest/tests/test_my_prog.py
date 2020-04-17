#!/usr/bin/python
# -*- coding: utf-8 -*-
import my_prog.work_with_slack as slackapi
import pytest

def test_post_to_slack(slack_params):
    test_config = slack_params
    assert slackapi.post_to_slack('PyTest msg','please dismiss', test_config) == 'ok'
