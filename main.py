import os 
import time 
os.system("clear && figlet -tc Setting Up AWS Cloud environment")
time.sleep(2)

os.system("ansible-playbook environment.yml")

os.system("clear && figlet -tc Building HDFS-MAPREDUCE cluster on AWS")
time.sleep(2)

os.system("ansible-playbook cluster.yml")


