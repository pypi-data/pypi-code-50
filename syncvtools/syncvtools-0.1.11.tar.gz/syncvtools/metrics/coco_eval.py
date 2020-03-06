'''
Based on tsungyi version of COCOeval github library
'''
from collections import OrderedDict
from typing import List, Tuple, Any, Dict, Optional, Union
from syncvtools.utils.bbox import iou_run
import warnings
import numpy as np
import datetime
#can't import that because of a loop
#from syncvtools.data.detections import DetectionEntity, DetectionsCollection,
import logging





class COCOParams:
    iouThr = 0.1
    maxDet = 100
    recThrs = np.linspace(.0, 1.00, np.round((1.00 - .0) / .01) + 1, endpoint=True)
    faThrs = np.concatenate((np.linspace(.0, .02, 21, endpoint=True), np.linspace(.03, .1, 8, endpoint=True)),axis=0)

def evaluate_img(dts_all: List, gts_all: List, cat_label: str) -> Optional[Dict[str, Any]]:
    '''
    Function that evaluates set of detections / gt for one image.
    :param dts_all: [{'score': 0.3333,'area':w*h, 'bbox': [1.1,2.2,3.3,4.4]},'id':]
    :param gts_all: [{'ignore':0, 'area':w*h,'bbox': [1,2,3,4]},'id':]
    :param cat_label: category name, i.e. 'sharp'
    :return:
    '''

    for i,dt in enumerate(dts_all):
        if dt.label_text != cat_label:
            continue
        dt.area = (dt.bbox.bbox_abs[2] - dt.bbox.bbox_abs[0]) * (dt.bbox.bbox_abs[3] - dt.bbox.bbox_abs[1])
        dt.id = i+1

    for i, gt in enumerate(gts_all):
        if gt.label_text != cat_label:
            continue
        gt.area = (gt.bbox.bbox_abs[2] - gt.bbox.bbox_abs[0]) * (gt.bbox.bbox_abs[3] - gt.bbox.bbox_abs[1])
        gt.id = i+1
        gt.ignore = 0 #keep for future use

    dts = []
    gts = []
    for dt in dts_all:
        if dt.label_text == cat_label:
            dts.append(dt)

    for gt in gts_all:
        if gt.label_text == cat_label:
            gts.append(gt)

    gt_bboxes = [gt.bbox.bbox_abs for gt in gts]
    inds = np.argsort([-d.score for d in dts], kind='mergesort')
    dt_bboxes = [dt.bbox.bbox_abs for dt in dts]
    dt_bboxes = [dt_bboxes[i] for i in inds]

    gt_bboxes = np.asarray(gt_bboxes).reshape(-1, 4)
    dt_bboxes = np.asarray(dt_bboxes).reshape(-1, 4)

    ious = iou_run(dt_bboxes, gt_bboxes)

    if len(gts) == 0 and len(dts) == 0:
        return None

    # sort dt highest score first, sort gt ignore last
    #gtind = np.argsort([g._ignore for g in gts], kind='mergesort')
    #gt = [gts[i] for i in gtind]
    gt = gts
    dtind = np.argsort([-d.score for d in dts], kind='mergesort')
    dt = [dts[i] for i in dtind[0:COCOParams.maxDet]]

    G = len(gt)
    D = len(dt)
    gtm = np.zeros((G,))
    dtm = np.zeros((D,))

    if not len(ious) == 0:
        t = COCOParams.iouThr
        for dind, d in enumerate(dt):
            # information about best match so far (m=-1 -> unmatched)
            iou = min([t, 1 - 1e-10])
            m = -1
            for gind, g in enumerate(gt):
                # if this gt already matched, and not a crowd, continue
                if gtm[gind] > 0:
                    continue

                # continue to next gt unless better match made
                if ious[dind, gind] < iou:
                    continue
                # if match successful and best so far, store appropriately
                iou = ious[dind, gind]
                m = gind
            # if match made store id of match for both dt and gt
            if m == -1:
                continue
            dtm[dind] = gt[m].id
            gtm[m] = d.id

    # store results for given image and category
    return {
        'category_name': cat_label,
        'dtIds': [d.id for d in dt], #ids of all dt boxes, corresponds to dtMatches
        'gtIds': [g.id for g in gt], #ids of all gt boxes, corresponds to gtMatches
        'dtMatches': dtm, # shape: [gtId for each dt box]
        'gtMatches': gtm, # shape: [dtId  for each gt box]
        'dtScores': [d.score for d in dt],
    }



