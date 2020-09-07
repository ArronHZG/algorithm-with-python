import numpy as np


def nms(dets, thresh):
    """Pure Python NMS baseline."""
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]
    return keep


def non_max_suppression(boxes, scores, threshold):
    """执行non-maximum suppression并返回保留的boxes的索引.
    boxes: [N, (y1, x1, y2, x2)].注意(y2, x2)可以会超过box的边界.
    scores: box的分数的一维数组.
    threshold: Float型. 用于过滤IoU的阈值.
    """
    assert boxes.shape[0] > 0
    if boxes.dtype.kind != "f":
        boxes = boxes.astype(np.float32)

    # 计算box面积
    y1 = boxes[:, 0]
    x1 = boxes[:, 1]
    y2 = boxes[:, 2]
    x2 = boxes[:, 3]
    area = (y2 - y1) * (x2 - x1)

    # 获取根据分数排序的boxes的索引(最高的排在对前面)
    order = scores.argsort()[::-1]

    pick = []
    while len(order) > 0:
        # 选择排在最前的box，并将其索引加到列表中
        i = order[0]
        pick.append(i)
        # 计算选择的box与剩下的box的IoU
        iou = compute_iou(boxes[i], boxes[order[1:]], area[i], area[order[1:]])
        # 确定IoU大于阈值的boxes. 这里返回的是ix[1:]之后的索引，
        # 所以为了与ixs保持一致，将结果加1
        remove_ixs = np.where(iou > threshold)[0] + 1
        # 将选择的box和重叠的boxes的索引删除.
        order = np.delete(order, remove_ixs)
        order = np.delete(order, 0)
    return np.array(pick, dtype=np.int32)


def nms(bbox, scores, thresh):
    areas = np.prod(bbox[:, 2:] - bbox[:, :2], axis=1)
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        tl = np.maximum(b[:2], bbox[i + 1:, :2])
        br = np.minimum(b[2:], bbox[i + 1:, 2:])
        inter = np.prod(br - tl, axis=1) * (br > tl).all(axis=1)
        ovr = inter / (areas[order[1:]] + areas[i] - inter)
        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]
    return keep


def nms(bbox, scores, thresh):
    area = np.prod(bbox[:, 2:] - bbox[:, :2], axis=1)
    keep = np.ones(len(bbox), dtype=bool)
    for i, b in enumerate(bbox):
        if (keep[i] == False):
            continue
        tl = np.maximum(b[:2], bbox[i + 1:, :2])
        br = np.minimum(b[2:], bbox[i + 1:, 2:])
        inter = np.prod(br - tl, axis=1) * (br >= tl).all(axis=1)
        iou = ia / (area[i + 1:] + area[i] - inter)
        r = [k for k in np.where(iou > thresh)[0] + i + 1 if keep[k] == True]
        if (scores[i] > scores[r]).all():
            keep[r] = False
        else:
            keep[i] = False
    return np.where(keep)[0].astype(np.int32)
