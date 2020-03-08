import requests

MARKDOWN_CONVERT_API = 'https://api.github.com/markdown/raw'
HEADER = {'Content-Type': 'text/plain; charset=utf-8'}

def toHtmlFromMarkdown(markdown):
    response = requests.post(MARKDOWN_CONVERT_API, data=markdown.encode('utf-8'), headers=HEADER)
    return '<div class="markdown-body"> {content} </div>'.format(content=response.text)