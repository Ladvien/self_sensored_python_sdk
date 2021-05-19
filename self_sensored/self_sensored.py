import requests

LOGIN = "/login"
CREATE_USER = "/user"
GET_USER = "/user"
ADD_DEVICE = "/device"
ADD_NATIVE_DESCRIPTION = "/native-description"
ADD_OBSERVATION_CONTEXT_DETAIL = "/observation/context/detail"


class SelfSensored:

    session = {}

    def __init__(self, host: str, port: int = 8080):
        self.host = f"{host}:{port}"
        print(self.host)

    def _get_auth_header(self):
        if "token" not in self.session:
            raise Exception("Must login first.")
        return {
            "Authorization": "Bearer " + str(self.session["token"]),
        }

    def login(self, username: str, password: str) -> dict:
        data = {"email": username, "password": password}
        response = requests.post(self.host + LOGIN, json=data)
        if response.status_code == 200:
            self.session = response.json()
            return self.session
        try:
            return response.json()
        except:
            return {"error": "Unknown error."}

    def add_native_descriptor(
        self, platform: str, name: str, datatype: str, description: str, link: str
    ) -> int:
        data = {
            "platform": platform,
            "name": name,
            "datatype": datatype,
            "description": description,
            "link": link,
        }

        response = requests.post(
            self.host + ADD_NATIVE_DESCRIPTION, json=data, headers=self._get_auth_header()
        )

        try:
            return response.json()
        except Exception as e:
            return { "error": e }

    def add_observation_context_details(
        self,
        action: str,
        type: str,
        description: str,
        url: str,
        unit: str,
        unit_description: str,
        native_description_id=None,
    ) -> dict:

        data = {
            "action": action,
            "type": type,
            "description": description,
            "url": url,
            "unit": unit,
            "unit_description": unit_description,
        }

        if native_description_id:
            data["native_description_id"] = native_description_id

        response = requests.post(
            self.host + ADD_OBSERVATION_CONTEXT_DETAIL,
            json=data,
            headers=self._get_auth_header(),
        )

        try:
            return response.json()
        except Exception as e:
            return { "error": e }