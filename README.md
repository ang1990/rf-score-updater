# rf-score-updater
#### Revival Fellowship Score Updater (SG)

###### More like a RFS Lyrics Grabber, really.

This tool is for convenience, meant to help with updating whichever
laptop we need for church use. Once I figure out PyInstaller,
I'll make a standalone Windows app as a one (double-) click solution.

Currently just grabs all the RFS Sheet Music from a folder in Dropbox
(Because I don't have the song lyrics HTMLs in my Dropbox!)

This project uses an envfile to store the secrets (like MY DROPBOX ACCESS TOKEN).
I use .env as you may notice in the code. Won't work without it obviously.


Once you get a working access token, run with Python using:
 
    ```python main.py```

Once I get all the lyrics on my Dropbox, I'll link to them instead.

Warning before using:
### 1. Running this script triggers a yuuge download (~220MB).
Make sure you're not on mobile hotspot when you run it.

Mark