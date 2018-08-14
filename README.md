# Intention Journal

Quick daily script that creates a markdown file to journal in each day. It prompts you for things you are grateful for and your priorities for the day.

If you want a file to generate each day, you can set it up as a cronjob!

```bash
$ env EDITOR=nano crontab -e
```

Then in the editor:

```
50 8 * * * ~/code/journal/script/journal.py
```

The above command will run every day at 8:50 AM if your folder is in the directory code with the folder name journal! You can edit this to be at a different time, to only run on week days, or at a different folder on your computer!
