from SOAPpy import (
    HTTPTransport,
    Config,
    SOAPAddress,
    SOAPProxy,
    Types
)
import urllib2
import base64

class AuthenticatedTransport(HTTPTransport):
    _username = None
    _password = None

    def __init__(self, username, password):
        self._username = username
        self._password = password        

    def call(self, addr, data, namespace, soapaction = None, encoding = None, http_proxy = None, config = Config, timeout = 10):
        if not isinstance(addr, SOAPAddress):
            addr = SOAPAddress(addr, config)

        content_type = 'text/xml';
        if encoding != None:
            content_type += '; charset="%s"' % encoding

        encoded_auth = None
        if ( isinstance(self._username, str) != False ):
            if ( isinstance(self._password, str) == False ):
                self._password = ""
            encoded_auth = base64.b64encode('%s:%s' % (self._username, self._password))

        this_request = None
        if ( encoded_auth is not None ):
            this_request = urllib2.Request(
                url=addr.proto + "://" + addr.host + addr.path,
                data=data,
                headers={
                    "Content-Type":content_type,
                    "SOAPAction":"%s" % "",
                    "Authorization":"Basic %s" % encoded_auth
                }
            )
        else:
            this_request = urllib2.Request(
                url=addr.proto + "://" + addr.host + addr.path,
                data=data,
                headers={
                    "Content-Type":content_type,
                    "SOAPAction":"%s" % "",
                }
            )

        response = urllib2.urlopen(this_request)
        data = response.read()

        # get the new namespace
        if namespace is None:
            new_ns = None
        else:
            new_ns = self.getNS(namespace, data)

        # return response payload
        return data, new_ns


username = "user"
password = "secret"

url = "http://%s:%s@10.17.0.6:8080/FisboxWs/services/Fiskal" % (username, password)
namespace = "http://server.fiskal.llarik.sk/"
proxy = SOAPProxy(url, namespace=namespace, transport = AuthenticatedTransport(username, password))
proxy.config.strictNamespaces = 1
proxy.config.debug = 1

input = Types.stringType(name = (namespace, "message"), data = "Python")
print(proxy.connect(input))

print(proxy.getServerVersion())
print(proxy.getModuleVersion())
print(proxy.getModuleSerialNumber())
print(proxy.getModuleDate())
print(proxy.getModuleInfo())

input = Types.decimalType(name = (namespace, "fmId"), data = 100)
print(proxy.getParagonCopy(input))