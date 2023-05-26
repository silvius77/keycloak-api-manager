import json
import requests


class KeycloakAPIManager:
    def __init__(self, keycloak_url, realm_name, client_id, client_secret, admin_username, admin_password):
        """
        :param keycloak_url: KEYCLOAK URL (http://localhost:8080/auth/, or http://server_url/auth/)
        :param realm_name: KEYCLOAK REALM NAME
        :param client_id: KEYCLOAK CLIENT NAME
        :param client_secret: KEYCLOAK CLIENT SECRET
        :param admin_username: KEYCLOAK user's USERNAME or EMAIL User with admin's
        :param admin_password: KEYCLOAK user's PASSWORD
        """
        self._keycloak_url = keycloak_url
        self._realm_name = realm_name
        self._client_id = client_id
        self._client_secret = client_secret
        self._admin_username = admin_username
        self._admin_password = admin_password

        self._access_token = self._get_access_token()['access_token']

    def _get_access_token(self):
        url = f"{self._keycloak_url}realms/{self._realm_name}/protocol/openid-connect/token"
        payload = {"username": self._admin_username, "password": self._admin_password, "grant_type": "password",
                   "client_id": self._client_id, "client_secret": self._client_secret}
        return requests.post(url=url, data=payload).json()

    def get_info_about_me(self):
        """
        :return: KEYCLOAK USER INFORMATION
        """
        url = f"{self._keycloak_url}realms/{self._realm_name}/protocol/openid-connect/userinfo"
        headers = {"Authorization": "Bearer " + self._access_token}
        return requests.get(url=url, headers=headers).json()

    def get_detailed_info_about_me(self):
        """
        :return: KEYCLOAK USER DETAILED INFORMATION
        """
        url = f"{self._keycloak_url}realms/{self._realm_name}/protocol/openid-connect/token/introspect"
        payload = {"token": self._access_token, "client_id": self._client_id, "client_secret": self._client_secret}
        return requests.post(url=url, data=payload).json()

    def get_realm_users(self, first: int, last: int, max_count=100):
        """
        :param first Pagination offset
        :param last Pagination offset
        :param max_count Maximum results size (defaults to 100)
        :return: list of realm users
        """
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}/users/?first={first}&last={last}&max={max_count}"
        headers = {"Authorization": "Bearer " + self._access_token}
        return requests.get(url=url, headers=headers).json()

    def get_realm_users_count(self):
        """
        :return: number of realm users
        """
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}/users/count"
        headers = {"Authorization": "Bearer " + self._access_token}
        return requests.get(url=url, headers=headers).json()

    def get_user(self, user_id: str):
        """
        :param user_id: KEYCLOAK ID
        :return: info about user
        """
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}/users/{user_id}"
        headers = {"Authorization": "Bearer " + self._access_token}
        return requests.get(url=url, headers=headers).json()

    def add_or_update_user_attributes(self, attributes: dict, user_id: str) -> bool:
        """
        :param attributes: {'key1': 'value1', 'key2': 'value2'}
        :param user_id: KEYCLOAK USER ID
        :return: bool
        """
        attr = dict()
        for k, v in self.get_user_attributes(user_id=user_id).items():
            attr[k] = v[0]
        for k, v in attributes.items():
            attr[k] = v
        return self.update_user(payload={"attributes": attr}, user_id=user_id)

    def delete_user_attributes(self, attributes: list, user_id: str) -> bool:
        """
        :param attributes:  list -> ['phone', 'newTest']
        :param user_id: KEYCLOAK USER ID
        :return: bool
        """
        attr = dict()
        for k, v in self.get_user_attributes(user_id=user_id).items():
            attr[k] = v[0]
        for key in attributes:
            del attr[key]
        return self.update_user(payload={"attributes": attr}, user_id=user_id)

    def get_user_attributes(self, user_id: str):
        """
        :parame user_id: KEYCLOAK ID
        :return: KEYCLOAK USER attributes
        """
        user = self.get_user(user_id=user_id)
        if "attributes" in user:
            user_attr = {}
            for k, v in user.get('attributes').items():
                user_attr[k] = v[0]
            return user_attr
        else:
            return None

    def get_realm_clients(self) -> dict:
        """
        :return: realm clients
        """
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}/clients"
        headers = {"Authorization": "Bearer " + self._access_token}
        return requests.get(url=url, headers=headers).json()

    def create_user(self, payload: dict) -> bool:
        """
        :param payload: Dict with params {"username": "some_user", "enabled": True,
        "credentials": [{"temporary": False, "value": "raw_password"}]}
        :return: bool
        """
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}/users"
        headers = {"Authorization": "Bearer " + self._access_token, "Content-Type": "application/json",
                   "Accept": "application/json"}
        response = requests.post(url=url, headers=headers, data=json.dumps(payload))

        if response.status_code == 201:
            return True
        else:
            raise Exception(response.text)

    def create_identity_provider_links_for_user(self, provider_identity: str, provider_user_id: str,
                                                provider_username: str, user_id: str) -> bool:
        """
        :param provider_identity: Identity Provider Alias (from method get_identity_providers)
        :param provider_user_id: Provider User ID
        :param provider_username: Provider Username
        :param user_id: KEYCLOAK USER ID
        :return:
        """
        payloadd = {"identityProvider": provider_identity, "userId": provider_user_id,
                    "userName": provider_username}
        url = f'{self._keycloak_url}admin/realms/{self._realm_name}/' \
              f'users/{user_id}/federated-identity/{provider_identity}'
        headers = {"Authorization": "Bearer " + self._access_token,
                   "Content-Type": "application/json",
                   "Accept": "application/json"}
        response = requests.post(url=url, headers=headers, data=json.dumps(payloadd))

        if response.status_code == 204:
            return True
        else:
            raise Exception(response.text)

    def get_identity_providers(self):
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}"
        headers = {"Authorization": "Bearer " + self._access_token}
        response = requests.get(url=url, headers=headers).json()
        providers = []
        for i in response['identityProviders']:
            providers.append(i['alias'])
        return providers

    def update_user(self, payload, user_id: str) -> bool:
        """
        :param payload:
        :param user_id: KEYCLOAK ID
        :return: bool
        """
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}/users/{user_id}"
        headers = {"Authorization": "Bearer " + self._access_token, "Content-Type": "application/json",
                   "Accept": "application/json"}
        response = requests.put(url=url, headers=headers, data=json.dumps(payload))
        if response.status_code == 204:
            return True
        else:
            raise Exception(response.text)

    def delete_user(self, user_id: str) -> bool:
        """
        :param user_id: KEYCLOAK ID
        :return: bool
        """
        url = f"{self._keycloak_url}admin/realms/{self._realm_name}/users/{user_id}"
        headers = {"Authorization": "Bearer " + self._access_token, "Content-Type": "application/json",
                   "Accept": "application/json"}
        response = requests.delete(url=url, headers=headers)
        if response.status_code == 204:
            return True
        else:
            raise Exception(response.text)
