import os
import json

input_folder = "/Users/chloecrelia/Desktop/COSI 232 NLP/Final Project/JSON files"
output_folder = "/Users/chloecrelia/Desktop/COSI 232 NLP/Final Project/Enriched_JSON"

# output folder
os.makedirs(output_folder, exist_ok=True)

def enrich_play_event(event_line):
    """
    Parse a 'play' event line and extract structured features.
    Format: play,inning,batting_team,batter_id,pitch_count,pitches,event_description
    Example: play,5,1,ramir001,00,,S8.3-H;1-2
    """
    parts = event_line.strip().split(",")
    if len(parts) < 7:
        return None  # skip bad lines

    try:
        inning = int(parts[1])
        batting_team = int(parts[2])
        batter_id = parts[3]
        pitch_count = parts[4]
        pitches = parts[5]
        event_desc = parts[6]

        # split primary event + runner advances
        if '.' in event_desc:
            event_code, *runner_parts = event_desc.split('.')
        else:
            event_code = event_desc
            runner_parts = []

        return {
            "inning": inning,
            "batting_team": batting_team,
            "batter_id": batter_id,
            "pitch_count": pitch_count,
            "pitches": pitches,
            "event": event_desc,
            "event_code": event_code,
            "runner_advances": runner_parts
        }
    except Exception as e:
        return None

def enrich_json_file(filepath, output_path):
    with open(filepath, "r") as f:
        data = json.load(f)

    for record in data:
        if record.get("record_type") == "play":
            enriched_fields = enrich_play_event(record["raw"])
            if enriched_fields:
                record.update(enriched_fields)

    with open(output_path, "w") as out_f:
        json.dump(data, out_f, indent=2)

# processing files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        in_path = os.path.join(input_folder, filename)
        out_path = os.path.join(output_folder, filename)
        enrich_json_file(in_path, out_path)

print("✅ Feature extraction complete.")
