#!/usr/bin/python3
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import pprint
fName = 'url_list.txt'

port = '443'
try:
    with open(fName) as f:
      for readurl in f:
        url = (readurl.strip())
        print(url)
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

except IOError:
  print ("Could not read file:"), fName