def accumulate(data_src: Any, cat_ids: list) -> Dict[str, Any]:
    '''
    Accumulates results obtained by evaluateImg across all images in dataset.
    :param data_src: either 1) dict with keys=labels, when data comes from single Image
    2) just list of data provided. Mostly manual use.
    3) Common case - DetectionsCollection, meaning dict with keys = img_ids.
    :param cat_ids:
    :return:
    '''
    if not data_src:
        raise ValueError("Detection collection is empty")
    # allows input customized parameters
    R = len(COCOParams.recThrs)
    FA_ruler_size = len(COCOParams.faThrs)
    K = len(cat_ids)

    precision = np.full((R, K), np.nan) #-np.ones((T, R, K, A, M))  # -1 for the precision of absent categories
    recall = np.full((K,), np.nan)#-np.ones((T, K, A, M))
    scores = np.full((R, K), np.nan) #-np.ones((T, R, K, A, M))
    recall_by_fa = np.full((FA_ruler_size, K), np.nan)
    conf_by_fa = np.full((FA_ruler_size, K), np.nan)

    for label_i, label_text in enumerate(cat_ids):  # by category
        if isinstance(data_src, dict): #for one image only
            E = [data_src[label_text]]
        elif isinstance(data_src, list): #for provided list
                E = [per_img[label_text] for per_img in data_src]
        elif isinstance(data_src, DetectionsCollection): #for DetectionCollection
            E = []
            for img_key in data_src:
                if not data_src[img_key].detection_evaluation:
                    logging.warning("Detection evaluation not set for: {}".format(img_key))
                    continue
                E.append(data_src[img_key].detection_evaluation[label_text])
        else:
            raise ValueError("Input src type not supported: {}".format(type(data_src)))
        img_num = len(E) #before sorting out Nones, since we are interested in all images for FA
        E = [e for e in E if not e is None] #None means no GT and dets for image
        if len(E) == 0:
            continue

        dtScores = np.concatenate([e['dtScores'][0:COCOParams.maxDet] for e in E])

        # different sorting method generates slightly different results.
        # mergesort is used to be consistent as Matlab implementation.
        recall_inds = np.argsort(-dtScores, kind='mergesort')
        dtScoresSorted = dtScores[recall_inds]
        # shape dtm = len(imgs), len(gt), len(dt (maxDet))
        dtm = [e['dtMatches'][0:COCOParams.maxDet] for e in E]  # 1758 (images), 1 (detections)
        # shape dtm = len(gt), len(imgs) -- concated by gt
        dtm = np.concatenate(dtm, axis=0)  # 1758 (images)
        dtm = dtm[ recall_inds]  # resort by score all bboxes through all images
        #dtIg = np.concatenate([e['dtIgnore'][:, 0:maxDet] for e in E], axis=1)[:, inds_by_score]  # shape = 10, 1758
        #gtIg = np.concatenate([e['gtIgnore'] for e in E])  # shape (952,)
        gt_count = sum([len(e['gtIds']) for e in E])  # shape (952,)
        tps = dtm.astype(np.bool)
        fps = np.logical_not(dtm)

        tp_sum = np.cumsum(tps, axis=0).astype(dtype=np.float)  # across all images, (1758)
        fp_sum = np.cumsum(fps, axis=0).astype(dtype=np.float)  # (1758)
        #for iou_thresh_i, (tp, fp) in enumerate(zip(tp_sum, fp_sum)):
        # number of GT detections accumulated from the most confident to the least confident
        # if i.e. we have 3/5 TPs: [0.95, 0.8, miss, miss, 0.5]
        # and we have 2/5 FPs:     [TP,    TP, 0.6,  0.55, TP ]
        # then we count them like this, TPs: [1,2,2,2,3], FPS: [0,0,1,2,2]
        tp = tp_sum #np.array(tp)
        fp = fp_sum #np.array(fp)
        num_dets = len(tp) #num of  detections
        if gt_count:
            rc = tp / gt_count  #normalize those TP counts by number of GT == recall
        else:
            rc =np.full_like(tp, np.nan) #no GT
        pr = tp / (fp + tp + np.spacing(1))  # (1758,) #same for precision
        fa = fp / img_num #false alarm rate: num of FPs across all images over total number of images
        #now our rc and pr are counts for recall and precision for each detection sorted by -confidence
        q = np.zeros((R,))  # (101,) precision by recall ruler
        ss = np.zeros((R,)) #confidence by recall ruler

        rc_by_fa_scaled = np.zeros((FA_ruler_size,))
        conf_by_fa_scaled = np.zeros((FA_ruler_size,))

        if num_dets:
            recall[label_i] = rc[-1] #take recall given all dets (last one - with smallest conf)
        else:
            recall[label_i] = 0 #no dets at all => recall = 0

        # numpy is slow without cython optimization for accessing elements
        # use python array gets significant speed improvement
        pr = pr.tolist()
        q = q.tolist()
        rc_by_fa_scaled = rc_by_fa_scaled.tolist()

        #that fix of precision that is specific to MSCOCO. Make precision never increase
        for i in range(num_dets - 1, 0, -1):
            if pr[i] > pr[i - 1]:
                pr[i - 1] = pr[i]
        # Find the indices into a sorted array rc such that, if the corresponding elements in COCOParams.recThrs
        # were inserted before the indices, the order of rc would be preserved.
        recall_inds = np.searchsorted(rc, COCOParams.recThrs, side='left')
        #for FA
        fa_inds = np.searchsorted(fa, COCOParams.faThrs, side='left')

        #for recall/fa curve
        try:
            for fa_tick, det_indx in enumerate(fa_inds):
                # fa_tick - FA rate from our ruler COCOParams.faThrs
                # det_indx - detection index corresponding to this FA
                det_indx = min(det_indx, len(rc)-1)
                rc_by_fa_scaled[fa_tick] = rc[det_indx] #recall corresponding to this FA rate
                conf_by_fa_scaled[fa_tick] = dtScoresSorted[det_indx] #confidence corresponding to FA rate
        except:
            pass

        #for precision/recall curve
        try:
            for ri, pi in enumerate(recall_inds):
                # ri - recall threshold from 0. to 1.0 with step 0.01
                # pi - precision index corresponding to this recall
                q[ri] = pr[pi] #precision corresponding to this recall
                ss[ri] = dtScoresSorted[pi] #confidence corresponding to this recall
        except:
            pass

        precision[:, label_i] = np.array(q)
        scores[:, label_i] = np.array(ss)
        recall_by_fa[:, label_i] = np.array(rc_by_fa_scaled)
        conf_by_fa[:, label_i] = np.array(conf_by_fa_scaled)
    eval = {
        'counts': [R, K],
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'precision': precision,
        'recall': recall,
        'scores': scores,
        'recall_by_fa': recall_by_fa,
        'conf_by_fa': conf_by_fa
    }
    return eval




