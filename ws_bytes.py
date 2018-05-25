from urllib.request import getproxies
from suds.client import Client
import base64

WSDL='http://192.168.56.1:8080/FisboxWs/services/Fiskal?wsdl'

client = Client(WSDL, proxy=getproxies()).service

encoded_data = base64.b64encode(open('/home/django/doklad.txt', 'rb').read()).decode()
#encoded_data = base64.b64encode(open('/home/django/test.txt', 'rb').read())
#encoded_data = base64.b64encode(b'ABC').decode()
print(encoded_data)
print(client.sendBase64(encoded_data))
