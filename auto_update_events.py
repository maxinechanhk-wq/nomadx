name: NOMADX Daily Update
on:
  schedule:
    # 08:00 UTC = 12am Vancouver standard time; use 07:00 UTC during daylight saving if exact midnight is required.
    - cron: '0 8 * * *'
  workflow_dispatch:
permissions:
  contents: write
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python scripts/auto_update_events.py
      - name: Commit updates
        run: |
          git config user.name "nomadx-bot"
          git config user.email "nomadx-bot@example.com"
          git add data/*.json
          git commit -m "daily auto update" || echo "No changes"
          git push
