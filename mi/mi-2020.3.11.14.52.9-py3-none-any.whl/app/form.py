#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : mi.
# @File         : EmailApp
# @Time         : 2020-03-06 09:41
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import time
import pandas as pd
from typing import Optional
from fastapi import FastAPI, Form, Depends, File, UploadFile
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import \
    RedirectResponse, FileResponse, HTMLResponse, PlainTextResponse
from starlette.status import *

ROUTE = ""
app = FastAPI(
    debug=True,
    openapi_url=f"{ROUTE}/openapi.json",
    docs_url=f"{ROUTE}/docs",
    redoc_url=f"{ROUTE}/redoc",
    swagger_ui_oauth2_redirect_url=f"{ROUTE}/docs/oauth2-redirect"
)


async def parse_my_form(request: Request) -> dict:
    form_data = await request.form()
    return dict(form_data)


@app.post("/my-form-endpoint")
async def my_endpoint(request: Request):
    form_data = await request.form()

    s = dict(form_data)['data'].strip().replace('null', "''")
    data = eval(s)
    df = pd.DataFrame(data[1:], columns=data[0])
    print(df)
    return "post succeed"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/report")
def read_root():
    # return HTMLResponse(content=open("/Users/yuanjie/Desktop/notebook/your_report.html").read())
    return PlainTextResponse(content=open("/Users/yuanjie/Desktop/notebook/your_report.html").read())


@app.get("/reports")
def read_root():
    print(1)
    return FileResponse(path="/Users/yuanjie/Desktop/notebook/your_report.html", filename='downloadName')


from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

# HTMLResponse(content="htmlString")
# HTMLResponse(content=open("/Users/yuanjie/Desktop/notebook/your_report.html").read())
# FileResponse(path="/Users/yuanjie/Desktop/notebook/your_report.html", filename=None) # 等价于上方
# FileResponse(path="./file.txt", filename='downloadName')
# https://fastapi.tiangolo.com/tutorial/background-tasks/

if __name__ == '__main__':
    import os
    import socket

    me = socket.gethostname() == 'yuanjie-Mac.local'

    uvicorn = "uvicorn" if me else "/opt/soft/python3/bin/uvicorn"

    main_file = __file__.split('/')[-1].split('.')[0]

    # --reload测试环境
    os.system(f"uvicorn {main_file}:app --reload --host 0.0.0.0 --port 9000")
