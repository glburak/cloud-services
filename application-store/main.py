import os
from flask import Flask
from application_list import storeList
from get_values import getValues
from flask_cors import CORS
GIT_API_URL = os.getenv('GIT_API_URL', 'no url') 
GIT_ACCESS_TOKEN = os.getenv('GIT_ACCESS_TOKEN', 'no token') 

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/application/list', methods=['GET'])
def getList(): 
    return storeList(GIT_API_URL,GIT_ACCESS_TOKEN)

@app.route('/application/<application_id>/tag/<application_tag>', methods=['GET'])
def getValuesFile(application_id,application_tag): 
    return getValues(GIT_API_URL,GIT_ACCESS_TOKEN,application_id,application_tag)

#localhost:8080?repositoryUrl=3333&repositoryTag=v2.33&userGroupId=1234 
@app.route('/application', methods=['PUT'])
ef putApplication(): 
    return putValues(GIT_API_URL,GIT_ACCESS_TOKEN)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=os.getenv('SERVE_PORT','8081'))