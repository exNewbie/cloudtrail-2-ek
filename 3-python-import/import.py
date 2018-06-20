#!/usr/local/bin/python
import gzip
import sys
import os
import json
import datetime

from datetime import datetime
from elasticsearch import Elasticsearch
from datetime import datetime

LOG_DIR = '/mnt'
ELASTICSEARCH_HOST = 'elasticsearch'
ELASTICSEARCH_SCHEME = 'http'
ELASTICSEARCH_PORT = 9200
datetime_fmt = "%Y-%m-%dT%H:%M:%SZ"

######################################################################

def safe_submit_log(es, log_entry, count, index_date):
    result = []

    # The log_entry can only be a string or a dict
    if isinstance(log_entry, str):
      log_entry = {"message": log_entry}
    elif not isinstance(log_entry, dict):
        raise Exception( "Cannot send the entry as it must be either a string or a dict. Provided entry: " + str(log_entry) )

    # Send to ElasticSearch
    str_entry = json.dumps(log_entry)
    #For debugging purpose uncomment the following line
    #print(str_entry)
    index_partition = 'cloudtrail-2-elk-' + str(index_date)

    try:
      result = es.index(index=index_partition, body=str_entry.encode("UTF-8"), id=count, doc_type='cloudtrail')
    except Exception as e:
      print('Unexpected exception in safe_submit_log: {}'.format(str(e)))
      print(str_entry.encode("UTF-8"))
      pass
    return result

######################################################################

def generate_logs(LOG_DIR, es):
  count = 0
  for (dirpath, dirnames, filenames) in os.walk(LOG_DIR):
    if filenames:
      for filename in filenames:
        full_path = dirpath + '/' + filename
        print('Processing filename ' + full_path)
        if filename[-3:] == '.gz':
          with gzip.GzipFile(full_path) as decompress_stream:
            data = decompress_stream.read()
        else:
          with open(full_path, 'rb') as f:
            data = f.read()

        cloud_trail = json.loads(data)
        for event in cloud_trail['Records']:
          if 'readOnly' not in event:
            count = count + 1
            index_date = datetime.strptime(event['eventTime'], datetime_fmt).date()
            s = safe_submit_log(es, event, count, index_date)
  return 

######################################################################

def execute():
  es = Elasticsearch( [ELASTICSEARCH_HOST], scheme=ELASTICSEARCH_SCHEME, port=ELASTICSEARCH_PORT )
  
  try:
    generate_logs(LOG_DIR, es)
      
  except Exception as e:
    print('Unexpected exception in execute: {}'.format(str(e)))

  return

######################################################################

execute()
print('Work finished')