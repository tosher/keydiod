#!/usr/bin/env python\n
# -*- coding: utf-8 -*-

from keyboard.base import BaseKeyboard
from .chroma_effect import extract_static


class RazerKeyboard(BaseKeyboard):

    def __init__(self, diods):
        self.diods = diods

    @classmethod
    def from_chroma_effects(cls, filepath_abs):
        diods = extract_static(filepath_abs)
        return cls(diods)
