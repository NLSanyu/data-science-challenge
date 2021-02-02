# Part 1 - Number of times each user triggered each event

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

    return event_count
