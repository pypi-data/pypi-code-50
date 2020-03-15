
import getpass


def get_credits( user=None ):
    
    user_login = getpass.getuser() if user is None or len(user)==0 else user

    user_name = input(f"enter github user [{user_login}]: ").strip()
    if len(user_name) == 0:
        user_name = user_login
        
    while True:
        user_password = getpass.getpass("enter github password (deprecated) or personal access token: ").strip()
        if len(user_password)>0:
            break

    return ( user_name, user_password )

