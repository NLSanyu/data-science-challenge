# Part 1 - Number of times each user triggered each event
from input_data import INPUT_DATA

# Initial dataset
dataset = INPUT_DATA

# Final dataset that will contain counts of events per user
event_count = {}

for metric in dataset:
    user_id = str(metric["properties"]["user_id"])
    event = metric["event"]
    if user_id not in event_count.keys():
        event_count[user_id] = {}
        event_count[user_id][event] = 1
    else:
        if event not in event_count[user_id].keys():
            event_count[user_id][event] = 1
        else:
            event_count[user_id][event] += 1
