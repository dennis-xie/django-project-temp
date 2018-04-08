#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create by Pycharm
File        dennis_pyweb:log.py
User        xieminliang
Create Date 2018/4/4 14:46

"""
# -*- coding: utf-8 -*-

"""
Usage:

    from common.log import logger

    logger.info("test")
    logger.error("wrong1")
    logger.exception("wrong2")

    # with traceback
    try:
        1 / 0
    except Exception:
        logger.exception("wrong3")
"""

import logging

logger = logging.getLogger("root")