import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
​
# Path to your service account key JSON file
SERVICE_ACCOUNT_KEY_FILE = 'last.json'
​
# SCOPES required to access the Admin SDK
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
          'https://www.googleapis.com/auth/admin.directory.group',
          'https://www.googleapis.com/auth/admin.directory.group.member']
​
# Authenticate and build the service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_KEY_FILE, scopes=SCOPES, subject='root@samialhamad.com'
)
service = build('admin', 'directory_v1', credentials=credentials)
​
# Function to add a user to a group
def add_user_to_group(user_email, group_email):
    try:
        service.members().insert(groupKey=group_email, body={'email': user_email}).execute()
        print(f"User {user_email} added to group {group_email} successfully.")
    except Exception as e:
        print(f"An error occurred while adding user {user_email} to group {group_email}: {e}")
​
# Retrieve all users in the domain
def retrieve_users():
    try:
        users = service.users().list(customer='my_customer', maxResults=200).execute()
        users_list = users.get('users', [])
​
        if not users_list:
            print('No users found.')
        else:
            print('Users:')
            for user in users_list:
                email = user.get('primaryEmail')
                tags = user.get('customSchemas', {}).get('Contacts', {}).get('SpecialTag', [])
                if 'SpecialTag' in tags:
                    add_user_to_group(email, 'publitas_group@samialhamad.com')
​
    except Exception as e:
        print(f"An error occurred: {e}")
​
# Call the function to retrieve and assign users to the group
retrieve_users()
