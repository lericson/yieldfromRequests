#!/usr/bin/python3


import sys
import asyncio

sys.path.append('/webroot/wsgi')

#import rdbemail as eml
from yieldfrom import requests

args = {"data": """{
      \"ReplyTo\": \"dkeeney@rdbhost.com\",
      \"To\": \"dkeeney@rdbhost.com\",
      \"From\": \"rdbhost@rdbhost.com\",
      \"TextBody\": \"BodyBody\",
      \"Subject\": \"SubSub yfreq\"
      }""",
 "headers": {
      "Accept": "application/json",
      "X-Postmark-Server-Token": "0be3da1e-f0b3-421e-ae6c-64ceda2cb914",
      "Content-Type": "application/json"
  },
  "allow_redirects": False,
  "url": "https://api.postmarkapp.com/email",
  "verify": None,
  "method": "POST",
  "timeout": 2
 }

loop = asyncio.get_event_loop()

@asyncio.coroutine
def getit():
    yield from requests.request(**args)


loop.run_until_complete(getit())
