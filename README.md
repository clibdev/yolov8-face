# Fork of [derronqi/yolov8-face](https://github.com/derronqi/yolov8-face)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.5. (🔥)
* Original pretrained models from GitHub [releases page](https://github.com/clibdev/yolov8-face/releases). (🔥)
* Sample script [detect.py](detect.py) for inference.
* Sample script [export.py](export.py) to export model to ONNX format.
* The following deprecations has been fixed:
  * DeprecationWarning: 'np.float' is a deprecated alias for builtin 'float'.
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.
  * FutureWarning: Cython directive 'language_level' not set.
  * Cython Warning: Using deprecated NumPy API.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

* Download links:

| Method       | Model Size (MB) | weights                                                                                                                                                                                                   | SHA-256                                                                                                                              |
|--------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv8n-Face | 6.1<br>11.8     | [PyTorch](https://github.com/clibdev/yolov8-face/releases/latest/download/yolov8n-face-derronqi.pt)<br>[ONNX](https://github.com/clibdev/yolov8-face/releases/latest/download/yolov8n-face-derronqi.onnx) | d545bf1add5aa736a4febac4f4f9245a6d596cd0fe70d5d57989fe0cb9e626ca<br>af09683be4937ebe23e9da0346cbf46cd937b73ed5fac986e6205e6c7cdd2c25 |

* Evaluation results on WIDERFace dataset:

| Method       | Test Size | Easy | Medium | Hard |
|--------------|-----------|------|--------|------|
| YOLOv8n-Face | 640       | 94.5 | 92.2   | 79.0 |

# Inference

```shell
python detect.py --weights yolov8n-face-derronqi.pt --source ultralytics/assets/bus.jpg --save-img
```

# WIDERFace evaluation

* Download WIDERFace [validation dataset](https://drive.google.com/file/d/1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q/view).
* Move dataset to `data/widerface/val` directory.

```shell
python test_widerface.py --weights yolov8n-face-derronqi.pt --dataset_folder data/widerface/val/images/
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
python export.py --weights yolov8n-face-derronqi.pt
```
