

import requests
import sys

ENVIRONMENT = "stage"

project_key = "smart-assistant"
feature_flag_key = "code-freeze"
url = "https://app.launchdarkly.com/api/v2/flags/" + project_key + "/" + feature_flag_key
headers = {"Authorization": sys.argv[1:]}

response = requests.get(url, headers=headers)

data = response.json()
if data["environments"][ENVIRONMENT]["on"]:
    raise Exception(f"There is a code freeze in {ENVIRONMENT}. Merging new code is currently not permitted.")