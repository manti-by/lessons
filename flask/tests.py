import json
import requests

from faker import Faker

fake = Faker()


if __name__ == "__main__":
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200

    response = requests.get("http://127.0.0.1:5000/user/")
    assert response.status_code == 200

    headers = {"Content-Type": "application/json"}
    data = {"email": fake.email(), "password": fake.word()}
    response = requests.post("http://127.0.0.1:5000/user/", data=json.dumps(data), headers=headers)
    assert response.status_code == 201

    print("All tests have passed")
