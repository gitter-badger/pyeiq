# PyeIQ

PyeIQ gathers everything needed by itself. It provides a simplified way to run
ML applications, which avoids the user spending time on preparing the environment.

## Release Date

| PyeIQ Version | Release Date | Notes |
|---------------|--------------|-------|
| tag_v1.0      | Apr 29, 2020 | -     |

## BSP Support

| **i.MX Board** | **BSP Release**   | **PyeIQ Version Support** | **Building Status** |
|----------------|-------------------|---------------------------|---------------------|
| 8 QM           | _5.4.3_2.0.0_     | tag_v1.0                  | **passing**         |
| 8 MPlus        | _5.4.3_2.0.0_     | tag_v1.0                  | **passing**         |
| 8 M Mini       | _5.4.3_2.0.0_     | tag_v1.0                  | -                   |


## Applications Status

| Application Name                  | Application Type   | i.MX Board | BSP Release   | BSP Framework           | Inference Core | Status      |  Notes                 |
|-----------------------------------|--------------------|------------|---------------|-------------------------|----------------|-------------|------------------------|
| Label Image                       | File Based         | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | **passing** | -                      |
| Label Image Switch                | File Based         | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | **passing** | -                      |
| Images Switch                     | File Based         | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | **passing** | -                      |
| Object Detection                  | SSD/Camera Based   | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | **passing** | Need better model.     |
| Object Detection OpenCV           | SSD/Camera Based   | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | **passing** | Need better model.     |
| Object Detection GStreamer        | SSD/Camera Based   | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | -           | Pending issues.        |
| Object Detection Yolov3           | SSD/File Based     | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | -           | Pending issues.        |
| Object Detection Yolov3           | SSD/Camera Based   | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | -           | Pending issues.        |
| Fire Detection                    | File Based         | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | **passing** | -                      |
| Fire Detection                    | Camera Based       | QM, MPlus  | _5.4.3_2.0.0_ | TensorFlow Lite _2.1.0_ | GPU, NPU       | **passing** | -                      |
| Fire Detection                    | Camera Based       | -          | _5.4.3_2.0.0_ | PyArmNN _19.08_         | -              | -           | Requires _19.11_       |
| Coral Posenet                     | Camera Based       | -          | -             | -                       | -              | -           | Ongoing                |
| NEO DLR                           | Camera Based       | -          | -             | -                       | -              | -           | Ongoing                |


## Copyright and License

© 2020 NXP Semiconductors.

Free use of this software is granted under the terms of the BSD 3-Clause License.
