# Intention Journal

Quick daily script that creates a markdown file to journal in each day. It prompts you for things you are grateful for and your priorities for the day.

If you want a file to generate each day, you can set it up as a cronjob!

```bash
$ env EDITOR=nano crontab -e
```

Then in the editor:

```
50 8 * * * python ~/code/journal/script/morning.py
00 22 * * * python ~/code/journal/script/evening.py
```

The above command will run the morning script every day at 8:50 AM and the evening script at 11:00 PM if your folder is in the directory code with the folder name journal! You can edit this to be at a different time, to only run on week days, or at a different folder on your computer!

Right now, each day a file will generate in a "morning" folder in the project directory with the file named with the current date.
