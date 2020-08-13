#!/usr/bin/env python\n
# -*- coding: utf-8 -*-

import json

from keyboard.razer.base import RazerKeyboard
from .huntsman_elite_rows import HuntsmanEliteRow
from .huntsman_elite_rows import HuntsmanEliteKeyboardRow
from .huntsman_elite_rows import HuntsmanEliteUnderglow
from .huntsman_elite_rows import HuntsmanEliteUnderglowDetachable
from . import huntsman_elite_map as keymap


class HuntsmanElite(RazerKeyboard):

    def key_swap(self, col, row1, row2):
        if not self.diods[row1].get(col):
            self.diods[row1][col] = (0, 0, 0)
        if not self.diods[row2].get(col):
            self.diods[row2][col] = (0, 0, 0)
        self.diods[row1][col], self.diods[row2][col] = self.diods[row2][col], self.diods[row1][col]

    def to_fruity(self, as_json=True):
        fruity_synapse3_data = {
            'type': 'raw',
            'rows': []
        }

        # NOTE: in Fruity Numpad's Enter (22) in 6 row
        #       in Chroma - in 5 row
        #       move it
        self.key_swap(22, 5, 6)

        for rownum in range(1, 7):
            r_keyb = HuntsmanEliteKeyboardRow()
            r_keyb.to_fruity(
                self.diods[rownum],
                getattr(keymap, 'keyboard_row_{}_map'.format(rownum))
            )
            fruity_synapse3_data['rows'].append(r_keyb.fruits)

        r_keyb_underglow = HuntsmanEliteUnderglow()
        r_keyb_underglow.to_fruity(self.diods, keymap.keyboard_underglow_map)
        rowsize = HuntsmanEliteRow.FRUITY_ROW_SIZE
        fruity_synapse3_data['rows'].append(r_keyb_underglow.fruits[:rowsize])
        fruity_synapse3_data['rows'].append(r_keyb_underglow.fruits[rowsize:])

        r_keyb_underglow_detach = HuntsmanEliteUnderglowDetachable()
        r_keyb_underglow_detach.to_fruity(self.diods, keymap.underglow_detachable_map)
        fruity_synapse3_data['rows'].append(r_keyb_underglow_detach.fruits)

        if as_json:
            return json.dumps(fruity_synapse3_data)

        return fruity_synapse3_data
