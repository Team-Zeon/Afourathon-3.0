import firebase_admin
from firebase_admin import credentials, auth

service_account_key_path = "afourathon_key.json"

cred = credentials.Certificate(service_account_key_path)
firebase_admin.initialize_app(cred)


def verify_user_token(token):
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token["uid"]
    return uid
