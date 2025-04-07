import os
import json

def parse_event_file(filepath):
    games = []
    current_game = {
        "metadata": {},
        "events": []
    }

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            code = line[:3]

            if code == 'id,':  # New game
                if current_game["events"]:
                    games.append(current_game)
                    current_game = {
                        "metadata": {},
                        "events": []
                    }
                current_game["metadata"]["game_id"] = line.split(",")[1]
            elif code == 'info':
                _, key, value = line.split(",", 2)
                current_game["metadata"][key] = value
            elif code == 'start':
                if "starting_lineups" not in current_game:
                    current_game["starting_lineups"] = []
                current_game["starting_lineups"].append(line)
            elif code == 'play':
                current_game["events"].append(line)
            else:
                current_game["events"].append(line)

    if current_game["events"]:
        games.append(current_game)

    return games

def parse_all_event_files(base_folder, output_folder):
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.EVA') or file.endswith('.EVN'):
                input_path = os.path.join(root, file)
                try:
                    games = parse_event_file(input_path)
                    output_path = os.path.join(output_folder, f"{file}.json")
                    with open(output_path, 'w', encoding='utf-8') as out_file:
                        json.dump(games, out_file, indent=2)
                    print(f"✅ Parsed {file} → {output_path}")
                except Exception as e:
                    print(f"❌ Failed to parse {file}: {e}")

base_data_dir = "/Users/chloecrelia/Desktop/COSI 232 NLP/Final Project/Raw"
output_json_dir = "/Users/chloecrelia/Desktop/COSI 232 NLP/Final Project/JSON files"

os.makedirs(output_json_dir, exist_ok=True)

# Run 
parse_all_event_files(base_data_dir, output_json_dir)
