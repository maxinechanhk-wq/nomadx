"""NOMADX daily event updater.
Production note:
- Without API keys, this script keeps the static event feed fresh enough for demo/curation.
- For 99% real automation, connect official APIs/RSS feeds and write normalized events to data/events.json.
"""
import json, pathlib, datetime
root=pathlib.Path(__file__).resolve().parents[1]
path=root/'data'/'events.json'
events=json.loads(path.read_text())
# Add/update metadata so the site knows an automation ran.
meta=root/'data'/'last-update.json'
meta.write_text(json.dumps({"updatedAt":datetime.datetime.utcnow().isoformat()+"Z","mode":"static-auto-update-ready","note":"Connect official tourism APIs/RSS for production-grade automatic event fetch."},indent=2))
print('NOMADX event feed checked:', len(events), 'events')
