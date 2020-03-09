import os
import codecs

import cherrypy
from markdown import markdown
import pystache

# from slickwiki.templates import *

class WikiApp(object):
    def __init__(self,
                 path,
                 config,
                 templates):
        self.init_page_text = config["initPageText"]
        self.port_number = config["portNumber"]
        self.editor_cmd = config["editorCommand"]
        print(self.editor_cmd)
        self.wiki_dir = path
        self.templates = templates

    def ensure_path_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        
    def wrap(self, path, title, content):
        return pystache.render(
            self.templates["wrapper"],
            {"title": title,
             "content": content,
             "path": path})

    def source_path(self, path_elems):
        return os.path.join(self.wiki_dir, *path_elems) + ".md"

    def get_source(self, path_elems):
        with codecs.open(self.source_path(path_elems), "r", "utf-8") as f:
            return f.read()

    def get_title(self, path_elems):
        src = self.get_source(path_elems)
        return src.split("\n")[0].strip()
        
    def get_content(self, path_elems):
        
        md = self.get_source(path_elems)
            
        return markdown(md)

    def edit_page(self, path_elems):
        fn = self.source_path(path_elems)
        path = self.source_path(path_elems[:-1])
        self.ensure_path_exists(path)

        print(pystache.render(self.editor_cmd,
                                  {"path": fn}) + " &")
        os.system(pystache.render(self.editor_cmd,
                                  {"path": fn}) + " &")

    def creating_404(self, path_elems):
        err = cherrypy.HTTPError(404)
        
        def fn(*a, **kw):
            return pystache.render(
                self.templates["not_found_msg"],
                {"path": "/".join(path_elems)}).encode("utf-8")
            
        err.get_error_page = fn

        return err

    @cherrypy.expose
    def favicon(self):
        raise cherrypy.HTTPRedirect("/static/favicon.png")

    def editing_message(self, path_elems):
        return pystache.render(
            self.templates["editing_msg"],
            {"path": "/".join(path_elems)})

    @cherrypy.expose
    def css(self, *args, **kwargs):
        cherrypy.serving.response.headers["Content-Type"] = "text/css"
        return self.templates["css"]
    
    @cherrypy.expose
    def default(self, *args, **kwargs):

        if len(args) == 0:
            raise cherrypy.HTTPRedirect("/index")
        
        elif "edit" in kwargs.keys():
            self.edit_page(args)
            return self.editing_message(args)
        else:  
            try:
                return self.wrap("/".join(args),
                                 self.get_title(args),
                                 self.get_content(args))
            except FileNotFoundError:
                self.edit_page(args)
                raise self.creating_404(args)

    def run(self):
        cherrypy.config.update({"server.socket_port": self.port_number})

        config = {
            "/static": {
                "tools.staticdir.on": True,
                "tools.staticdir.dir": os.path.abspath(os.path.join(self.wiki_dir, "static"))
            },
            "/favicon.ico": {
                "tools.staticfile.on": True,
                "tools.staticfile.filename": os.path.abspath(os.path.join(self.wiki_dir, "static", "favicon.ico"))
            },
        }
        
        cherrypy.quickstart(self, config=config)
