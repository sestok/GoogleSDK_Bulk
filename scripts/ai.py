import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build
​
# Set the path to your service account key JSON file
SERVICE_ACCOUNT_FILE = 'last.json'
​
# Set the desired API version
API_VERSION = 'directory_v1'
​
# Set the desired domain (e.g., 'example.com')
DOMAIN = 'samialhamad.com'
​
# Authenticate with the Google Workspace API using the service account key
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/admin.directory.user'], subject='')
service = build('admin', API_VERSION, credentials=credentials)
​
# Set the path to your CSV file
CSV_FILE = 'users-last.csv'
​
def create_user(first_name, last_name, email, password, org_unit_path, employee_title, change_password):
    user = {
        'name': {
            'givenName': first_name,
            'familyName': last_name
        },
        'primaryEmail': email,
        'password': password,
        'orgUnitPath': org_unit_path,
        'organizations': [
            {'title': employee_title}
        ],
        'changePasswordAtNextLogin': change_password
    }
    return service.users().insert(body=user).execute()
​
# Read the CSV file and process each row
with open(CSV_FILE, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        first_name = row['First Name']
        last_name = row['Last Name']
        email = row['Email Address']
        password = row['Password']
        org_unit_path = row['Org Unit Path [Required]']
        employee_title = row['Employee Title']
        change_password = row['Change Password at Next Sign-In'] == 'TRUE'
​
        # Create the user in Google Workspace
        create_user(first_name, last_name, email, password, org_unit_path, employee_title, change_password)
​
        print(f"User {email} created successfully.")
