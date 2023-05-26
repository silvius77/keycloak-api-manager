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
Run a file: ```main.py```


# All functions

<br/>

## ABOUT ME
___ 


### get_info_about_me
- return USER INFORMATION

_**example:**_

get_info_about_me()

**_output:_**
```
{'email': 'ivan-test@mail.ru',
 'email_verified': False,
 'family_name': 'Ivanovich',
 'given_name': 'Ivan',
 'name': 'Ivan Ivanovich',
 'preferred_username': 'user',
 'sub': '5cb2908f-d623-4fef-9f1b-f454d3aba112'}
```
<br/>

### get_detailed_info_about_me
- return USER DETAILED INFORMATION

_**example:**_

     get_detailed_info_about_me()

**_output:_**

```
{'acr': '1',
 'active': True,
 'allowed-origins': ['http://localhost:8081'],
 'aud': ['realm-management', 'broker', 'account'],
 'azp': 'client_test_name',
 'client_id': 'client_test_name',
 'email': 'ivan-test@mail.ru',
 'email_verified': False,
 'exp': 1685025680,
 'family_name': 'Ivanovich',
 'given_name': 'Ivan',
 'iat': 1685025380,
 'iss': 'http://localhost:8080/auth/realms/myrealm',
 'jti': 'b4b53a34-a2e5-4580-9354-90a7c3334c7c',
 'name': 'Ivan Ivanovich',
 'preferred_username': 'user',
 'realm_access': {'roles': ['offline_access',
                            'default-roles-mymai',
                            'uma_authorization']},
 'resource_access': {'account': {'roles': ['manage-account', 'view-applications', 'view-consent',
                                           'manage-account-links', 'delete-account', 'manage-consent',
                                           'view-profile']},
                     'broker': {'roles': ['read-token']},
                     'realm-management': {'roles': ['view-realm', 'view-identity-providers',
                                                    'manage-identity-providers', 'impersonation',
                                                    'realm-admin', 'create-client', 'manage-users',
                                                    'query-realms', 'view-authorization',
                                                    'query-clients', 'query-users', 'manage-events',
                                                    'manage-realm', 'view-events', 'view-users',
                                                    'view-clients', 'manage-authorization',
                                                    'manage-clients', 'query-groups']}},
 'scope': 'profile email',
 'session_state': '23fb25eb-c847-49d7-80ec-79e9d550a65a',
 'sid': '23fb25eb-c847-49d7-80ec-79e9d550a65a',
 'sub': '5cb2908f-d623-4fef-9f1b-f454d3aba112',
 'typ': 'Bearer',
 'username': 'user'}
```
<br/>

## USER AND USER ATTRIBUTES
___ 

### create_user
**_params:_**  
payload (dict) - ```
{"username": "some_user", "enabled": True, "credentials": [{"temporary": False, 
"value": "raw_password"}]}```

- return bool


_**example:**_

     payload = {
         "username": "some_user",
         "attributes": {"phoneNumber": "1234567890"},  # optional field 
         "enabled": True,
         "credentials": [{"temporary": False, "value": "raw_password"}]
     }
     
     create_user(payload=payload)

**_output:_**
```
True
```
<br/>

### update_user
**_params:_**  
payload (dict) -  ```{'email': 'vasyapup011@gmail.com'}```<br/>
user_id (str) - KEYCLOAK USER ID</br>

- return bool

