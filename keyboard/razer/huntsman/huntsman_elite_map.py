#!/usr/bin/env python\n
# -*- coding: utf-8 -*-

keyboard_row_1_map = [
    None,
    ('Esc', 1),
    None,
    None,
    ('F1', 3),
    ('F2', 4),
    ('F3', 5),
    ('F4', 6),
    ('F5', 7),
    ('F6', 8),
    ('F7', 9),
    ('F8', 10),
    ('F9', 11),
    ('F10', 12),
    ('F11', 13),
    ('F12', 14),
    ('PrintScreen', 15),
    ('ScrollLock', 16),
    ('Pause', 17),
    ('Media-1', 18, 20),  # in Synapse-3, one color for three media keys, in real may has different values
    ('Media-2', 19),
    ('Media-3', 20, 20),
    ('Volume', 21),
    None
]

keyboard_row_2_map = [
    ('Underglow-0', None),
    ('`', 1),
    ('1', 2),
    ('2', 3),
    ('3', 4),
    ('4', 5),
    ('5', 6),
    ('6', 7),
    ('7', 8),
    ('8', 9),
    ('9', 10),
    ('0', 11),
    ('-', 12),
    ('=', 13),
    ('Backspace', 14),
    None,
    ('Ins', 15),
    ('Home', 16),
    ('PageUp', 17),
    ('NumLock', 18),
    ('/', 19),
    ('*', 20),
    ('-', 21),
    ('Underglow-23', None)
]


keyboard_row_3_map = [
    ('Underglow-0', None),
    ('Tab', 1),
    ('q', 2),
    ('w', 3),
    ('e', 4),
    ('r', 5),
    ('t', 6),
    ('y', 7),
    ('u', 8),
    ('i', 9),
    ('o', 10),
    ('p', 11),
    ('[', 12),
    (']', 13),
    ('Backslash', 14),
    None,
    ('Del', 15),
    ('End', 16),
    ('PageDown', 17),
    ('NP-7', 18),
    ('NP-8', 19),
    ('NP-9', 20),
    ('+', 21),
    ('Underglow-23', None)
]


keyboard_row_4_map = [
    None,
    None,
    ('Capslock', 1),
    ('a', 2),
    ('s', 3),
    ('d', 4),
    ('f', 5),
    ('g', 6),
    ('h', 7),
    ('j', 8),
    ('k', 9),
    ('l', 10),
    (';', 11),
    ('Quot', 12),
    ('Enter', 14),
    None,
    None,
    None,
    None,
    ('NP-4', 18),
    ('NP-5', 19),
    ('NP-6', 20),
    None,
    None
]


keyboard_row_5_map = [
    ('Underglow-0', None),
    None,
    ('LShift', 1),
    ('z', 3),
    ('x', 4),
    ('c', 5),
    ('v', 6),
    ('b', 7),
    ('n', 8),
    ('m', 9),
    (',', 10),
    ('.', 11),
    ('Slash', 12),
    None,
    ('RShift', 14),
    None,
    None,
    ('Up-Arrow', 16),
    None,
    ('NP-1', 18),
    ('NP-2', 19),
    ('NP-3', 20),
    ('Enter', 21),  # None
    ('Underglow-23', None)
]


keyboard_row_6_map = [
    None,
    ('LCtrl', 1),
    ('Win', 2),
    ('LAlt', 3),
    None,
    None,
    None,
    ('Space', 7),
    None,
    None,
    None,
    None,
    ('RAlt', 11),
    ('Fn', 12),
    ('Prop', 13),
    ('RCtrl', 14),
    ('Left-Arrow', 15),
    ('Down-Arrow', 16),
    ('Right-Arrow', 17),
    None,
    ('NP-0', 19),
    ('Del', 20),
    None,  # ('Enter', 21),
    None
]

# NOTE: name, diods->row, diods-row->col, fruity-index

keyboard_underglow_map = [
    ('Underglow-0-1', 0, 1, 0),
    ('Underglow-0-3', 0, 3, 1),
    ('Underglow-0-4', 0, 4, 2),
    ('Underglow-0-6', 0, 6, 3),
    ('Underglow-0-7', 0, 7, 4),
    ('Underglow-0-9', 0, 9, 5),
    ('Underglow-0-10', 0, 10, 6),
    ('Underglow-0-12', 0, 12, 7),
    ('Underglow-0-14', 0, 14, 8),
    ('Underglow-0-16', 0, 16, 9),
    ('Underglow-0-17', 0, 17, 10),
    ('Underglow-0-19', 0, 19, 11),
    ('Underglow-0-20', 0, 20, 12),
    ('Underglow-0-22', 0, 22, 13),
    ('Underglow-0-23', 0, 23, 14),
    # row-1-empty
    ('Underglow-2-23', 2, 23, 15),
    ('Underglow-3-23', 3, 23, 16),
    # row-4-empty
    ('Underglow-5-23', 5, 23, 17),
    # row-6-empty
    ('Underglow-7-0', 7, 0, 18),
    ('Underglow-7-1', 7, 1, 19),
    ('Underglow-7-3', 7, 3, 20),
    ('Underglow-7-4', 7, 4, 21),
    ('Underglow-7-6', 7, 6, 22),
    ('Underglow-7-7', 7, 7, 23),
    ('Underglow-7-9', 7, 9, 24),
    ('Underglow-7-10', 7, 10, 25),
    ('Underglow-7-12', 7, 12, 26),
    ('Underglow-7-14', 7, 14, 27),
    ('Underglow-7-16', 7, 16, 28),
    ('Underglow-7-17', 7, 17, 29),
    ('Underglow-7-19', 7, 19, 30),
    ('Underglow-7-20', 7, 20, 31),
    ('Underglow-7-22', 7, 22, 32),
    ('Underglow-7-23', 7, 23, 33),
    # row-6-empty
    ('Underglow-5-0', 5, 0, 34),
    # row-4-empty
    ('Underglow-3-0', 3, 0, 35),
    ('Underglow-2-0', 2, 0, 36),
    # row-1-empty
    ('Underglow-0-0', 0, 0, 37)
]


underglow_detachable_map = [
    ('UnderglowDeatchable-8-23', 8, 23, 0),
    ('UnderglowDeatchable-9-23', 9, 23, 1),
    ('UnderglowDeatchable-10-23', 10, 23, 2),
    ('UnderglowDeatchable-10-22', 10, 22, 3),
    ('UnderglowDeatchable-10-20', 10, 20, 4),
    ('UnderglowDeatchable-10-19', 10, 19, 5),
    ('UnderglowDeatchable-10-17', 10, 17, 6),
    ('UnderglowDeatchable-10-16', 10, 16, 7),
    ('UnderglowDeatchable-10-14', 10, 14, 8),
    ('UnderglowDeatchable-10-12', 10, 12, 9),
    ('UnderglowDeatchable-10-10', 10, 10, 10),
    ('UnderglowDeatchable-10-9', 10, 9, 11),
    ('UnderglowDeatchable-10-7', 10, 7, 12),
    ('UnderglowDeatchable-10-6', 10, 6, 13),
    ('UnderglowDeatchable-10-4', 10, 4, 14),
    ('UnderglowDeatchable-10-3', 10, 3, 15),
    ('UnderglowDeatchable-10-1', 10, 1, 16),
    ('UnderglowDeatchable-10-0', 10, 0, 17),
    ('UnderglowDeatchable-9-0', 9, 0, 18),
    ('UnderglowDeatchable-8-0', 8, 0, 19)
]
