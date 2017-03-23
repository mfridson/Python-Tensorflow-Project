import pandas as pd
import json
import attr
import sys
from py_ms_cognitive import PyMsCognitiveImageSearch
values=[]
cont_sz=[]
thumb=[]
token=[]
host_page=[]
search_url=[]
jsn=[]
image_id=[]
cont_url=[]
cont_name=[]
search_term = "korean painting"
search_service = PyMsCognitiveImageSearch(search_term)
first_fifty_result = search_service.search_all(quota=50000, format='json')

for i in range(0,50000):
    cont_sz.append(first_fifty_result[i].content_size)
    thumb.append(first_fifty_result[i].thumbnail_url)
    token.append(first_fifty_result[i].image_insights_token)
    host_page.append(first_fifty_result[i].host_page_url)
    search_url.append(first_fifty_result[i].web_search_url)
    jsn.append(first_fifty_result[i].json)
    image_id.append(first_fifty_result[i].image_id)
    cont_url.append(first_fifty_result[i].content_url)
    cont_name.append(first_fifty_result[i].name)

result = {'content_size': cont_sz, 'thumbnail_url': thumb, 'image_insights_token': token, 'host_page_url': host_page,'web_search_url': search_url, 'json': jsn, 'image_id': image_id, 'content_url': cont_url, 'name': cont_name}


    #print(dict.fromkeys(first_fifty_result[0]._))


#for i in range(0,50):
 #   content=first_fifty_result[i].__dict__
  #  print(content)

#d = {}
#for i in range(0,50):
 #   for k in first_fifty_result[i].__dict__.iterkeys():
  #      d[k] = tuple(d[k] for d in first_fifty_result[i].__dict__)
#print(d)
#d={keys:first_fifty_result.__dict__.values()}
#d = dict(value for value in first_fifty_result[0:50].__dict__.values())
#d = {key: value for (key, value) in first_fifty_result[0]._dict_}

#d=dict(zip(key,values))
pd.DataFrame.to_csv(pd.DataFrame.from_dict(result,orient='columns'),'korean.csv')