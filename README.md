# auto-learner

**To run:**
1. Install dependencies
```sh
pip install -r requirements.txt
```
2. Replace `HTML_FILE_NAME` in `.env.example` with your own `.html` file downloaded from [Google takeout](https://takeout.google.com)
3. Copy `.env.example` to `.env`
```sh
cp .env.example .env
```
5. Run in order: `create_searches.py` -> `create_clusters.py` -> `create_summaries.py`
6. `.txt` and `.png` are saved in `/data`
