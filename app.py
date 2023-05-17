from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import markdown
from notion_data import push2notion

app = Flask(__name__)
CORS(app, resource={r"/*": {'origins': 'https://chat.openai.com'}})
DATA_HOST = "http://127.0.0.1:5001"
# DATA_HOST = 'https://gpt-2-notion--liompei.repl.co'
# DATA_HOST = 'https://<YOUR_REPO>--<YOUR_OWNER>.repl.co'

user_data = {}


@app.route('/notion/add/<string:username>', methods=['POST'])
def add_notion(username):
    openai_conversation_id = request.headers.get('Openai-Conversation-Id')

    if openai_conversation_id not in user_data:
        return 'not set notion key for this user', 400

    user = user_data[openai_conversation_id]
    notion_integration = user['notion_integration']
    database_id = user['database_id']

    request_data = request.get_json(force=True)
    print(request_data)
    user_content = request_data['user_content']
    assistant_content = request_data['assistant_content']
    description = request_data['description']
    print(user_content)
    print(assistant_content)
    print(description)

    notion_response = push2notion(
        user_content=user_content,
        assistant_content=assistant_content,
        description=description,
        token=notion_integration,
        database_id=database_id
    )
    if notion_response.status_code == 200:
        return 'OK', 200
    else:
        print(notion_response.text)
        return notion_response.text, notion_response.status_code


@app.route('/notion/primaryData/<string:username>', methods=['POST'])
def set_notion_primary_data(username):
    request_data = request.get_json(force=True)
    print(request_data)
    openai_conversation_id = request.headers.get('Openai-Conversation-Id')
    notion_integration = request_data['notion_integration']
    database_id = request_data['database_id']

    user_data[openai_conversation_id] = {
        'notion_integration': notion_integration,
        'database_id': database_id
    }

    print(user_data)
    return 'OK,now you can push to notion', 200


@app.route('/notion/primaryData/<string:username>', methods=['GET'])
def get_notion_primary_data(username):
    openai_conversation_id = request.headers.get('Openai-Conversation-Id')
    if openai_conversation_id not in user_data:
        return 'Invalid Openai-Conversation-Id', 401
    user = user_data[openai_conversation_id]
    notion_integration = user['notion_integration']
    database_id = user['database_id']

    return jsonify(notion_integration, database_id), 200


@app.route('/logo.png', methods=['GET'])
def plugin_logo():
    print('plugin_logo ')
    return send_file('logo.png', mimetype='image/png')


@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def plugin_manifest():
    host = request.headers['Host']
    print('plugin_manifest ' + host)
    with open('./.well-known/ai-plugin.json') as f:
        text = f.read()
        text = text.replace("PLUGIN_HOSTNAME", DATA_HOST)
        return text, 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/openapi.yaml', methods=['GET'])
def openapi_spec():
    host = request.headers['Host']
    print('openapi ' + host)
    with open('openapi.yaml') as f:
        text = f.read()
        text = text.replace("PLUGIN_HOSTNAME", DATA_HOST)
        return text, 200, {'Content-Type': 'text/yaml; charset=utf-8'}


@app.route('/')
def hello_world():  # put application's code here
    host = request.headers['Host']
    print('index ' + host)

    with open('README.md', 'r') as f:
        markdown_content = f.read()
        html_content = markdown.markdown(markdown_content)
    centered_html_content = f'<div style="max-width: 60vw; margin: 0 auto;">{html_content}</div>'
    return centered_html_content


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
