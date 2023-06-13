import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin.auth import ExpiredIdTokenError

service_account_key_path = "afourathon_key.json"

cred = credentials.Certificate(service_account_key_path)
firebase_admin.initialize_app(cred)


def verify_user_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token["uid"]
        return decoded_token
    except ExpiredIdTokenError:
        print("Expired token. Please reauthenticate.")
    except Exception as e:
        print("Error occurred:", e)


jwt_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjU0NWUyNDZjNTEwNmExMGQ2MzFiMTA0M2E3MWJiNTllNWJhMGM5NGQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWZvdXJhdGhvbi0zODkyMDQiLCJhdWQiOiJhZm91cmF0aG9uLTM4OTIwNCIsImF1dGhfdGltZSI6MTY4NjU5MzQyNiwidXNlcl9pZCI6Ijd1bjF5VDkwMFVXQVRoTGN5RXI5NTBudm80RDIiLCJzdWIiOiI3dW4xeVQ5MDBVV0FUaExjeUVyOTUwbnZvNEQyIiwiaWF0IjoxNjg2NTkzNDI2LCJleHAiOjE2ODY1OTcwMjYsImVtYWlsIjoiZXhhbXBsZUBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJleGFtcGxlQGV4YW1wbGUuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.wIYOeM3Uqv0kKPuSq5y-d4vhrSH8s1o9JVwoofPXziMdZMiGh0Ocva_6gnkrE0NCmz0vMWjKlftRo1KawnQ1Y-qC8i2wWk_Y0FxADDjlf7bsCkq8D9JqgAhupmBhPFeF6vvt1vjs2V3emRMAgLlkw321xfyDjzw4CJeqUKlC54iJ6WJQIXykT2VWeO2Lb5BbgD_xz8PZupUaSW9dNpbbMMfGR_xkHjETPn0cEgSVbnh4D1ywM5HilC8mN3AAIoDSeODngQr5JDl_aI6XNDuxZHt_NPd_ei6ppHhCg4AXnT_jtjul8wE8YeFOgUOA9HZvEE_ao9iZldBxqw-i3e4Nbw"  # Replace with the actual JWT token

user_id = verify_user_token(jwt_token)
if user_id:
    print("User ID:", user_id)
else:
    print("Invalid token. Failed to verify user.")
