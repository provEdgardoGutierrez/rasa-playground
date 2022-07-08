

import requests
import os

ENVIRONMENT = "stage"

project_key = "smart-assistant"
feature_flag_key = "code-freeze"
url = "https://app.launchdarkly.com/api/v2/flags/" + project_key + "/" + feature_flag_key
LD_API_KEY = os.getenv('LD_API_KEY')
headers = {"Authorization": LD_API_KEY}

response = requests.get(url, headers=headers)

data = response.json()
if data["environments"][ENVIRONMENT]["on"]:
    raise Exception(f"There is a code freeze in {ENVIRONMENT}. Merging new code is currently not permitted.")