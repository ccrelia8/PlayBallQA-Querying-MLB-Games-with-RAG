For the data preparation step of the project, I used the data of regular season MLB games from Retrosheet from 
the 1960s to 2020s. I stored all of the data in a folder called Raw then I wrote a python script called parse.py that converts
the raw files to JSON format and saves them into a folder called JSON files. 

Next I wanted to extract features from the data. I wrote a second python script called feature_extractor.py that extracts 
features such as inning number, batter ID, itch sequence, and runner advances from each play in the data. This data was 
saved into a new folder called Enriched_JSON.

Next steps include implementing RAG. One question that we will see about in the implementation and experimentation phase
is if the documents need to be in smaller chunks since they are still quite long right now. If so, the current python
scripts can be adjusted to break down the data into smaller parts so that RAG might have more success locating the answers
to queries.