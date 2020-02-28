import gitlab


url = 'https://gitee.com/'
token = '88537ed7434a95960ebd01a1b6be5682'

gl = gitlab.Gitlab(url, token)


projects = gl.projects.list(owned=True)
# for pro in projects:
#     print(pro.name)
#     hook = pro.hooks.create({'url': 'http://my/action/url?project=' + pro.name, 'push_events': 1})
#     print(hook)

# gl.projects.create({'name': 'project1'})
