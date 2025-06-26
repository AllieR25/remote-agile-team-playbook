# standup-bot-template.py

"""
A template for a daily standup bot that prompts team members and logs responses.
Can be integrated with Slack via a webhook or bot framework.
"""

from datetime import datetime

TEAM = [
    {"name": "Allie", "slack": "@allie"},
    {"name": "Chris", "slack": "@chris"},
    {"name": "Maya", "slack": "@maya"},
    {"name": "Luis", "slack": "@luis"},
    {"name": "Anika", "slack": "@anika"}
]

def send_standup_prompt(team):
    for member in team:
        print(f"Prompt sent to {member['slack']}: What did you work on yesterday? Plans for today? Any blockers?")

def log_response(name, response):
    with open("standup_log.txt", "a") as log:
        log.write(f"{datetime.now().isoformat()} - {name}: {response}\n")

if __name__ == "__main__":
    send_standup_prompt(TEAM)
