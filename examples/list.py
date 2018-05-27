#!/usr/bin/env python
"""List items in slack."""

# https://github.com/os/slacker
# https://api.slack.com/methods
# https://metacorp-space.slack.com

import os
from slacker import Slacker


def list_slack():
    """List channels & users in slack."""
    try:
        token = "xoxp-XXXXXXXXXXXXXXXX"
        slack = Slacker(token)

        # Get channel list
        response = slack.channels.list()
        channels = response.body['channels']
        for channel in channels:
            print(channel['id'], channel['name'])
            # if not channel['is_archived']:
            # slack.channels.join(channel['name'])
        print()

        # Get users list
        response = slack.users.list()
        users = response.body['members']
        for user in users:
            if not user['deleted']:
                print(user['id'], user['name'], user['is_admin'], user[
                    'is_owner'])
        print()
    except KeyError as ex:
        print('Environment variable %s not set.' % str(ex))


if __name__ == '__main__':
    list_slack()
