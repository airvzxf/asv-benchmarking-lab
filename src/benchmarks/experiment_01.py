#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Benchmarks for the experiment 01 in core.
"""
from asv_runner.benchmarks.mark import timeout_at

from experiments.experiment_01 import wait_for_x_seconds


class TimeRawSuite:
    @staticmethod
    def timeraw_import_wait_for_x_seconds():
        return """
from experiments.experiment_01 import wait_for_x_seconds
"""


class Time:
    @staticmethod
    @timeout_at(600)
    def time_wait_for_x_seconds():
        wait_for_x_seconds()
