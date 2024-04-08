#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Benchmarks for general test of ASV Benchmarking Tool.
"""
from gc import get_objects


# @skip_benchmark
class TimeRawSuite:
    @staticmethod
    def timeraw_import_range():
        return """
        from builtins import range
        """


# @skip_benchmark
class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """

    def __init__(self):
        self.d = None

    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        for key in self.d.keys():
            pass

    def time_values(self):
        for value in self.d.values():
            pass

    def time_range(self):
        d = self.d
        for key in range(500):
            d[key]


# @skip_benchmark
class MemSuite:
    @staticmethod
    def mem_list():
        return [0] * 256


# @skip_benchmark
class PeakMemSuite:
    @staticmethod
    def peakmem_list():
        return [0] * 256


# @skip_benchmark
class TrackSuite:
    @staticmethod
    def track_num_objects():
        return len(get_objects())

    track_num_objects.unit = "objects"
