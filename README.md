# :sparkles:Fully Automated Hadoop HDFS-MAPREDUCE Cluster setup on top of AWS using Ansible:sparkles:
Configuring aws vpc's, subnets, Internet Gateways and then launching EC2 instances is tedious task. However, configuring hadoop hdfs cluster and map reduce cluster is super tedious.
So, here I have automated everthing using Ansible. 

## :heavy_exclamation_mark: Steps to be followed to achieve this task :heavy_exclamation_mark: 

:one: Create a ansible role to *configure AWS environment*. Here, ec2environment role will do for us.

:two: Create a ansible role to configure *HDFS Namenode*. Here, hdfs-namenode role. 

:three: Create a ansible role to configure *HDFS Datanode*. Here, hdfs-datanode role. 

:four: Create a ansible role to configure *MapReduce JobTracker*. Here, mapreduce-jobtracker role. 

:five: Create a ansible role to configure *MapReduce TaskTracker*. Here, mapreduce-tasktracker role. 

<br>
To create a role, use command :leftwards_arrow_with_hook:

      ansible-galaxy init provisionEC2 
     
Similarly, you can create other roles. 

<br>
