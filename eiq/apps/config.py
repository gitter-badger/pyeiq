# Copyright 2020 NXP Semiconductors
# SPDX-License-Identifier: BSD-3-Clause

# Switch Label Image

IMAGES_DRIVE_ID = "12wRWlzYQp1ABp2hVuZcPiO5FipEy6HIJ"
IMAGES_DRIVE_NAME = "bmp_examples"

DEFAULT_TFLITE_IMAGE = "/usr/bin/tensorflow-lite-2.1.0/examples/grace_hopper.bmp"

TFLITE_LABEL_IMAGE_ACCEL = "cd /usr/bin/tensorflow-lite-2.1.0/examples/; " \
                           "VSI_NN_LOG_LEVEL=0 ./label_image " \
                           "-m /usr/bin/tensorflow-lite-2.1.0/examples/mobilenet_v1_1.0_224_quant.tflite " \
                           "-t 1 -i {} " \
                           "-l labels.txt -a 1 -v 0 -c 100"

TFLITE_LABEL_IMAGE_NO_ACCEL = "cd /usr/bin/tensorflow-lite-2.1.0/examples/; " \
                              "VSI_NN_LOG_LEVEL=0 ./label_image " \
                              "-m /usr/bin/tensorflow-lite-2.1.0/examples/mobilenet_v1_1.0_224_quant.tflite " \
                              "-t 1 -i {} " \
                              "-l labels.txt -a 0 -v 0 -c 100"

REGEX_GET_INTEGER_FLOAT = "\d+\.\d+|\d+"

REGEX_GET_STRING = "[^a-zA-Z\s]"

SWITCH_MODEL_NAME = "<b>MODEL NAME</b>"

SWITCH_LABELS = "<b>LABELS</b>"

SWITCH_RESULTS = "<b>RESULTS (%)</b>"

SWITCH_INFERENCE_TIME = "<b>INFERENCE TIME</b>"

SWITCH_SELECT_IMAGE = "<b>SELECT AN IMAGE</b>"

# Apps Titles

TITLE_LABEL_IMAGE_SWITCH = "PyeIQ - Label Image Switch App"

# ML Player

MAIN_WINDOW_TITLE = "PyeIQ ML Player"

DEFAULT_DEMOS_DIR = "/opt/eiq/demos"
DEFAULT_DEMOS_DESCRIPTION = "Demos\nDescription"

DEFAULT_IMAGE = "/usr/bin/tensorflow-lite-2.1.0/examples/grace_hopper.bmp"
DEFAULT_IMAGE_HEIGHT = 400
DEFAULT_IMAGE_WIDTH = 300

RUN_DEMO = "python3 /opt/eiq/demos/{} -i {}"

ALIGN_LEFT = 0.0
ALIGN_CENTER = 0.5
ALIGN_RIGHT = 1.0
