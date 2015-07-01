#------------------------------------------------------------------------------------------
#    PATH
#------------------------------------------------------------------------------------------
#Path to the backup (NAS/harddrive mounted on computer)
BACK_UP="../test/fakeNAS"

#Path to data
ROOT='../test/dataLocal'

#------------------------------------------------------------------------------------------
#    Processing: > klusta fileName.prm
#------------------------------------------------------------------------------------------

#PROGRAM="klusta"

# To avoid "source activate klusta", put full path
PROGRAM="/home/david/anaconda/envs/klusta/bin/klusta"



#------------------------------------------------------------------------------------------
#    Main Window   
#------------------------------------------------------------------------------------------
WIDTH=1000
HEIGHT=1000
MIN_WIDTH=int(WIDTH*0.75)
MIN_HEIGHT=int(HEIGHT*0.75)
TITLE="FileBrowser + Process Manager"

#------------------------------------------------------------------------------------------
#    FileBrowser     
#------------------------------------------------------------------------------------------

DEFAULT_ICON="folder-grey.png"
LENGTH_ID=3
DATE_TIME_FORMAT="yyyy_MM_dd_HH_mm"
EXP_PATH="/Experiments"

#------------------------------------------------------------------------------------------
#    Transfer:  > rsync RSYNC_ARG /source/ /destination     
#------------------------------------------------------------------------------------------

#Rsync arguments | -a=archive (recursive, update permission and timestamp, keep symlink...) -u=update (do not downgrade files)
RSYNC_ARG_TO_BACKUP="-au"
RSYNC_ARG_FROM_BACKUP="-au"

#------------------------------------------------------------------------------------------
#    Console
#------------------------------------------------------------------------------------------
#separator printed in the console view 
SEPARATOR='---'*10


#------------------------------------------------------------------------------------------
#    Client: where to find server by default
#------------------------------------------------------------------------------------------
IP="10.51.101.29"
PORT=8000

#------------------------------------------------------------------------------------------
# Server
#------------------------------------------------------------------------------------------
SERVER_PATH="./test/dataServer"
BACK_UP_PATH="./test/fakeNAS"
PROGRAM="klusta"
PORT=8000
SEPARATOR="---"*10
IP="127.0.0.1" 

