from urllib.request import getproxies
from suds.client import Client


WSDL='http://callcentrum.llarik.sk:8080/VATNumberValidator/EUVatValidator?wsdl'

client = Client(WSDL, proxy=getproxies()).service

print(client.isValid('SK2020192691'))
