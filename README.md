# Fork of [derronqi/yolov8-face](https://github.com/derronqi/yolov8-face)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.1. (🔥)
* Original pretrained models from GitHub [releases page](https://github.com/clibdev/yolov8-face/releases). (🔥)
* Sample script [detect.py](detect.py) for inference.
* Sample script [export.py](export.py) to export model to ONNX format.
* The following deprecations has been fixed:
  * DeprecationWarning: 'np.float' is a deprecated alias for builtin 'float'.
  * FutureWarning: Cython directive 'language_level' not set.
  * Cython Warning: Using deprecated NumPy API.

# Installation

```shell
pip install -r requirements.txt
```

# yolov8-face

| Method  | Test Size | Easy | Medium | Hard | FLOPs (B) @640 | weights                                                                                                                                                                               |
|---------|-----------|------|--------|------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| yolov8n | 640       | 94.5 | 92.2   | 79.0 | -              | [PyTorch](https://github.com/clibdev/yolov8-face/releases/latest/download/yolov8n-face.pt), [ONNX](https://github.com/clibdev/yolov8-face/releases/latest/download/yolov8n-face.onnx) |

# Inference

```shell
python detect.py --weights yolov8n-face.pt --source ultralytics/assets/bus.jpg --save-img
```

# WIDERFace evaluation

* Download WIDERFace [validation dataset](https://drive.google.com/file/d/1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q/view).
* Move dataset to `data/widerface/val` directory.

```shell
python test_widerface.py --weights yolov8n-face.pt --dataset_folder data/widerface/val/images/
```
```shell
cd widerface_evaluate
```
```shell
python setup.py build_ext --inplace
```
```shell
python evaluation.py
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --weights yolov8n-face.pt
```
