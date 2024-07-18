import json
from qaseio import QaseApi

with open('qase_config.json') as f:
    config = json.load(f)

api = QaseApi(config['apiToken'])
project_code = config['projectCode']
results_file = "results.xml"

response = api.results.create_from_junit(project_code, results_file)
print(response)  # Добавьте это для проверки ответа от API
