#!/usr/bin/env python2

# THIS FILE IS PART OF THE CYLC SUITE ENGINE.
# Copyright (C) 2008-2018 NIWA & British Crown (Met Office) & Contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os, sys
# parse:
sys.path.append( os.path.join( os.path.dirname(os.path.abspath(__file__)), '..' ))
# cylc:
sys.path.append( os.path.join( os.path.dirname(os.path.abspath(__file__)), '../..' ))

from cfgspec import SPEC
from parsec.config import ParsecConfig
import cylc.flags

cylc.flags.verbose = True
class testcfg( ParsecConfig ):
    def check( self, sparse ):
        # TEMPORARY EXAMPLE
        if 'missing item' not in self.sparse.keys():
            print "missing item is MISSING!!!!"

cfg = testcfg( SPEC )
strict = False
cfg.loadcfg( os.path.join( os.path.dirname( __file__ ), 'site.rc' )) # TODO: test strict=False (fail but accept defaults)
cfg.loadcfg( os.path.join( os.path.dirname( __file__ ), 'user.rc' ))

cfg.dump()
#print
#cfg.dump( ['list values'] )
#print
#cfg.dump( ['list values', 'integers'] )
#print
#cfg.dump( ['single values', 'strings with internal comments'] )
