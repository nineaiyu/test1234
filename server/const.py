# -*- coding: utf-8 -*-
#
import os
__all__ = ['PROJECT_DIR', 'VERSION', 'CONFIG', 'LOG_DIR', 'TMP_DIR', 'CELERY_LOG_DIR']

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(PROJECT_DIR, "data", "logs")
TMP_DIR = os.path.join(PROJECT_DIR, "data", "tmp")
CELERY_LOG_DIR = os.path.join(LOG_DIR, "task")
VERSION = '5.0.0'
