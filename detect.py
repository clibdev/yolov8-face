import argparse
from ultralytics import YOLO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='./yolov8n-face.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='./ultralytics/assets/bus.jpg', help='source')
    parser.add_argument('--img-size', nargs='+', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.6, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--save-img', action='store_true', help='save results')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    model.predict(
        source=opt.source,
        imgsz=opt.img_size,
        conf=opt.conf_thres,
        iou=opt.iou_thres,
        device=opt.device,
        save=opt.save_img
    )
