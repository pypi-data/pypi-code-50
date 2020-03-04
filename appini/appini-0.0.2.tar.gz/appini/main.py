import os
from shutil import copyfile
import fileinput
import io
import shutil

def create(title, website, website_url, org, description):
    #Flutter project create with given information
    os.system("flutter create --project-name='"+title+"' --description='"+description+"' "+website+"")

    #delete old code 
    os.remove(os.getcwd()+"/%s/lib/main.dart" %website)
    shutil.rmtree(os.getcwd()+"/%s/test"%website)

    #write new main.dart
    maindart= open(os.getcwd()+"/%s/lib/main.dart" %website, "w")
    maindartwritelist = ["import 'package:flutter/material.dart';\nimport 'package:flutter/webview_flutter.dart';\nimport 'data.dart';\n\nvoid main() => runApp(MyApp());\n\nclass MyApp extends StatelessWidget { \n  // This widget is the root of your application.\n  @override\n  Widget build(BuildContext context) {\n    return Scaffold(\n      body: WebView(\n        initialUrl: website,\n        javascriptMode: JavascriptMode.unrestricted,\n      ),\n    );\n  }\n}"]
    maindart.writelines(maindartwritelist)

    #add data.dart and change variable
    datadart= open(os.getcwd()+"/%s/lib/data.dart" %website, "w")
    datadartwritelist = ["String title='%s';\n"%title,"String website='%s';"%website_url] 
    datadart.writelines(datadartwritelist)

    #add webview plugin to pubspec.yaml
    with open(website+"/pubspec.yaml",'r') as f:
        get_all=f.readlines()

    with open(website+"/pubspec.yaml",'w') as f:
        for i,line in enumerate(get_all,1):
            if i == 25:
                f.writelines("  webview_flutter:\n\n")
            else:
                f.writelines(line)

    os.system("cd "+ website +" && flutter pub get")
