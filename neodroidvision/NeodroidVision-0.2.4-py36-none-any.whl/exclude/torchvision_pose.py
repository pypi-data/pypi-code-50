#!/usr/bin/env python
# coding: utf-8

# # Simple 2D human pose service using torchvision and zmq.

# ### Initialization


import io
import json
from pathlib import Path

import numpy
import torch
import torchvision
import zmq
from IPython import get_ipython
from PIL import Image, ImageDraw
# Seems to give a slight speedup
from torchvision.models.detection import keypointrcnn_resnet50_fpn
import matplotlib.pyplot as plt

cudnn = torch.backends.cudnn
cudnn.benchmark = True
cudnn.enabled = True

# ### Construct the network and move to GPU

rpn_n = 4
model = keypointrcnn_resnet50_fpn(pretrained=True,
                                  min_size=128,
                                  rpn_pre_nms_top_n_test=rpn_n,
                                  rpn_post_nms_top_n_test=max(1, rpn_n // 2),
                                  box_score_thresh=0.5,
                                  box_detections_per_img=5)
model.eval()
model.cuda()


# ### Convenience functions


def get_preds(img, threshold=.7):
  '''
      Make `img` a tensor, transfer to GPU and run inference.
      Returns bounding boxes and keypoints for each person.
  '''
  with torch.no_grad():
    img_t = torchvision.transforms.ToTensor()(img)
    img_t = img_t.unsqueeze(0)
    if next(model.parameters()).is_cuda:
      img_t = img_t.pin_memory().cuda(non_blocking=True)
    pred = model(img_t)[0]
  boxes = pred['boxes']
  kpts = pred['keypoints']
  box_scores = pred['scores']
  kpt_scores = pred['keypoints_scores']
  idxs = [i for (i, s) in enumerate(box_scores) if s > threshold]
  res = [(boxes[i].cpu().numpy(), kpts[i].cpu().numpy()) for i in idxs]
  return res


def show_preds(img, pred):
  '''
      Draw bounding boxes and keypoints.
  '''
  draw = ImageDraw.Draw(img)
  drawdot = lambda x, y, r=3, fill="red":draw.ellipse((x - r, y - r, x + r, y + r), fill=fill)
  for (box, kpts) in pred:
    for kpt in kpts:
      if kpt[2] == 1:
        drawdot(kpt[0], kpt[1])
    draw.rectangle(((box[0], box[1]), (box[2], box[3])), outline="red", width=2)
  return img


def to_json(preds):
  '''
      Return predictions in JSON format
  '''
  names = ["nose", "left_eye", "right_eye", "left_ear", "right_ear",
           "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
           "left_wrist", "right_wrist", "left_hip", "right_hip",
           "left_knee", "right_knee", "left_ankle", "right_ankle"]
  detections = [k for (_, k) in preds]
  res = []
  for kpts in detections:
    d = {n:k.round().astype(int).tolist() for (n, k) in zip(names, kpts)}
    res.append(d)
  return json.dumps(res)


# ### Tests


def run_p():
  p = Path("/home/heider/Data/PennFudanPed")/'PNGImages'/"PennPed00095.png"
  img = Image.open(p)
  #get_ipython().run_line_magic('timeit', 'get_preds(img, .70)')
  preds = get_preds(img, .70)
  show_preds(img, preds)
  plt.imshow(img)
  plt.show()


# ### ZMQ interface to Unity:


def inference_server(addr, port, callback=None):
  '''
      Start a ZMQ Reply service.
      Receives an image (encoded in some image format, e.g. jpg) and
      returns detections in JSON format.
  '''
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind(f"tcp://{addr}:{port}")

  try:
    while True:
      msg = socket.recv()
      try:
        img = Image.open(io.BytesIO(msg))
        preds = get_preds(img)
        if callback:
          callback(img, preds)
        json_str = to_json(preds)
        print(json_str)
        socket.send(json_str.encode())
      except:
        socket.send("fail".encode())
  except KeyboardInterrupt:
    pass
  finally:
    context.destroy()


def run_ss():
  addr = "10.24.11.87"
  import streamserver

  with streamserver.StreamServer(host=addr,
                                 secret="hack",
                                 ssl=False,
                                 JPEG_quality=70,
                                 fmt='rgb',
                                 nb_output=False) as ss:
    cb = lambda img, preds:ss.set_frame(numpy.array(show_preds(img, preds)))
    inference_server(addr, 8989, cb)


run_p()
# run_ss()
