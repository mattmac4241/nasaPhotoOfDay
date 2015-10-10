import subprocess
import sys

def script(code):
    return subprocess.call(
        ['bash', '-c', code],
        shell=False,
        stdin=None,
        stdout=sys.stdout,
        stderr=sys.stdout)



def set_wallpaper(file):
    # See http://superuser.com/a/689804.
    assert \
        script('''
            sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '%(file)s'"
            killall Dock
        ''' % {
            'file': file,
        }) == 0, \
        'Failed to set wallpaper'
