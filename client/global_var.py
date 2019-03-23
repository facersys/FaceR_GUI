# -*- coding: utf-8 -*-


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, default=None):
    try:
        return _global_dict[name]
    except KeyError:
        return default


_init()
set_value('checked_students', [])
