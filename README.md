# Fork of [derronqi/yolov8-face](https://github.com/derronqi/yolov8-face)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Original pretrained models from GitHub [releases page](https://github.com/clibdev/yolov8-face/releases). (🔥)
* Sample script [detect.py](detect.py) for inference.

# Installation

```shell
pip install -r requirements.txt
```

# yolov8-face

| Method  | Test Size | Easy | Medium | Hard | FLOPs (B) @640 | weights                                                                                    |
|---------|-----------|------|--------|------|----------------|--------------------------------------------------------------------------------------------|
| yolov8n | 640       | 94.5 | 92.2   | 79.0 | -              | [PyTorch](https://github.com/clibdev/yolov8-face/releases/latest/download/yolov8n-face.pt) |

# Inference

```shell
python detect.py --weights yolov8n-face.pt --source ultralytics/assets/bus.jpg --save-img
```
