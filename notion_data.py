import requests
from datetime import date

notion_url = 'https://api.notion.com/v1/pages'


def push2notion(user_content, assistant_content, description, token, database_id):
    headers = {
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'parent': {'database_id': database_id},
        # 'icon': {'emoji': '🍉'},
        # 'cover': {'external': {'url': 'https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg'}},
        'properties': {
            'Name': {'title': [{'text': {'content': user_content}}]},
            'gpt': {'rich_text': [{'text': {'content': description}}]},
            'Date': {'date': {'start': date.today().isoformat()}}
        },
        'children': [
            {
                'object': 'block',
                'type': 'paragraph',
                'paragraph': {
                    'rich_text': [{'type': 'text', 'text': {'content': assistant_content}}]
                }
            },
        ]
    }
    response = requests.post(url=notion_url, headers=headers, json=data)
    return response

