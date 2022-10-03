import pandas as pd
import urllib.request
import json
import time

def query_graphql(graphql_retrieve_query):
    events = []
    #print(graphql_retrieve_query)
    query_data = json.dumps({'query': graphql_retrieve_query}).encode('utf-8')
    req = urllib.request.Request('https://api.thegraph.com/subgraphs/name/aavegotchi/gotchiverse-matic',
                                 data=query_data,
                                 method='POST')
    resp = urllib.request.urlopen(req)
    query_obj = json.loads(resp.read())
    if 'data' in query_obj:
        events.extend(query_obj['data']['installations'])

    return events

query_installations_template ='''
{
  installations(first: 1000, where: {type_in:["%d"], equipped: true, id_gt:"%s"}) {
    id
    type {
      id
    }
    equipped
    parcel {
      id
    }
    owner
  }
}
'''

def query_parcels_by_installation(timestamp):
    parcels_installations_list = []
    i=0
    for id_installation in range(56,92):
        print(id_installation)
        last_id= ''
        empty_query = False
        while (empty_query == False):
            graphquery_installations = query_installations_template % (id_installation, last_id)
            payload_json_obj = query_graphql(graphquery_installations)
            parcels_installations_list += payload_json_obj
            print('len= ', len(parcels_installations_list))
            if ((len(payload_json_obj)) == 0):
                last_id = ''
                empty_query = True
            else:
                last_id = parcels_installations_list[-1]['id']

    df = pd.json_normalize(parcels_installations_list)
    df =df.drop_duplicates(subset='id', keep='last').reset_index(drop=True)
    df.sort_values(by='id', ascending=True)
    filename = 'installations_' + timestamp + '.json'
    df.to_json(filename, orient='records')

query_parcels_by_installation(str(int(time.time())))