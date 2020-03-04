#!/usr/bin/env python3
import web,sys,os,socket
from os import path
from pathlib import Path
import time
from io import BytesIO
from base64 import b64encode,b64decode
sys.argv.append('8088')
urls = (   
    '/download/.*','download',
    '/.*','FileSystem')
file_render=web.template.render('.',cache=False)

def generate_html(body,dirname):
    html_string1 = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="maximum-scale=1.0,minimum-scale=1.0,user-scalable=no,
    width=device-width,initial-scale=1.0" />
   
'''
    fs1 = '<title>Directory listing for /{dirname}/</title>'
    html_string2='''</head>

<script>
    function change(){  
        document.getElementById("file_name").value=document.getElementById("file_content").value;  
    }  
</script>
<body>
'''
    fs2 = '<h1>Directory listing for /{dirname}/</h1>'
    html_string3 = '''<hr>
<form method="post"  enctype="multipart/form-data">
    <div class="col-sm-4">  
        <button type="button" class="btn btn-primary" id="select_file"  
                onclick="file_content.click();">Scan file  
        </button>  
        <input type="file" class="form-control" id="file_content" name="file_content"  
               style="display: none;" onchange="change();">  
        <input type="text" class="form-control" id="file_name" name="file_name"  
               readonly="readonly" onclick="file_content.click(); ">  
        <input type="submit" value="Submit file" />
    </div>  
</form>
</hr>
<hr>
<form method="post"  enctype="multipart/form-data">
    <div class="col-sm-4">  
        <input type="submit" value="Submit file" /></br>
        <ul>
    '''
        # $for i,j in body:
    # fs3 = '     <label><input name="{i}" type="checkbox" value=""/><a href="{i}">{j}</a></label> </br>\n'
    fs3 = '     <li><a href="{j}">{i}</a></li>\n'
    html_string4='''    </ul>
</div>  
</form>
</hr>
</body>
</html>
'''
    html_bytes = BytesIO()
    html_bytes.write(html_string1.encode('utf8'))
    html_bytes.write(fs1.format(dirname = dirname).encode('utf8'))
    html_bytes.write(html_string2.encode('utf8'))
    html_bytes.write(fs2.format(dirname = dirname).encode('utf8'))
    html_bytes.write(html_string3.encode('utf8'))
    a = [fs3.format(i=i,j=j) for i,j in body]
    html_bytes.write(''.join(a).encode('utf8'))
    html_bytes.write(html_string4.encode('utf8'))
    length = html_bytes.tell()
    html_bytes.seek(0,0)
    web.header('Content-Type','text/html')
    web.header('Content-Length',str(length))
    return html_bytes


def encode(url):
    return url
    # return b64encode(url.encode('utf8')).decode('utf8')
def decode(url):
    return url
    # return b64decode(url.encode()).decode('utf8')
class FileSystem:
    def GET(self,*d):
        url=web.url()
        url=decode(url)
        print(url)
        url = '.'+url
        url_path = Path(url)
        print(url_path)
        if url_path.is_dir():
            p=url
            if p[-1] != '/':
                raise web.seeother(url[1:]+'/')
        else:
            if url.endswith('mp4'):
                raise web.seeother('/download/file?f1='+encode(url))
            return send_file(url)
        x=os.listdir(p)
        index_file = url_path / 'index.html'
        if index_file.is_file():
            return send_file(str(index_file))
        a=[]
        for i in x:
            filename=p+i
            if path.isfile(filename):
                a.append([i,i])
            else:
                a.append([i+os.sep,i+os.sep])
        a.sort(key=lambda x:x[1][-1])
        for i in a:
            i[0]=encode(i[0])
        return generate_html(a,url_path.name)
        # return file_render.file(a,path.split(p[:-1])[1])

def send_file(filename):
    if not path.exists(filename):
        return None
    ct = web.ctx.env.get('CONTENT_TYPE')
    if ct is None:
        suffix = Path(filename).suffix.lower()
        if suffix == '.html':
            ct = 'text/html'
        elif suffix == '.js':
            ct = 'text/javascript'
        elif suffix == '.css':
            ct = 'text/css'
        elif suffix == '.mp4':
            ct = 'video/mp4'
        else:
            ct = 'application/octet-stream'
    web.header('Content-Type',ct)
    web.header('Content-Length',str(path.getsize(filename)))
    return open(filename,'rb')
    

def download_file(fp,length,file_name='package'):
    BUF_SIZE=1024*1024
    try:
        ct = web.ctx.env.get('CONTENT_TYPE')
        if ct is None:
            suffix = Path(file_name).suffix.lower()
            if suffix == '.html':
                ct = 'text/html'
            elif suffix == '.js':
                ct = 'text/javascript'
            elif suffix == '.css':
                ct = 'text/css'
            elif suffix == '.mp4':
                ct = 'video/mp4'
            else:
                ct = 'application/octet-stream'
        
        web.header('Content-Type',ct)
        web.header('Content-disposition', 'attachment; filename={name}'.format(name=file_name))
        
        # Content-Range: bytes 2293762-3342338/145108958
        start = 0
        hrange = web.ctx.env.get('HTTP_RANGE')
        if hrange:
            web.ctx.status = '206 PartialContent'
            ipos = int(hrange[6:-1])
            fp.seek(ipos,0)
            start = ipos
        fs = 'bytes {}-{}/{}'
        while True:
            
            c = fp.read(BUF_SIZE)
            if c:
                end = start + BUF_SIZE
                web.header('Content-Range',fs.format(start,end,length))
                start = end
                yield c
            else:
                break
    except Exception as err:
        print(err)
        yield 'Error'
    finally:
        if fp:
            fp.close()

class download:
    def GET(self):
        t=web.input()
        file_list=list(t.values())
        url=file_list[0]
        file_name=decode(url)
        f = open(file_name, "rb")
        length=path.getsize(file_name)
        for i in download_file(f,length,path.basename(file_name)):
            yield i
def getip():
    return socket.gethostbyname(socket.gethostname())
def website():
    app=web.application(urls, globals ())
    app.run()
if __name__ == '__main__': 
    x=getip()
    print('本机ip：{ip}'.format(ip=x))
    print(sys.path[0])
    website()
    
