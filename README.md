# publitas-assignment

Objective
The primary objective of this implementation plan is to streamline and automate the bulk addition of users to Google Workspace. By developing a custom script, our aim is to optimize efficiency, enhance the user onboarding experience, and eliminate manual administrative processes involved in adding a significant number of users to Google Workspace.
Requirements
Bulk User Addition
The script should be designed to support the bulk addition of users, accommodating an unlimited number of users by extracting data from a CSV file. The CSV file format should adhere to a predefined structure, including essential user attributes such as Full Name, Email, Password, Organization Unit, Employee Title, and an optional flag indicating whether users need to change their password at the next login. This approach ensures flexibility and scalability when adding users in bulk.
Security Measures (Optional)
To prioritize data security, it is recommended to include a “Change Password after Next Login” column in the CSV file. Setting this column to “True” ensures that users are prompted to change their passwords upon initial login, mitigating the risk of credential breaches.
Resources
Software and Packages
This implementation requires Python 3.7.10 or a higher version installed locally.
The following Python packages need to be installed using the package management tool “pip”: google-api-python-client google-auth-httplib2 google-auth-oauthlib. These packages provide the necessary functionality to interact with the Google Admin SDK API.
Detailed instructions for installing and configuring these resources can be found in the official Google Admin SDK API documentation [1].
Google Cloud and Workspace: A Google Cloud project and a Google Workspace domain with API access enabled and domain-wide delegation are essential prerequisites for this implementation. The Google Account used for the integration must possess administrator privileges within the Workspace domain. Information on setting up the necessary Google Cloud project and enabling the required API access can be found in the official Google Admin SDK API documentation [1].
Google Admin SDK API documentation for detailed instructions and guidance listed below provides step-by-step explanations of setting up the local development environment, implementing OAuth for authentication, creating users via the Admin SDK API [2], and assigning group members [3]. Referencing these resources ensures adherence to best practices and accurate integration with the Google Workspace ecosystem.
Workflow
Adding Users in Bulk — (Script: ai.py):
To facilitate the bulk addition of users, the script will follow this workflow:Establish a secure connection to the Admin SDK API using OAuth, allowing for proper authentication and authorization. The necessary steps for establishing this connection are outlined in the official Google Admin SDK API documentation [1].
Configure the required scopes for the Admin SDK API, ensuring the script has appropriate permissions for creating users. The required scopes can be found in the documentation [2].
Locate the users-last.csv file within the same directory as the script and parse each row individually to extract the required user attributes, following the CSV file format mentioned earlier.
Utilize the Admin SDK API to process API requests, systematically adding users based on the extracted information. The official Admin SDK API documentation provides detailed information on the API endpoints and parameters required for user creation [2].
Assigning Users in Bulk to a Directory Group — (Script: group_member.py):
To assign users to a specific directory group in bulk, the script will follow this workflow:
Establish a secure connection to the Admin SDK API using OAuth, following the authentication process outlined in the official Google Admin SDK API documentation [1].
Configure the necessary scopes to enable the required permissions for adding users and managing groups. The required scopes can be found in the documentation [2].
Implement the logic within the script to add users based on a predefined tag, which is hardcoded as “SpecialTag”. The script will identify users with this tag and assign them to the appropriate directory group.
Define the target group to which users will be added using the designated email address, “publitas_group@samialhamad.com”. This email address should correspond to the desired group within the Google Workspace domain.
Deployment
Local Execution: The script can be executed locally within a Linux Shell using this command ‘python3 ai.py’, ensuring that all required dependencies are met. Running the script locally provides flexibility and allows for easy integration into existing workflows.
Confirmation and Reporting: As part of the execution, the script will display the email addresses of successfully added users, providing real-time confirmation of successful user additions.
This plan achieves a robust and automated solution for bulk user addition to Google Workspace. This will streamline the user onboarding process, enhance efficiency, and reduce the administrative burden associated with manual operations.
Links
[1] Google Admin SDK API Documentation: https://developers.google.com/admin-sdk
[2] Google Admin SDK API - Creating Users: https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/insert
[3] Google Admin SDK API - Assigning Group Members: https://developers.google.com/admin-sdk/directory/v1/guides/manage-group-members
[4] Admin SDK API with Python — Quickstart: https://developers.google.com/admin-sdk/directory/v1/quickstart/python
