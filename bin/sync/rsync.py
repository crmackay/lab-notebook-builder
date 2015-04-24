#!/usr/bin/env python

import subprocess

# rsync (direc

# mount the finberg lab server folder to the user home folder
mount -t smbfs //ummsnas01/finberglabserver$ ~/smb

# raise exception is not available...
# and output to a log?

# call rsync on the local notebook and server notebook

exclude_file = '/path/to/sync-exclude.txt'

source = ''

target = ''

'''
```$ rsync --exclude-from=exclude_file```