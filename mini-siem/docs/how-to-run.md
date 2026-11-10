# How to run Mini SIEM

1. Install Python 3.10 or newer.
2. Clone the repo and open a terminal in the project folder.
3. Create and activate a virtual environment:
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Start the app: `python app.py`
6. Open http://127.0.0.1:5000 in a browser.
7. Paste the content of `sample_logs.txt` into the form and click **Analyze**.
   You should see one alert for `192.0.2.10` (5 failed logins).

The database file `siem.db` is created on first start. It is ignored by Git, so delete it to start fresh.

Run the tests: `python -m pytest`

## Common problems

- `ModuleNotFoundError: flask`: the virtual environment is not active, or step 4 was skipped.
- `Address already in use`: another program uses port 5000. Stop it or change the port in `app.py`.
