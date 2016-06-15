#!/usr/bin/env python

#
# Author: Stephen Newhouse <stephen.j.newhouse@gmail.com>
# Date: June 2016
# see: http://amp.pharm.mssm.edu/Enrichr/help#api for API docs
#
# Usage: python query_enrichr_v0.1.py <genelist> <listdesrciption> <enrichr_library> <enrichr_results>

import json
import requests
import sys

#genelist = "gene_list.txt"
#enrichr_library = "KEGG_2015"
#listdesrciption = "TEST"
#enrichr_results = "example_enrichment_kegg"

genelist = sys.argv[1]
listdesrciption = sys.argv[2]
enrichr_library = sys.argv[3]
enrichr_results = sys.argv[4]

##
print 'Input file is:', genelist
print 'Analysis name: ', listdesrciption
print 'Enrichr Library: ', enrichr_library
print 'Enrichr Results File: ', enrichr_results

# get gene lits
f = open(genelist)
genes = f.read()

## enrichr url
ENRICHR_URL = 'http://amp.pharm.mssm.edu/Enrichr/addList'

# stick gene list here
genes_str = str(genes)

# name of analysis or list
#description = 'Example gene list'
description = str(listdesrciption)

# payload
payload = {
  'list': (None, genes_str),
  'description': (None, description)
}

# response
response = requests.post(ENRICHR_URL, files=payload)

if not response.ok:
  raise Exception('Error analyzing gene list')

job_id = json.loads(response.text)

print(job_id)

################################################################################
# View added gene list
#
#import json
#import requests

ENRICHR_URL_A = 'http://amp.pharm.mssm.edu/Enrichr/view?userListId=%s'

user_list_id = job_id['userListId']
print(user_list_id)

response_gene_list = requests.get(ENRICHR_URL_A % str(user_list_id))
if not response_gene_list.ok:
    raise Exception('Error getting gene list')

added_gene_list = json.loads(response_gene_list.text)
print(added_gene_list)

################################################################################
# Get enrichment results
#
#import json
#import requests


ENRICHR_URL = 'http://amp.pharm.mssm.edu/Enrichr/enrich'
query_string = '?userListId=%s&backgroundType=%s'
## get id data
user_list_id = job_id['userListId']
print(user_list_id)

## Libraray
gene_set_library = str(enrichr_library)

response = requests.get(
    ENRICHR_URL + query_string % (str(user_list_id), gene_set_library)
 )
if not response.ok:
    raise Exception('Error fetching enrichment results')

data = json.loads(response.text)
print(data)

################################################################################
##Download file of enrichment results

ENRICHR_URL = 'http://amp.pharm.mssm.edu/Enrichr/export'
query_string = '?userListId=%s&filename=%s&backgroundType=%s'
user_list_id = str(job_id['userListId'])
filename = enrichr_results
gene_set_library = str(enrichr_library)

url = ENRICHR_URL + query_string % (user_list_id, filename, gene_set_library)
response = requests.get(url, stream=True)

with open(filename + '.txt', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
################################################
print("Done")
