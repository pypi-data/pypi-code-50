import open_detection as od

# dataset = od.dataset.coco.COCODataSet("/home/killf/data/数据集/mscoco")
# while True:
#     for data in dataset:
#         print(data)

anchors = od.anchor.generate_anchors(img_size=550,
                                     feature_map_size=[69, 35, 18, 9, 5],
                                     aspect_ratio=[1, 0.5, 2],
                                     scale=[24, 48, 96, 192, 384])

reader = od.dataset.coco.train("/home/killf/data/数据集/mscoco",
                               anchors=anchors,
                               num_workers=2,
                               batch_size=4,
                               max_queue=8,
                               total_iter=100,
                               use_multiprocess_reader=False)
for data in reader():
    print(data.get("image").shape)
