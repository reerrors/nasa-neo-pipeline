import os
import sys
import json
#nasa-neo-pipeline/tests/python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/src")

from extract import fetch_neo_data as e

data = e('2020-01-01','2020-01-02')

with open('dump.json','w',encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)
    print("Amostra criada com sucesso!")

