import shutil
import os
import dropbox
import environs

def main():
    e = environs.Env()
    e.read_env('.env')
    client = dropbox.Dropbox(os.environ.get('ACCESS_TOKEN'))
    print('Client obtained. Downloading scores now...')
    result, data_resp = client.files_download_zip('/Revival Fellowship Singapore Music Scores')
    print('Scores downloaded. Committing to zip file...')
    with open('scores.zip', 'wb') as fp:
        fp.write(data_resp.content)
    print('zip file done.')

if __name__ == "__main__":
    main()
