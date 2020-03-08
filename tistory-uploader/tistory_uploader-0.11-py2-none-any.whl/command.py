import tistory_api
import click
import os
import user_info
from pathlib import Path
import json

FILE_NAME = 'user.json'

@click.command()
def init():

    is_exist = os.path.isfile(FILE_NAME)
    if is_exist:
        os.popen('code {name}'.format(name=FILE_NAME))
        return

    with open(FILE_NAME, "w") as json_file: 
        json_file.write(json.dumps({
            "blog_name": "",
            "client_id": "",
            "client_secret": "",
            "access_token": "",
            "categories": []
        }, indent = 4)) 

    os.popen('code {name}'.format(name=FILE_NAME))

@click.command()
def token():
    tistory_api.getAccessToken()
    return

@click.command()
def category():
    response = tistory_api.getCategories()
    data = json.loads(response.text)
    categories = data['tistory_api']['item']['categories']
    my_categories = []
    for c in categories:
        a = {}
        for key in c.keys():
            if key == 'id' or key == 'name':
                a[key] = c[key] 
            
        my_categories.append(a) 

    user_info.write_categories(my_categories)
    return

@click.command()
@click.argument('file')
@click.option('-cg', '--category', help="카테고리 이름 입력")
def write(category, file):
    f = open(file, "r")

    req = {
        'title': os.path.basename(f.name).split('.')[0], 
        'content':f.read(),
    }

    if category == None:
        tistory_api.writePost(req)
        return

    try:
        categoryId = user_info.get_category_id_by_name(category)
        req['category'] = categoryId
        tistory_api.writePost(req)
    except:
        print('카테고리 정보를 확인해주세요. (user.json)')

@click.command()
@click.argument('id', nargs=-1)
@click.argument('file', nargs=1)
@click.option('-cg', '--category', help="카테고리 이름 입력")
def modify(category, id, file):
    f = open(file, "r")

    req = {
        "postId": id,
        'title': os.path.basename(f.name).split('.')[0], 
        'content':f.read(),
    }

    if category == None:
        tistory_api.modifyPost(req)
        return

    try:
        categoryId = user_info.get_category_id_by_name(category)
        req['category'] = categoryId
        tistory_api.modifyPost(req)
    except:
        print('카테고리 정보를 확인해주세요. (user.json)')

# ---------------------------------------------------------

@click.group()
def cli():
    pass

cli.add_command(init)
cli.add_command(category)
cli.add_command(token)
cli.add_command(write)
cli.add_command(modify)

if __name__ == '__main__':
    cli()