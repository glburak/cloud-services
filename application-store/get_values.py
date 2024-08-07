import requests
from flask import Flask, jsonify, Response
from ruamel.yaml import YAML
import sys
def getValues(GIT_API_URL,GIT_ACCESS_TOKEN,application_id,application_tag):
    print("selam")
    # GitLab erişim tokenı ve proje bilgileri
    access_token = GIT_ACCESS_TOKEN
    project_id = application_id
    file_path = 'values.yaml'
    tag = application_tag # Dosyanın bulunduğu tag

    # API URL'si
    url = f"{GIT_API_URL}/projects/{project_id}/repository/files/{file_path}/raw?ref={tag}"

    # İstek yapma
    headers = {
        'PRIVATE-TOKEN': GIT_ACCESS_TOKEN
    }
    response = requests.get(url, headers=headers)
    yaml = YAML()
    yaml.preserve_quotes =True
    # Yanıtı kontrol etme ve dosya içeriğini yazdırma
    if response.status_code == 200:
        yaml_content=response.text
        try:
            return Response(yaml_content,mimetype='text/plain;charset=utf-8')
        except yaml.YAMLError as exc:
            print(f"YAML parsing error: {exc}")
            return None
    else:
        print(f"Error: {response.status_code}, {response.text}")
