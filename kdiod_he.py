#!/usr/bin/env python\n
# -*- coding: utf-8 -*-

import os
import argparse
from keyboard.razer.huntsman.huntsman_elite import HuntsmanElite


argp = argparse.ArgumentParser(description='Convert .ChromaEffects file to Fruity UI JSON')
argp.add_argument('--effect_file', help='Path to .ChromaEffects file with static effect', type=str, required=True)
args = argp.parse_args()

if not args.effect_file:
    print('Argument effect_file is required to proceed.')
    exit(0)

keyb = HuntsmanElite.from_chroma_effects(args.effect_file)

print('Fruity UI result JSON:')

data = keyb.to_fruity()
print(data)

res_file = '{}.json'.format(os.path.splitext(args.effect_file)[0])
with open(res_file, 'w') as fruity_data:
    fruity_data.write(data)

print('Result saved to file {}'.format(res_file))
