#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class gmsk_burst_source(gr.sync_block):
    """
    docstring for block gmsk_burst_source
    """
    def __init__(self, message, period):
        gr.sync_block.__init__(self,
            name="gmsk_burst_source",
            in_sig=None,
            out_sig=[numpy.float32])
        self.message = message
        self.period = period


    def work(self, input_items, output_items):
        out = output_items[0]
        # <+signal processing here+>
        out[:] = whatever
        return len(output_items[0])





