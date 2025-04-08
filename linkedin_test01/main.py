import os
from dotenv import load_dotenv
from requests_html import HTMLSession

# Load environment variables from .env file
load_dotenv()

# Get LinkedIn credentials from environment variables
username = os.getenv('LINKEDIN_USERNAME')
password = os.getenv('LINKEDIN_PASSWORD')

# Initialize a session
session = HTMLSession()

# URL for LinkedIn login
login_url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

# Fetch the login page
response = session.get(login_url)

# Extract the CSRF token from the login page
csrf_token = response.html.find('input[name="loginCsrfParam"]', first=True).attrs['value']

# Prepare the login payload
login_payload = {
    'session_key': username,
    'session_password': password,
    'loginCsrfParam': csrf_token
}

# Send the login request
login_response = session.post(login_url, data=login_payload)

# Check if login was successful
if login_response.status_code == 200 and 'feed' in login_response.url:
    print("Login successful")
else:
    print("Login failed")

# Logout
logout_url = 'https://www.linkedin.com/m/logout'
logout_response = session.get(logout_url)

if logout_response.status_code == 200:
    print("Logout successful")
else:
    print("Logout failed")
