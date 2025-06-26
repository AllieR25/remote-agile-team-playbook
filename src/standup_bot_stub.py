# standup_bot_stub.py

"""
🕒 Async Standup Bot (Stub)

This script is a placeholder for an async standup bot that could post prompts 
to Slack or Teams and aggregate responses from distributed team members.
"""

def post_standup_prompt():
    print("🌤️ Good morning team! Please answer:")
    print("1. What did you work on yesterday?")
    print("2. What will you work on today?")
    print("3. Any blockers?")

def collect_responses():
    # Placeholder for collecting responses from a messaging platform
    return [
        {"name": "Alex", "response": "Worked on dashboard. Today: testing. No blockers."},
        {"name": "Jamie", "response": "Finished backlog grooming. Starting new story today."}
    ]

def display_summary():
    responses = collect_responses()
    print("\n📋 Standup Summary:")
    for r in responses:
        print(f"{r['name']}: {r['response']}")

if __name__ == "__main__":
    post_standup_prompt()
    display_summary()
