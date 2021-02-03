## Analysis of the PhotoUpload event

### Analysis process
The `PhotoUpload` event is one of four that users trigger at GuideBook, which are `GuideSession`, `GuideDownload`, `ConnectionRequest` and `PhotoUpload`.

The analysis was done in two parts:
1. Part 1: 
A script (`user_event_counts.py`) to keep track of how many times each user uses each event. This script created a json file (`event_counts.json`). In this file, each user id is a key and the corresponding value is a dictionary of events and how many times they were used by that user.

2. Part 2:
A Jupyter Notebook (`photo_upload_analysis.ipynb`) containing the analysis for the `PhotoUpload` event.


### Findings
The `PhotoUpload` event is not frequently triggered by users in this dataset.
<br/> 
More than 75% of users having not triggered it, as shown in the histogram below:
<img src="plots/photo_upload_hist.png">

The average number of times a user has triggered it is 2, while the highest number of times it has been triggered by one user is 24.
<br/> 
These numbers, compared to the `GuideSession` event (more then 49000 triggers), are very low.
<br/> 
However, when put in context with the other two event types (`GuideDownload` and `ConnectionRequest`), it is evident that `PhotoUpload` has been triggered more than them and is in fact the second most triggered event after `GuideSession`.
<br/> 
<img src="plots/events_comparison.png">
