from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError

port = '443'
list = ['www.ibm.com','www.bbc.co.uk','www.itv.com']

try:
  for url in list:
    context = ssl.create_default_context()
  
    with socket.create_connection((url, port)) as sock:
        with context.wrap_socket(sock, server_hostname=url) as ssock:
          data = (ssock.getpeercert())
          notafter_date = data["notAfter"]
          subject = data["subject"]
          issuer = data["caIssuers"]
          print("Subject:",subject)
          print("Issuers:",issuer)
          print("Expiry date:",notafter_date)
except:
  print("Something else went wrong")