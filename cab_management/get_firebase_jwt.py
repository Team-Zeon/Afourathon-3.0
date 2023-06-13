import firebase_admin
from firebase_admin import credentials, auth
import requests
from firebase_admin import exceptions

service_account_key_path = "afourathon_key.json"
api_key = "AIzaSyBrvFPjUThqCEb7nHpgn-EI2FrE2rooQKk"

cred = credentials.Certificate(service_account_key_path)
firebase_admin.initialize_app(cred)


def login_with_firebase(email, password):
    try:
        user = auth.get_user_by_email(email)
        custom_token = auth.create_custom_token(
            user.uid,
            app=firebase_admin.get_app(),
        )
        response = requests.post(
            "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key="
            + api_key,
            json={"email": email, "password": password, "returnSecureToken": True},
        )
        if response.status_code == 200:
            id_token = response.json()["idToken"]
            return id_token
        else:
            print("Failed to authenticate with Firebase:", response.text)
    except exceptions.FirebaseError as e:
        print("Firebase authentication error:", e)
    except Exception as e:
        print("Error occurred:", e)


email = "example@example.com"
password = "example_password"

jwt_token = login_with_firebase(email, password)
print("JWT Token:", jwt_token)

# with open("jwt_token.txt", "w") as f:
#     f.write(jwt_token)
