# cloudtrail-2-ek
For the need of presenting boring-JSON Cloud Trail in a nicer user interface, this solution is 
* Create a Elastic Search Cluster
* Create a Kibana dashboard to display data of the Elastic Search Cluster
* Import log files to the Elastic Search Cluster


## Clone the repo
Personally I store this repository at `/tmp`.  
```
:$ cd /tmp/

:/tmp$ git clone https://github.com/exNewbie/cloudtrail-2-elk.git
Cloning into 'cloudtrail-2-elk'...
remote: Counting objects: 15, done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 15 (delta 0), reused 11 (delta 0), pack-reused 0
Unpacking objects: 100% (15/15), done.
```

## Create the folder to store log files
This folder is important. The process script relies on this folder to retrieve and process log files. 

```
:$ mkdir /tmp/cloudtrail-2-elk/logs
```

## Store log files at logs folder
Copy logs files to folder `cloudtrail-2-elk/logs`

```
:$ ls -l /tmp/cloudtrail-2-elk/logs
drwxrwxr-x 2 root root 1142784 Jun 16 22:26 ./
drwxr-xr-x 7 root root    4096 Jun 16 22:28 ../
-rw-rw-r-- 1 root root   33152 Feb 22 10:04 CloudTrail_ap-southeast-2_20200222T0000Z_4RqStJkbG2DSPBFX.json.gz
-rw-rw-r-- 1 root root    8527 Feb 22 09:57 CloudTrail_ap-southeast-2_20200222T0000Z_XqlHnLOcV7OgTLSw.json.gz
-rw-rw-r-- 1 root root    6288 Feb 22 10:03 CloudTrail_ap-southeast-2_20200222T0005Z_2siNuPuo5NRDrrWD.json.gz
-rw-rw-r-- 1 root root   32549 Feb 22 10:09 CloudTrail_ap-southeast-2_20200222T0005Z_SO4PKAQY3akl5Fnm.json.gz
-rw-rw-r-- 1 root root   12038 Feb 22 10:13 CloudTrail_ap-southeast-2_20200222T0010Z_k7miNJzgWkyY0dX9.json.gz
-rw-rw-r-- 1 root root    4008 Feb 22 10:09 CloudTrail_ap-southeast-2_20200222T0010Z_rrMtHZZz6frLrrLf.json.gz
-rw-rw-r-- 1 root root    9970 Feb 22 10:19 CloudTrail_ap-southeast-2_20200222T0015Z_eeLzsE9QAHQjtlJk.json.gz
```

## Process log files

```
:$ docker-compose up -d
Creating network "cloudtrail2ek_cloudtrail-2-ek" with the default driver
Creating cloudtrail2ek_elasticsearch_1 ... done
Creating cloudtrail2ek_kibana_1        ... done
Creating cloudtrail2ek_worker_1        ... done
```

### Wait 1-3 minutes for Kibana to be ready
Browse Kibana at `http://localhost:5601`

![Kibana](https://github.com/exNewbie/cloudtrail-2-ek/blob/feature/docker-compose/images/kibana.png)

### Create an index pattern to Kibana
Go to Index management at `http://localhost:5601/app/kibana#/management/kibana/index_pattern`

![Index Pattern](https://github.com/exNewbie/cloudtrail-2-ek/blob/feature/docker-compose/images/create-index-pattern.png)

![Time Filter](https://github.com/exNewbie/cloudtrail-2-ek/blob/feature/docker-compose/images/choose-time-filter.png)


### Enjoy the beauty of log files
Browse logs at `http://localhost:5601/app/kibana#/discover`

![Discovery](https://github.com/exNewbie/cloudtrail-2-ek/blob/feature/docker-compose/images/discovery.png)
