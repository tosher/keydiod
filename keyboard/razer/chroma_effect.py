#!/usr/bin/env python\n
# -*- coding: utf-8 -*-

from zipfile import ZipFile
from lxml import etree


def element_dig(element, path):
    for token in path:
        element = element.find(token)
        if element is None:
            return None
    return element


def unzip_first_tree(filepath_abs):
    '''
    Unpacks first file from archive,
    returns as xmltree obj
    '''

    with ZipFile(filepath_abs, 'r') as zip_obj:
        filenames = zip_obj.namelist()
        data = zip_obj.read(filenames[0])
        xmldata = etree.fromstring(data)
        xmltree = etree.ElementTree(xmldata)
    return xmltree


def extract_static(filepath_abs):

    def region_color(region):
        rgb = (0, 0, 0)

        color = element_dig(region, ['Colors', 'RzColor'])
        if color is None:
            return rgb

        is_blank = color.find('IsBlank')
        if is_blank is not None and is_blank.text == 'true':
            return rgb

        red = color.find('Red')
        green = color.find('Green')
        blue = color.find('Blue')
        rgb = (
            int(red.text) if red is not None else 0,
            int(green.text) if green is not None else 0,
            int(blue.text) if blue is not None else 0
        )
        return rgb

    def region_keys(region):
        attr = element_dig(region, ['Cells', 'Item', 'Value', 'ArrayOfDeviceCell'])
        if attr is None:
            return []
        return attr.getchildren()

    xmltree = unzip_first_tree(filepath_abs)
    diods = {}
    regions = []
    elayers = xmltree.find('EffectLayers').getchildren()
    for elayer in elayers:
        if elayer.find('Effect').text != 'static':
            continue
        regions = elayer.find('Regions').getchildren()
        break

    for region in regions:
        rgb = region_color(region)
        for key in region_keys(region):
            row = int(key.find('Row').text)
            col = int(key.find('Col').text)
            if row not in diods:
                diods[row] = {}
            diods[row][col] = rgb

    return diods
