import argparse
from ultralytics import YOLO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='./yolov8n-face.pt', help='model.pt path(s)')
    parser.add_argument('--img-size', nargs='+', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--dynamic', action='store_true', default=False, help='enable dynamic axis in onnx model')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    model.export(
        format='onnx',
        imgsz=opt.img_size,
        dynamic=opt.dynamic,
        opset=18
    )
