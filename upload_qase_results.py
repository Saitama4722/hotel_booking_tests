import json
from qaseio import QaseApi
from qaseio.models import TestRunCreate

# Загрузите конфигурацию
with open('qase_config.json') as f:
    config = json.load(f)

api_token = config['apiToken']
project_code = config['projectCode']
results_file = "results.xml"

# Инициализация API с использованием токена
api = QaseApi(api_token)

# Создание тестового прогона
test_run = TestRunCreate(title="Test Run")
created_run = api.runs.create(project_code, test_run)

# Загрузка результатов из JUnit файла
api.results.create_from_junit(project_code, created_run.id, results_file)
