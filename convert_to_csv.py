import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse('results.xml')
root = tree.getroot()

data = []
for testsuite in root:
    for testcase in testsuite:
        test_data = {
            'classname': testcase.attrib['classname'],
            'name': testcase.attrib['name'],
            'time': testcase.attrib['time'],
            'status': 'passed'
        }
        for child in testcase:
            if child.tag == 'failure':
                test_data['status'] = 'failed'
        data.append(test_data)

df = pd.DataFrame(data)
df.to_csv('results.csv', index=False)
