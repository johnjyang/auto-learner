# auto-learner

**To run:**
1. Install dependencies
```sh
pip install -r requirements.txt
```
2. Copy `.env.example` to `.env`
```sh
cp .env.example .env
```
3. Replace `HTML_FILE_NAME` in `.env` with your own `.html` file downloaded from [Google takeout](https://takeout.google.com)
4. Specify number of available GPUs for PyTorch in `.env`. Default is set to 0.
5. Run `main.py`
