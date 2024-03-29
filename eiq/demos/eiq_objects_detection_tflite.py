#!/usr/bin/env python3
# Copyright 2020 NXP Semiconductors
# SPDX-License-Identifier: BSD-3-Clause

from eiq.modules.detection.object_detection_ssd import eIQObjectsDetection


def main():
    app = eIQObjectsDetection()
    app.run()


if __name__ == '__main__':
    main()
