
import os
import pprint
import json
import google.oauth2.credentials
from google.oauth2 import id_token
from googleapiclient.discovery import build
from google.auth.transport import requests
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

pp = pprint.PrettyPrinter(indent=2)

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This access scope grants read-only access to the authenticated user's Drive
# account.
SCOPES=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
    ]
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=SCOPES)
  # urlslink,_=flow.authorization_url()
  # print("i got the url",urlslink)
  flow.run_local_server()
  session = flow.authorized_session()
  profile_info = session.get(
    'https://www.googleapis.com/userinfo/v2/me').json()
  print(profile_info)
  
  return profile_info

if __name__ == '__main__':
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
