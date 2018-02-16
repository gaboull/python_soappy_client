from SOAPpy import SOAPProxy
from SOAPpy import Types


namespace = "http://server.fiskal.llarik.sk/"
url = "http://10.17.0.6:8080/FisboxWs/services/Fiskal"
input = Types.stringType(name = (namespace, "message"), data = "Python")

proxy = SOAPProxy(url, namespace = namespace)
proxy.config.debug = 1
proxy.connect(input)