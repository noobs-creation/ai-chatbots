from __future__ import print_function
import os.path
# import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type
import time

# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ['https://mail.google.com/']
# our_email = 'siddhanthdas99@gmail.com'

def reading_emails(email_type="primary"):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    loc_007 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'token-primary-007.json'))
    loc_99 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'token-secondary-99.json'))
    loc_50 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'token-tertiary-50.json'))
    loc_cred = os.path.abspath(os.path.join(os.path.dirname(__file__), 'credentials.json'))
    if email_type == "primary":
        if os.path.exists(loc_007):
            creds = Credentials.from_authorized_user_file(loc_007, SCOPES)
    elif email_type == "secondary":
        if os.path.exists(loc_99):
            creds = Credentials.from_authorized_user_file(loc_99, SCOPES)
    elif email_type == "tertiary":
        if os.path.exists(loc_50):
            creds = Credentials.from_authorized_user_file(loc_50, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                loc_cred, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        if email_type == "primary":
            with open(loc_007, 'w') as token:
                token.write(creds.to_json())
        elif email_type == "secondary":
            with open(loc_99, 'w') as token:
                token.write(creds.to_json())
        elif email_type == "third":
            with open(loc_50, 'w') as token:
                token.write(creds.to_json())
        # with open('token.json', 'w') as token:
        #     token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    
    unread_emails = []
    
    # msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = results.get('messages', [])
    # print(messages)
    for mssg in messages:
        temp_msg = {}
        # print(mssg)
        # print('\n\n\n--------------------------------------------------------------------\n')
        msg = service.users().messages().get(userId='me', id=mssg['id']).execute()
        # parts can be the message body, or attachments
        payload = msg['payload']
        headers = payload.get("headers")
        # print(msg['snippet'])
        # folder_name = "email"
        has_subject = False
        if headers:
            # this section prints email basic info & creates a folder for the email
            for header in headers:
                name = header.get("name")
                value = header.get("value")
                if name.lower() == 'from':
                    # we print the From address
                    # print("From:", value)
                    temp_msg['from'] = value
                if name.lower() == "to":
                    # we print the To address
                    # print("To:", value)
                    temp_msg['to'] = value
                if name.lower() == "subject":
                    # make our boolean True, the email has "subject"
                    has_subject = True
                    # print("Subject:", value)
                    temp_msg['subject'] = value
                if name.lower() == "date":
                    # we print the date when the message was sent
                    # print("Date:", value)
                    temp_msg['date'] = value
        if not has_subject:
            # print('no subject available')
            temp_msg['subject'] = 'no subject available'
        temp_msg['snippet'] = msg['snippet']
        unread_emails.append(temp_msg)
    
    service.users().messages().batchModify(userId='me',body={'ids': [ msg['id'] for msg in messages ],'removeLabelIds': ['UNREAD']}).execute()
    # print(unread_emails)
    return unread_emails