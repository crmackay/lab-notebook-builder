#!/usr/bin/env python

import subprocess


# mount the finberg lab server folder to the user home folder
#mkdir /Volumes/smb

subprocess.call("mount -t smbfs //mackayc:Erikam91@ummsnas01/finberglabserver$ /Volumes/smb")

# raise exception is not available...
# and output to a log?

# call rsync on the local notebook and server notebook

#exclude_file = '/path/to/sync-exclude.txt'


# directory 
source = '/Users/christophermackay/lab/notebook/test/'

target = 'Volumes/finberglabserver\$/Lab\ Notebooks/MacKay\,\ Christopher/test'

cmd = " ".join(["rsync -a", source, target])

subprocess.call(cmd, shell = True)

# unmount

# delete directory
