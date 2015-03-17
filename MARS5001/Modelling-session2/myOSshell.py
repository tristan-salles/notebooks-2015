##########################################################
# Some usefull shell command for the MARS5001 lectures
# Author: Tristan Salles
# Date: 13/03/15
#
# To run properly you will need to import:
# 
# import os
# import glob
#
# Then 
# import myOSshell.py
#
##########################################################
import os
import glob
from distutils.dir_util import mkpath

def xbeach_command(DIR):
    # Get the current working directory
    working_path=os.getcwd()
    # Prepare the shell command
    run_xbeach='(cd '+working_path+'/'+DIR+'; xbeach)'
    # run XBEACH
    os.system(run_xbeach)
    
def list_dir(DIR):
    print glob.glob(DIR+'/*')

def dropbox_upload(OUTDIR,OUTFILE,UPLOADDIR):
    # Get the current working directory
    working_path=os.getcwd()
    # Prepare the shell command
    dropbox_upload='(~/Dropbox-Uploader/dropbox_uploader.sh upload '+working_path+'/'+OUTDIR+'/'+OUTFILE+' '+UPLOADDIR+')'
    # upload file to dropbox
    os.system(dropbox_upload)

def dropbox_download(REMOTE,LOCALDIR,LOCALFILE):
    # Get the current working directory
    working_path=os.getcwd()
    # Prepare the shell command
    dropbox_download='(~/Dropbox-Uploader/dropbox_uploader.sh download '+REMOTE+' '+working_path+'/'+OUTDIR+'/'+OUTFILE+')'
    # download file from dropbox
    os.system(dropbox_download)

def delete(NAME):
    # Get the current working directory
    working_path=os.getcwd()
    delete_os='(rm -r '+working_path+'/'+NAME+')'
    # run RM
    os.system(delete_os)

def copy(NAME,PLACE):
    # Get the current working directory
    working_path=os.getcwd()
    copy_os='(cp -r '+working_path+'/'+NAME+' '+PLACE+')'
    # run CP
    os.system(copy_os)

def mkdir(DIR):
    mkpath('./'+DIR)
