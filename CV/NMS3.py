import numpy as np
import matplotlib.pyplot as plt

# 给出 左下和右上的顶点, x1,y1,x2,y2
boxes = np.array([[100, 100, 210, 210],
                  [250, 250, 420, 420],
                  [220, 220, 320, 330],
                  [100, 100, 210, 210],
                  [230, 240, 325, 330],
                  [220, 230, 315, 340]])

scores = np.array([0.72,
                   0.8,
                   0.92,
                   0.72,
                   0.81,
                   0.9])
'''
ious [0.79664777 0.70984056 0.16573009 0.         0.        ]
[2 3 4]
ious [0. 0.]
[0 1]
ious [1.]
[]'''


def IOU(index, order, boxes, area):
    # 选取 x1 , y1 中 较大的点
    min_x1_y1 = np.maximum(boxes[index, :2], boxes[order, :2])
    # 选取 x2 , y2 中 较小的点
    max_x2_y2 = np.minimum(boxes[index, 2:], boxes[order, 2:])
    # 如果 x1,y1 < x2, y2 则表示相交, mask 为true, 否则为false
    mask = np.all(max_x2_y2 > min_x1_y1, axis=1)
    inter_area = np.prod(max_x2_y2 - min_x1_y1, axis=1) * mask
    # iou 计算公式
    iou = inter_area / (area[index] + area[order] - inter_area)
    return iou


def nums(boxes, scores, threshold=0.7):
    # 计算面积
    areas = np.prod(boxes[:, 2:] - boxes[:, :2], axis=1)
    # 得到按照scores 排序后的box 序号
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        keep.append(order[0])
        order = order[1:]
        # 如果iou大于阈值, 则去掉对应框, 如果小于等于阈值, 则保留进行下一次处理
        iou = IOU(keep[-1], order, boxes, areas)
        # 在order中, 可以保留下的index
        save_order_idx = np.where(iou <= threshold)[0]
        # 保留下的order
        order = order[save_order_idx]
    return keep


def plot_bbox(dets, c='k'):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]

    plt.plot([x1, x2], [y1, y1], c)
    plt.plot([x1, x1], [y1, y2], c)
    plt.plot([x1, x2], [y2, y2], c)
    plt.plot([x2, x2], [y1, y2], c)
    plt.title("after nms")


plot_bbox(boxes, 'k')  # before nms
plt.show()
keep = nums(boxes, scores)
print(keep)
plot_bbox(boxes[keep], 'r')  # after nms
plt.show()
