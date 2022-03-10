import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def add_new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
    """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
   запроса и результат в формате JSON с данными добавленного питомца"""

    data = MultipartEncoder(
        fields={
            'name': name,
            'animal_type': animal_type,
            'age': age
        })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

    res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result
