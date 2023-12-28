'''
This is a script to start a TPU node using Google Cloud API Python client library.

To use this you need to authenticate on GCloud. Use the GCloud CLI for this:
"gcloud auth application-default login"

This script runs this CLI command:
"gcloud compute tpus tpu-vm start node-2 --zone=europe-west4-a"
'''

from google.cloud import tpu_v2
from google.api_core.exceptions import ResourceExhausted

client = tpu_v2.TpuClient()

name=client.node_path(
  project="octo-409413",     
  location="europe-west4-a",
  node="node-2"
)

request = tpu_v2.StartNodeRequest(
  name=name,
)

node_started = False
i=0

while not node_started:
  try:
    i+=1
    print('Sending StartNodeRequest No. '+str(i))
    operation = client.start_node(request=request)
    response = operation.result()
    print(response)
    node_started = True
    break
  except ResourceExhausted as err:
    print(err.message+"\n")
