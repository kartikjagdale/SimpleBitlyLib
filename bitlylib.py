# Bitly Python Library
import requests
import sys
import json
API_KEY = '2aa488f3be85c8983395757fb77aff9f3d083e5b'
lngurl = None
def shorten():
	query_params = {'access_token':API_KEY,'longUrl':lngurl}
	endpoint = 'https://api-ssl.bitly.com/v3/shorten'
	try:
		response = requests.get(endpoint, params=query_params, verify=False)
	except requests.ConnectionError:
                print 'Network Problem,Please check Internet Connection'
	if response.status_code == 200:
                data = json.loads(response.content)
                while(True):
                        if data['status_code']==200:
                                return  data['data']['url']
                                break
                        else:
                                print "There was some problem, Error Code :" , data['status_code']
                                print "Error status text is : ", data['status_txt']
                                break
        else:
                print 'There was some problem:\n status_code:',response.status_code       
                        
        
#End of Bitly API library
