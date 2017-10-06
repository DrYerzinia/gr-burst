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

class general_burster(gr.basic_block):
    """
    docstring for block general_burster
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="general_burster",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = 0

    def general_work(self, input_items, output_items):
        print len(input_items[0])
        #output_items[0][:] = input_items[0]
        for i in xrange(len(output_items[0])):
            if i < len(input_items[0]):
                output_items[0][i] = input_items[0][i]
            else:
                output_items[0][i] = 0.

        #consume(0, len(input_items[0]))
        self.consume_each(len(input_items[0]))
        return len(output_items[0])





