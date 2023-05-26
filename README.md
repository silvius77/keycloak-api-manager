# KeycloakAPIManager
API for Keycloak management
<br/>


**CLIENT_ID** = "test_client_name" <br/>
**REALM_NAME** = "realm_name" <br/>
**CLIENT_SECRET** = "40j32-5860-4d79-ad16-9c39897w083" <br/>
**USERNAME** = "username@gmail.com"   - User name with admin's rules <br/> 
**PASSWORD** = "f232@3s456S#422" <br/>
**SERVER_URL** = "http://localhost:8080/auth/" - url keykcloak server <br/>
<br/>


# Installation

```pip install keycloak-api-manager```

# Example
### Create it
Create a file ```main.py``` with:
```
from keycloak_api_manager import KeycloakAPIManager

CLIENT_ID = "test_client_name"
REALM_NAME = "realm_name"
CLIENT_SECRET = "40j32-5860-4d79-ad16-9c39897w083"
USERNAME = 'username@gmail.com'                         # KEYCLOAK user's USERNAME or EMAIL User with admin's
PASSWORD = 'f232@3s456S#422'
SERVER_URL = "http://localhost:8080/auth/"              # KEYCLOAK URL http://localhost:8080/auth/ or
                                                        # http://server_url/auth/


keycloak_api = KeycloakAPIManager(keycloak_url=SERVER_URL, realm_name=REALM_NAME,
                           client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                           admin_username=USERNAME, admin_password=PASSWORD)

about_me = keycloak_api.get_info_about_me()
print(about_me)
```

### Run it
Run a file: ```python keycloak_test.py```

<br/>

___

### Create user


Method **Create_user** with parameter _**payload**_  <br/>
    `create_user(payload=payload)`<br/>

    payload = {
        "username": "some_user",
        "attributes": {"phoneNumber": "1234567890"}, # optional field 
        "enabled": True,
        "credentials": [{"temporary": False, "value": "raw_password"}]
    }

### Editing user


Method **Update_user** with parameter _**payload**_ and  **_user_id_** <br/>
    `update_user(payload=payload_update, user_id="090798-bdaf-4bfb-969b-efc862eaa")`<br/>

    payload_update = {
        "attributes": {
            "phoneNumber": "1234567890",
            "testKey": "testValue"
        }
    }


____

### All functions see on page [Documentation](https://github.com/martinlauren55/keycloakAPI/blob/main/DOCS/DOCS.md)
