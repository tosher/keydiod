#!/usr/bin/env python\n
# -*- coding: utf-8 -*-

from keyboard.base import BaseKeyboardRow

HEX_BLACK = '#000000'


class HuntsmanEliteRow(BaseKeyboardRow):
    FRUITY_ROW_SIZE = 26

    def __init__(self):
        self.fruits = ['#000000'] * self.FRUITY_ROW_SIZE


class HuntsmanEliteKeyboardRow(HuntsmanEliteRow):

    def to_fruity(self, row, keymap):
        for idx, k in enumerate(keymap):
            if idx in [0, 23]:
                # underglow diods will be in sep. underlow arrays
                continue
            if k is None:
                continue

            alt_idx = None
            fruit_idx = k[1]
            if len(k) > 2:
                alt_idx = k[2]

            row_idx = alt_idx or idx

            if row_idx not in row:
                continue

            clr = self.rgb2hex(row[row_idx])
            self.fruits[fruit_idx] = clr


class HuntsmanEliteUnderglow(HuntsmanEliteRow):
    '''
    2 Fruity rows (size 26) in one list
    '''

    FRUITY_ROW_SIZE = 52

    def to_fruity(self, diods, keymap):
        if not diods:
            return
        for k in keymap:
            if k[1] not in diods:
                continue
            if k[2] not in diods[k[1]]:
                continue
            rgb = diods[k[1]][k[2]]
            self.fruits[k[3]] = self.rgb2hex(rgb)


class HuntsmanEliteUnderglowDetachable(HuntsmanEliteUnderglow):
    FRUITY_ROW_SIZE = 26
