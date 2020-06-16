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
:/tmp/cloudtrail-2-elk$ docker-compose up -d
Creating network "cloudtrail2ek_cloudtrail-2-ek" with the default driver
Creating cloudtrail2ek_elasticsearch_1 ... done
Creating cloudtrail2ek_kibana_1        ... done
Creating cloudtrail2ek_worker_1        ... done

```
