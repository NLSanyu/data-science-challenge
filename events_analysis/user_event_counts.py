# Part 1 - Number of times each user triggered each event

import json
from input_data import INPUT_DATA as data


def count_events(dataset):
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

    with open("events_analysis/event_counts.json", "w") as outfile:  
        json.dump(event_count, outfile) 


if __name__ == "__main__":
    count_events(data)
    print("event_counts.json file created")