url = "https://us-west2-aiplatform.googleapis.com/v1beta1/projects/309043943411/locations/us-west2/endpoints/5521993685295693824:predict"
import requests
import json
import google.auth
import google.auth.transport.requests

credentials, project_id = google.auth.default(
    scopes=[
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-platform.read-only",
    ]
)
request = google.auth.transport.requests.Request()
credentials.refresh(request)
token = credentials.token
headers = {"Authorization": "Bearer " + token}
data = {
    "instances": [
        [2, 1.0, 202.0, -37.7996, 144.9984],
        [2, 1.0, 156.0, -37.8079, 144.9934],
        [3, 2.0, 134.0, -37.8093, 144.9944],
        [3, 2.0, 94.0, -37.7969, 144.9969],
        [4, 1.0, 120.0, -37.8072, 144.9941],
    ]
}
response = requests.post(url, json=data, headers=headers)
print(response.text)
print("------------------------------")
print(token)
