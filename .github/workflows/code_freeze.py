import requests
import os

LD_API_KEY = os.getenv("LD_API_KEY")
if not LD_API_KEY:
    raise Exception(
        f"The 'LD_API_KEY' environment variable has not been setup, has expired or was revoked in GH Secrets."
    )

ENVIRONMENT = os.getenv("BRANCH")
if not ENVIRONMENT:
    raise Exception(f"The 'ENVIRONMENT' environment variable was not set.")

ACCEPTED_ENVIRONMENTS = ["dev", "stage"]
if not ENVIRONMENT in ACCEPTED_ENVIRONMENTS:
    raise Exception(
        f"The 'ENVIRONMENT' environment variable is not one of the allowed values. Accepted: {ACCEPTED_ENVIRONMENTS}"
    )

URL = "https://app.launchdarkly.com/api/v2/flags/smart-assistant/code-freeze"
headers = {"Authorization": LD_API_KEY}
response = requests.get(URL, headers=headers)

data = response.json()
if data["environments"][ENVIRONMENT]["on"]:
    raise Exception(
        f"There is a code freeze in {ENVIRONMENT}. Merging new code is currently not permitted."
    )
