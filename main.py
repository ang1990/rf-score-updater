import os
import sys
import requests
import zipfile

SONGS_ZIP_NAME = 'songs.zip'

def main():
    path = os.path.abspath(sys.argv[0])
    curr_folder = '/'.join(path.split('/')[:-1])
    os.chdir(curr_folder)

    print('Downloading choruses now...')
    url = 'https://www.dropbox.com/sh/q73i1c796vhj01o/AABA48foZmFZn_mM67AUBsR1a?dl=1'
    response = requests.get(url)
    print('Scores downloaded. Committing to zip file...')

    try:
        os.remove(SONGS_ZIP_NAME)
    except FileNotFoundError:
        pass

    with open(SONGS_ZIP_NAME, 'wb') as fp:
        fp.write(response.content)
    print('zip file done.')

    def file_to_remove(filename, this_exe_name=None):
        if not this_exe_name:
            this_exe_name = sys.argv[0].split('/')[-1]
        fn = str(filename)

        return not fn.startswith('.') and\
               not fn.endswith('.exe') and\
               fn != this_exe_name and\
               fn != SONGS_ZIP_NAME

    current_files = [f for f in os.listdir('.') if file_to_remove(f)]
    for file in current_files:
        os.remove(file)

    with zipfile.ZipFile(SONGS_ZIP_NAME, "r") as zip_ref:
        zip_ref.extractall(".")
        print('Zip extracted.')

    print('Cleaning up temp zip file.')
    os.remove(SONGS_ZIP_NAME)

if __name__ == "__main__":
    main()