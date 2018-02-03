# install ssh
sudo apt-get install openssh-server

# check if start
sudo ps -e |grep ssh 

# start
sudo service ssh start

# connect
ssh username@192.168.1.103 

# disconnect
exit

# file transfer
scp /media/ml/all_video_restore/* user@IP:/home/Downloads
