import json
from qaseio import QaseApi

# Загрузка конфигурации из файла qase_config.json
with open('qase_config.json') as f:
    config = json.load(f)

# Инициализация API клиента с использованием API токена
api = QaseApi(config['apiToken'])

# Получение кода проекта из конфигурации
project_code = config['projectCode']

# Указание пути к файлу с результатами тестов
results_file = "results.xml"

# Загрузка результатов тестов в QASE
api.results.create_from_junit(project_code, results_file)
