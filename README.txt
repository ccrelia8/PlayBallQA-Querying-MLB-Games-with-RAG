# PlayBallQA: Querying MLB Games with RAG
**PlayBallQA** is a work-in-progress project that aims to answer natural language questions about Major League Baseball (MLB) games using structured play-by-play data and a Retrieval-Augmented Generation (RAG) framework.

## ⚾ Data Source

This project uses publicly available MLB regular season data from **[Retrosheet](https://www.retrosheet.org/)**, covering games from the 1960s to 2020s. The data is distributed in structured text formats containing every play-by-play event from each game.

📎 *To access the full dataset:*
- Visit: [https://www.retrosheet.org/game.htm](https://www.retrosheet.org/game.htm)
- Download files for your seasons of interest
- Use the included `parse.py` script to convert raw files into JSON format

> The full dataset is not included in this repository due to its size. Only example outputs and scripts are provided.

---

## Current Progress

1. **Data Parsing**  
   A script `parse.py` converts raw Retrosheet event files into structured JSON files.

2. **Feature Extraction**  
   A second script `feature_extractor.py` enriches the parsed data by extracting useful features such as:
   - Inning number
   - Batter and pitcher IDs
   - Pitch sequences
   - Runner movements

   These enriched records are stored in the `Enriched_JSON/` directory.

---

## Next Steps

The next phase of this project involves implementing a **Retrieval-Augmented Generation (RAG)** pipeline. The idea is to allow users to ask questions like:

> “What happened in the 5th inning of the Red Sox game on August 13, 2022?”  
> “How many home runs did Mike Trout hit in 2023?”

### Planned Tasks:
- Preprocess and structure play-by-play records
- Experiment with chunking the documents into smaller units (e.g., by inning, by player)
- Index documents using FAISS for dense retrieval
- Integrate with a large language model (e.g., GPT or LLaMA)
- Build a demo to visualize results and model behavior
- Evaluate model performance and response accuracy