_**example:**_

    payload = {'email': 'vasyapup011@gmail.com'}

    update_user(payload=payload, user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")
**_output:_**
```
True
```

<br/>

### delete_user
**_params:_**
user_id (str) - KEYCLOAK USER ID</br>

- return bool

_**example:**_

    delete_user(user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")
**_output:_**
```
True
```
<br/>

### get_user
**_params:_**  
user_id (str) - KEYCLOAK ID </br>

- return info about user


_**example:**_

     get_user(user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")

**_output:_**
```
{'access': {'impersonate': True,
            'manage': True,
            'manageGroupMembership': True,
            'mapRoles': True,
            'view': True},
 'attributes': {'testkey': ['testvalue']},
 'createdTimestamp': 1684489339995,
 'disableableCredentialTypes': [],
 'email': 'vasyapup123@gmail.com',
 'emailVerified': False,
 'enabled': True,
 'federatedIdentities': [],
 'firstName': 'Vasya',
 'id': '43f1bd77-effb-4f98-8c22-5ad8145ebf0d',
 'lastName': 'Pupkin',
 'notBefore': 0,
 'requiredActions': [],
 'totp': False,
 'username': 'vasyapup'}
 ```
<br/>


### get_user_attributes
**_params:_**  
user_id (str) - KEYCLOAK ID </br>

- return (dict) user attributes


_**example:**_

     get_user_attributes(user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")

**_output:_**
```
{'testkey': 'testvalue'}
```
<br/>

### add_or_update_user_attributes
**_params:_**  
user_id (str) - KEYCLOAK ID </br>
attributes (dict) - ```{'key1': 'value1', 'key2': 'value2'}```

- return info about user


_**example:**_

     attr= {'key1': 'value1', 'key2': 'value2'}
     
     add_or_update_user_attributes(attributes=attr, 
                                   user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")

**_output:_**
```
True
```

_**next example:**_

re-run function get_user_attributes:

     get_user_attributes(user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")

**_output:_**
```
{'key1': ['value1'], 'key2': ['value2'], 'testkey': ['testvalue']}
```
<br/>

### delete_user_attributes
**_params:_**  
user_id (str) - KEYCLOAK ID </br>
attributes (list) - only keys ``` ['key1', 'key2']```

- return info about user

_**example:**_

     delete_user_attributes(attributes=['key1'], 
                            user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")
**_output:_**
```
True
```

_**next example:**_

re-run function get_user_attributes:

     get_user_attributes(user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")

**_output:_**
```
{'key2': ['value2'], 'testkey': ['testvalue']}
```
<br/>

## REALM
___ 

### get_realm_users_count
- return number of realm users

_**example:**_

    get_realm_users_count()

**_output:_**

```3```

<br/>

### get_realm_users
**_params:_**  
 first (int) - first Pagination offset </br>
 last (int) - Pagination offset</br>
 max_count (int) -  Maximum results size (defaults to 100)</br>
 
- return list of realm users


_**example:**_

     get_realm_users(first=0, last=5)

**_output:_**
```
[{'access': {'impersonate': True,
             'manage': True,
             'manageGroupMembership': True,
             'mapRoles': True,
             'view': True},
  'attributes': {'phoneNumber2': ['1234567890'], 'statistics': ['quality']},
  'createdTimestamp': 1684334724550,
  'disableableCredentialTypes': [],
  'email': 'johndoe@mail.com',
  'emailVerified': False,
  'enabled': True,
  'firstName': 'John',
  'id': '090260ba-bdaf-4bfb-969b-efcf61222eaa',
  'lastName': 'Doe',
  'notBefore': 0,
  'requiredActions': [],
  'totp': False,
  'username': 'testuser'},
 {'access': {'impersonate': True,
             'manage': True,
             'manageGroupMembership': True,
             'mapRoles': True,
             'view': True},
  'createdTimestamp': 1684091405854,
  'disableableCredentialTypes': [],
  'email': 'ivan-test@mail.ru',
  'emailVerified': False,
  'enabled': True,
  'firstName': 'Ivan',
  'id': '5cb2908f-d623-4fef-9f1b-f454d3aba112',
  'lastName': 'Ivanovich',
  'notBefore': 0,
  'requiredActions': [],
  'totp': False,
  'username': 'user'},
 {'access': {'impersonate': True, 'manage': True,  'manageGroupMembership': True, 
             'mapRoles': True, 'view': True},
  'attributes': {'testkey': ['testvalue']},
  'createdTimestamp': 1684489339995,
  'disableableCredentialTypes': [],
  'email': 'vasyapup123@gmail.com',
  'emailVerified': False,
  'enabled': True,
  'firstName': 'Vasya',
  'id': '43f1bd77-effb-4f98-8c22-5ad8145ebf0d',
  'lastName': 'Pupkin',
  'notBefore': 0,
  'requiredActions': [],
  'totp': False,
  'username': 'vasyapup'}]

```

<br/>

### get_realm_clients
- return realm clients

_**example:**_

     delete_user_attributes(attributes=['key1'], 
                            user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")
**_output:_**
```
[{'access': {'configure': True, 'manage': True, 'view': True},
  'adminUrl': 'http://localhost:8081/',
  'alwaysDisplayInConsole': False,
  'attributes': {... most of the content has been cut ...},
  'authenticationFlowBindingOverrides': {},
  'bearerOnly': False,
  'clientAuthenticatorType': 'client-secret',
  'clientId': 'client_test_name',
  'consentRequired': False,
  'defaultClientScopes': ['web-origins', 'profile', 'roles', 'email'],
  'directAccessGrantsEnabled': True,
  'enabled': True,
  'frontchannelLogout': False,
  'fullScopeAllowed': True,
  'id': '8a8998fb-7b16-4447-a1b8-758b6c4f7c64',
  'implicitFlowEnabled': False,
  'nodeReRegistrationTimeout': -1,
  'notBefore': 0,
  'optionalClientScopes': ['address',
                           'phone',
                           'offline_access',
                           'microprofile-jwt'],
  'protocol': 'openid-connect',
  'protocolMappers': [... most of the content has been cut ...],
  'publicClient': False,
  'redirectUris': ['http://localhost:8081/*'],
  'rootUrl': 'http://localhost:8081/',
  'serviceAccountsEnabled': True,
  'standardFlowEnabled': True,
  'surrogateAuthRequired': False,
  'webOrigins': ['http://localhost:8081']},
  
  {'access': {'configure': True, 'manage': True, 'view': True},
    ... most of the content has been cut ...
  },
  {'access': {'configure': True, 'manage': True, 'view': True},
    ... most of the content has been cut ...
   },
  {'access': {'configure': True, 'manage': True, 'view': True},
    ... most of the content has been cut ...
  }
 ]
```
<br/>

## IDENTITY PROVIDERS
___ 

### get_identity_providers

- return Identity Providers list

_**example:**_

    get_identity_providers()
**_output:_**
```
['google', 'facebook']
```


### create_identity_provider_links_for_user
**_params:_**  
provider_identity (str) - Identity Provider Alias (from method _get_identity_providers_)</br>
provider_user_id (str) - Provider User ID</br>
provider_username (str) - Provider Username</br>
user_id (str) - KEYCLOAK USER ID</br>

- return bool

_**example:**_

    create_identity_provider_links_for_user(provider_identity="google",
                                            provider_username="vasya",
                                            provider_user_id="12345678",
                                            user_id="43f1bd77-effb-4f98-8c22-5ad8145ebf0d")

**_output:_**
```
True
```