def summarize(acc_result: Dict[str, Any]) -> Dict[str, Any]:
    '''
    Final post-processing.
    Summarizes result into printable dictionary.
    Takes as input output of accumulate() function.
    :param acc_result: output of accumulate() function
    :return: printable dictionary with metrics
    '''
    prec = acc_result['precision']
    #dimension: recall_thresholds, label_i
    prec = prec[:, :]
    if len(prec[~np.isnan(prec)]) == 0:
        ap_mean_cats = -1
        ap_by_cat = np.full((prec.shape[1],),fill_value=-1)
    else:
        ap_mean_cats = np.nanmean(prec)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            ap_by_cat = np.nanmean(prec, axis=0)

    recall = acc_result['recall']
    if len(recall[~np.isnan(recall)]) == 0:
        recall_mean_cats = -1
        recall_by_cat = np.full((recall.shape[0],),fill_value=-1)
    else:
        recall_mean_cats = np.nanmean(recall)
        recall_by_cat = recall

    rec_conf_list = [{'recall':r,'conf':c} for r,c in zip(acc_result['recall_by_fa'], acc_result['conf_by_fa'])]
    recall_by_fa = OrderedDict(zip(COCOParams.faThrs, rec_conf_list))

    return {'ap_mean_cats':ap_mean_cats,
            'ap_by_cat':ap_by_cat,
            'recall_mean_cats':recall_mean_cats,
            'recall_by_cat':recall_by_cat,
            'recall_by_fa':recall_by_fa}


if __name__ == '__main__':
    label_map = {1:'bbox2'}
    from pprint import pprint
    from syncvtools.data.detections import DetectionEntity, DetectionsCollection, ImageLevelDetections
    from syncvtools.utils.data_import import TFRecords, ProdDetections
    from syncvtools.utils.data_export import COCODetectionsExport, COCOExport
    from syncvtools.utils.draw_detections import DrawDetections
    import cv2
    import syncvtools.utils.file_tools as ft
    gts_all = [[#DetectionEntity(label_text=label_map[0], label_id=0, bbox_abs=(100,200,300,400)),
           DetectionEntity(label_text=label_map[1], label_id=1, bbox_abs=(300,100,400,200)),
           DetectionEntity(label_text=label_map[1], label_id=1, bbox_abs=(10, 10,30,30)),
          # DetectionEntity(label_text=label_map[1], label_id=1, bbox_abs=(50, 50, 100, 100))
           ]] + [[] for x in range(100)]
    dts_all = [[#DetectionEntity(label_text=label_map[0], label_id=0, bbox_abs=(105, 210, 305, 405),score=0.95),
           DetectionEntity(label_text=label_map[1], label_id=1, bbox_abs=(300, 100, 450, 200),score=0.85),
           DetectionEntity(label_text=label_map[1], label_id=1, bbox_abs=(300, 100, 410, 200),score=0.5), #FP (double box) box overlaps with previous one, but higher IOU with GT

           DetectionEntity(label_text=label_map[1], label_id=1, bbox_abs=(50, 50, 100, 100),score=0.6), #FP box with higher score than FP (next one)
           DetectionEntity(label_text=label_map[1], label_id=1, bbox_abs=(10, 10, 33, 29),score=0.4)],  # TP box with lower score than FP above
           ] + [[] for x in range(100)]
    #res = evaluateImg(dts_all=dts,gts_all=gts,aRng=COCOParams.areaRng[0])
    evalImgs = []
    for dts, gts in zip(dts_all,gts_all):
        eval_per_cat = {}
        for label_i, label_text in enumerate(list(label_map.values())):
            #for area_i, area_rng in enumerate(COCOParams.areaRng):
            eval_per_cat[label_text] = evaluate_img(
                dts_all=dts,
                gts_all=gts,
                cat_label=label_text)
        evalImgs.append(eval_per_cat)
    res_acc = accumulate(data_src=evalImgs, cat_ids=list(label_map.values()))
    pprint(summarize(acc_result = res_acc))

