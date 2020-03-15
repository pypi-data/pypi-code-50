# -*- coding=utf-8 -*-
import os
from datetime import date
from flask import current_app, jsonify, request, send_from_directory, url_for
from flask_login import login_required
from flask_ckeditor import upload_fail, upload_success

from xp_cms.utils import allowed_file, rename_image, resize_image, upload_thumb, upload_image
from .. import course_module


@course_module.route('/uploads/<path:filename>')
def get_image(filename):
    print("-"*10)
    print(filename)
    return send_from_directory(current_app.config['COURSE_UPLOAD_PATH'], filename)


@course_module.route('/upload', methods=['POST'])
@login_required
def course_upload_image():
    filename = upload_image('COURSE')
    url = url_for('.get_image', filename=filename[0])
    return upload_success(url, filename[0])


@course_module.route('/upload_thumb', methods=['GET', 'POST'])
@login_required
def course_upload_thumb():
    filenames = upload_thumb('COURSE')
        # photo = Photo(
        #     filename=filename,
        #     filename_s=filename_s,
        #     filename_m=filename_m,
        #     author=current_user._get_current_object()
        # )
        # db.session.add(photo)
        # db.session.commit()
    return jsonify({"file": filenames[0]})
