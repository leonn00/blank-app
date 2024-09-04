import streamlit as st
import requests

# Input for the authorization code
auth_code = st.text_input("Enter the Authorization Code")

# Button to submit the request
if st.button("Exchange for Tokens"):
    # URL and data for the POST request
    token_url = "https://x2b64v65h7ed-staging.auth.eu-central-1.amazoncognito.com/oauth2/token"
    data = {
        'client_id': '61e315i84cl4ismgop8b9o5sg2',
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': 'https://www.hirebuddy.link/redirect'
    }
    
    # Make the POST request to exchange code for tokens
    response = requests.post(token_url, data=data)
    
    # Display the response
    if response.status_code == 200:
        st.success("Tokens received!")
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")
        st.text(response.text)
