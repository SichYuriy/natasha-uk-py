from flask import Flask
from flask import Response
from flask import request

import json
from api import name_extracting_service
from api import person_extracting_service

app = Flask(__name__)


@app.route('/extract-names-uk', methods=['POST'])
def extract_names_uk():
    articles = json.loads(request.data)
    articles_matches = name_extracting_service.extract_names(articles)
    dto = list(map(lambda matches: matches.as_json, articles_matches))
    return Response(json.dumps(dto), mimetype='application/json')


@app.route('/extract-persons-uk', methods=['POST'])
def extract_persons_uk():
    articles = json.loads(request.data)
    articles_matches = person_extracting_service.extract_persons(articles)
    dto = list(map(lambda matches: matches.as_json, articles_matches))
    return Response(json.dumps(dto), mimetype='application/json')


if __name__ == '__main__':
    app.run()
