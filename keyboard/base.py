#!/usr/bin/env python\n
# -*- coding: utf-8 -*-


class BaseKeyboard(object):

    def __init__(self, diods):
        self.diods = diods


class BaseKeyboardRow(object):

    @staticmethod
    def rgb2hex(val):
        clr_r, clr_g, clr_b = val
        return '#{:02x}{:02x}{:02x}'.format(clr_r, clr_g, clr_b)
