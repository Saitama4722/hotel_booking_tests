import json
from qaseio import QaseApi

# Загрузка конфигурации QASE из файла
with open('qase_config.json') as f:
    config = json.load(f)

# Инициализация API QASE
api = QaseApi(config['apiToken'])
project_code = config['projectCode']
results_file = "results.xml"

# Загрузка результатов тестирования в QASE
response = api.results.create_from_junit(project_code, results_file)
print(response)  # Для проверки ответа от API
