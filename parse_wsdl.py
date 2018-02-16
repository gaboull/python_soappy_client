from SOAPpy import WSDL


# just use the path to the wsdl of your choice
wsdlObject = WSDL.Proxy('http://10.17.0.6:8080/FisboxWs/services/Fiskal?wsdl')

print 'Available methods:'
for method in wsdlObject.methods.keys() :
  print method
  ci = wsdlObject.methods[method]
  # you can also use ci.inparams
  for param in ci.outparams :
    # list of the function and type
    # depending of the wsdl...
    print 'Name:', param.name
    print 'Type:', param.type
  print

