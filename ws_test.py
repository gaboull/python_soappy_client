from urllib.request import getproxies
from suds.client import Client


WSDL='http://10.17.0.6:8080/FisboxWs/services/Fiskal?wsdl'

client = Client(WSDL, proxy=getproxies()).service

print(client.connect('Python'))
#print(client.getServerVersion())
#print(client.getModuleVersion())
print(client.getModuleDate())
#print(client.getModuleSerialNumber())
#print(client.getModuleInfo())
#print(client.getParagonCopy(100))
print(client.getVatSetup())
print(client.getParagonInfoExtended(5000))
