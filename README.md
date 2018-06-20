# cloudtrail-2-ek
Download Cloud Trail logs to your local computer and import them to your local Elastic Search + Kibana

```
:$ cd /tmp/

:/tmp$ git clone https://github.com/exNewbie/cloudtrail-2-elk.git
Cloning into 'cloudtrail-2-elk'...
remote: Counting objects: 15, done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 15 (delta 0), reused 11 (delta 0), pack-reused 0
Unpacking objects: 100% (15/15), done.


:/tmp$ cd cloudtrail-2-elk/
:/tmp/cloudtrail-2-elk$ cd 1-elk-es/
:/tmp/cloudtrail-2-elk/1-elk-es$ ./start-v6 
bf50378fb1cae3f4062661dc6ad219d8baf01ca01b34d00c794e4641f77c1432
:/tmp/cloudtrail-2-elk/1-elk-es$ docker ps
CONTAINER ID        IMAGE                                                     COMMAND                  CREATED             STATUS                  PORTS                                            NAMES
bf50378fb1ca        docker.elastic.co/elasticsearch/elasticsearch-oss:6.3.0   "/usr/local/bin/dock…"   6 seconds ago       Up Less than a second   0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp   elasticsearch-v6


:/tmp/cloudtrail-2-elk/1-elk-es$ cd ../2-elk-kibana/
:/tmp/cloudtrail-2-elk/2-elk-kibana$ ./start-v6 elasticsearch-v6
6119e15c0cfe3da7f1e920ab6df08219bad123961cc52d83be3f264f6340a8c5
:/tmp/cloudtrail-2-elk/2-elk-kibana$ docker ps
CONTAINER ID        IMAGE                                                     COMMAND                  CREATED             STATUS                  PORTS                                            NAMES
6119e15c0cfe        docker.elastic.co/kibana/kibana-oss:6.3.0                 "/bin/bash -c /usr/l…"   5 seconds ago       Up 3 seconds            0.0.0.0:5601->5601/tcp                           kibana-v6
bf50378fb1ca        docker.elastic.co/elasticsearch/elasticsearch-oss:6.3.0   "/usr/local/bin/dock…"   29 seconds ago      Up Less than a second   0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp   elasticsearch-v6


:/tmp/cloudtrail-2-elk/2-elk-kibana$ cd ../3-python-import/
:/tmp/cloudtrail-2-elk/3-python-import$ ./start elasticsearch-v6 /tmp/CloudTrail/08
f706860bb712629e788be087ca6d46e4234319aa42ab5939a6fe960e7d90e70b
:/tmp/cloudtrail-2-elk/3-python-import$ docker ps
CONTAINER ID        IMAGE                                                     COMMAND                  CREATED              STATUS                          PORTS                    NAMES
f706860bb712        python:latest                                             "/bin/bash -c 'pip i…"   7 seconds ago        Up 6 seconds                                             cloudtrail-2-elk
6119e15c0cfe        docker.elastic.co/kibana/kibana-oss:6.3.0                 "/bin/bash -c /usr/l…"   About a minute ago   Up About a minute               0.0.0.0:5601->5601/tcp   kibana-v6
bf50378fb1ca        docker.elastic.co/elasticsearch/elasticsearch-oss:6.3.0   "/usr/local/bin/dock…"   About a minute ago   Restarting (1) 24 seconds ago                            elasticsearch-v6


:/tmp/cloudtrail-2-elk/3-python-import$ docker logs cloudtrail-2-elk
Collecting elasticsearch
  Downloading https://files.pythonhosted.org/packages/c3/e3/146b675e6d0138a49c4b817b4e68170eb9b75cee7e71fa3ec69624c4f467/elasticsearch-6.2.0-py2.py3-none-any.whl (69kB)
Collecting urllib3<1.23,>=1.21.1 (from elasticsearch)
  Downloading https://files.pythonhosted.org/packages/63/cb/6965947c13a94236f6d4b8223e21beb4d576dc72e8130bd7880f600839b8/urllib3-1.22-py2.py3-none-any.whl (132kB)
Installing collected packages: urllib3, elasticsearch
Successfully installed elasticsearch-6.2.0 urllib3-1.22
Processing filename /mnt/365000009351_CloudTrail_ap-southeast-2_20180607T2045Z_JpI2IFxxxxxeTLM.json.gz
Work finished

```

