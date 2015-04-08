#!/usr/bin/env python

import os
import sys

from . import interp

def parse(stream, template):
	"""Parse the stream using the supplied template

	:stream: Input stream
	:template: template contents (str)
	:returns: pfp DOM

	"""
	interpretor = interp.PfpInterp()
	dom = interp.parse(stream, template)
	return dom
