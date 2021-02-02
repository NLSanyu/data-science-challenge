# Part 2 - Analyzing the PhotoUpload event

import pandas as pd
import seaborn as sns

from user_event_counts import count_events
from input_data import INPUT_DATA

def analyze_photoupload():
    event_counts = count_events(INPUT_DATA)
    events_df = pd.json_normalize(event_counts)
    # print(event_counts)

