#! python3
# zip_current_directory.py - Copies an entire dir and its contents into a
# Zip file.

import zipfile, os

root_dir = '/Users/grogu/Documents/PDF Conversions'

def backupToZip(dir(object)):
    # Backup the entire contents of "dir" into a zip file.

    dir = os.path.abspath(dir) # need to make sure to use absolute dir

    # Figure out the file name based on what files already exist.

    number = 1
    while True:
        zipFilename = os.path.basename(dir) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    

    # TODO: Create the ZIP file.
        print('Creating %s...' %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire dir tree and compress the files in each dir.
    for root, dir, files in os.walk(dir):
        print('Adding files in %s...' %(dirname))
        # Add current dir to ZIP file.join()
        backupZip.write(dirname)
        # Add all the files in this dir to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(dir) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the backup ZIP files
            backupZip.write(os.path.join(dirname, filename))
    backupZip.close()
    print('Done!')
    
backupToZip(root_dir)
