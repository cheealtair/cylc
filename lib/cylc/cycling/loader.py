#!/usr/bin/env python

#C: THIS FILE IS PART OF THE CYLC SUITE ENGINE.
#C: Copyright (C) 2008-2014 Hilary Oliver, NIWA
#C:
#C: This program is free software: you can redistribute it and/or modify
#C: it under the terms of the GNU General Public License as published by
#C: the Free Software Foundation, either version 3 of the License, or
#C: (at your option) any later version.
#C:
#C: This program is distributed in the hope that it will be useful,
#C: but WITHOUT ANY WARRANTY; without even the implied warranty of
#C: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#C: GNU General Public License for more details.
#C:
#C: You should have received a copy of the GNU General Public License
#C: along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Tasks spawn a sequence of POINTS (P) separated by INTERVALS (I).
Each task may have multiple sequences, e.g. 12-hourly and 6-hourly.
"""

import integer
import iso8601


ISO8601_CYCLING_TYPE = 'iso8601'
INTEGER_CYCLING_TYPE = 'integer'

DEFAULT_CYCLING_TYPE = ISO8601_CYCLING_TYPE

POINTS = {INTEGER_CYCLING_TYPE: integer.IntegerPoint,
          ISO8601_CYCLING_TYPE: iso8601.ISO8601Point}

INTERVALS = {INTEGER_CYCLING_TYPE: integer.IntegerInterval,
             ISO8601_CYCLING_TYPE: iso8601.ISO8601Interval}

SEQUENCES = {INTEGER_CYCLING_TYPE: integer.IntegerSequence,
             ISO8601_CYCLING_TYPE: iso8601.ISO8601Sequence}

INIT_FUNCTIONS = {INTEGER_CYCLING_TYPE: integer.init_from_cfg,
                  ISO8601_CYCLING_TYPE: iso8601.init_from_cfg}


def get_point(*args, **kwargs):
    cycling_type = kwargs.pop("cycling_type", DEFAULT_CYCLING_TYPE)
    return get_point_cls(cycling_type=cycling_type)(*args, **kwargs)


def get_point_cls(cycling_type=ISO8601_CYCLING_TYPE):
    return POINTS[cycling_type]


def get_interval(*args, **kwargs):
    cycling_type = kwargs.pop("cycling_type", DEFAULT_CYCLING_TYPE)
    return get_interval_cls(cycling_type=cycling_type)(*args, **kwargs)


def get_interval_cls(cycling_type=ISO8601_CYCLING_TYPE):
    return INTERVALS[cycling_type]


def get_sequence(*args, **kwargs):
    cycling_type = kwargs.pop("cycling_type", DEFAULT_CYCLING_TYPE)
    return get_sequence_cls(cycling_type=cycling_type)(*args, **kwargs)


def get_sequence_cls(cycling_type=ISO8601_CYCLING_TYPE):
    return SEQUENCES[cycling_type]


def init_cyclers(cfg):
    for cycling_type, init_func in INIT_FUNCTIONS.items():
        init_func(cfg)
