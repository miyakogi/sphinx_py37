#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Meta data for sphinx_py37."""

from typing import Optional

__version__ = '0.0.1'


class Node(object):
    """Node class."""

    def __init__(self, parent_node: Optional['Node']) -> None:
        self._parent = parent_node
