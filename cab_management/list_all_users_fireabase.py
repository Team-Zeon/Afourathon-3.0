import firebase_admin
from firebase_admin import credentials, auth

service_account_key_path = "afourathon_key.json"

cred = credentials.Certificate(service_account_key_path)
firebase_admin.initialize_app(cred)


def get_all_users():
    try:
        user_list = auth.list_users()
        return user_list.users
    except firebase_admin.exceptions.FirebaseError as e:
        print("Firebase error:", e)
    except Exception as e:
        print("Error occurred:", e)


users = get_all_users()
if users:
    print("Total users:", len(users))
    for user in users:
        print("User ID:", user.uid)
        print("Email:", user.email)
        print("Display Name:", user.display_name)
        print("---")
else:
    print("Failed to retrieve user list.")
