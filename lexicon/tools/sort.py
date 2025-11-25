# -*- coding: utf-8 -*-
# PYTHON 3.10

# COPYRIGHT LICENSE: ISC license. See LICENSE.md in the top level directory.
# SPDX-License-Identifier: ISC

# ============================================================ #

import sys, os, time

from common import edit_json_from_path

SELF_PATH = os.path.dirname(os.path.realpath(__file__))

# ============================================================ #

def entrypoint():
	start_time = time.time()
	path = SELF_PATH + "/../lexicon.json"
	edit_json_from_path(
		path, sorted_from, output_path = path)
	print("Execution time: {:.3f}s.".format(
		time.time() - start_time))

def sorted_from(lexicon):
	return sorted(
		lexicon,
		key = lambda entry: entry["lemma"]
	)

# ============================================================ #

# === ENTRY POINT === #

entrypoint()

