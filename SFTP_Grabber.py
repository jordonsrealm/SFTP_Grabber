#!/usr/bin/env python
import pysftp

from os import listdir
from os.path import isfile, join

remote_domain_name = '123.server.ip'
username = 'username'
password = 'password'
remote_working_directory = '/remoteWorkingDirectory/'
local_file_directory = 'localFileDirectory'

# domain name or server ip:
sftp = pysftp.Connection(remote_domain_name, username=username, password=password)

sftp.cwd(remote_working_directory)


def grab_new_files(list_to_compare):
    remote_master_files = sftp.listdir()

    newest_files = set(remote_master_files).difference(list_to_compare)

    for newFile in newest_files:
        local_file = open(newFile, 'wb')
        sftp.get(newFile)
        local_file.close()

    pysftp.quit()


local_files_to_compare = [f for f in listdir(local_file_directory) if isfile(join(local_file_directory, f))]

# Downloads the files locally
grab_new_files(local_files_to_compare)