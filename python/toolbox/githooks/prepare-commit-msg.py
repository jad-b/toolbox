#!/usr/bin/env python3
# vim: set ft=python
import os
import sys

# Third-party requirement
import git

repo = git.Repo(search_parent_directories=True)
githooks = os.path.join(repo.git_dir, 'hooks')
# Save the last ticket used in your githooks directory
last_ticket_file = os.path.join(githooks, '.jira')
tmp_commit_file = sys.argv[1]


ticket = None
try:  # Read in last ticket number
    with open(last_ticket_file) as f:
        ticket = f.read()
except:
    print('No ticket number stored')

# Open stdin for input - usually Git hooks are non-interactive
with open("/dev/tty", "r") as tty:
    sys.stdin = tty
    if not ticket:  # Get ticket number user
        ticket = input("Please enter the JIRA ticket: ")
    if ticket:  # Confirm ticket number
        answer = input("Hit Enter to confirm {}, or provide new ticket: "
                       .format(ticket)).strip()
        if answer:  # Overwrite with user's input
            ticket = answer

    # Prompt user for time
    time = input("How much time did you spend? ").strip()
    timelog = "{tkt} #time {time}".format(tkt=ticket, time=time)

with open(tmp_commit_file, 'a') as f:
    f.write('\n' + timelog)

with open(last_ticket_file, 'w') as f:
    f.write(ticket)
