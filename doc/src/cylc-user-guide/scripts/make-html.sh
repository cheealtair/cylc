#!/bin/bash

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

# Make HTML Cylc User Guide (called from Makefile).

set -e

TYPE=$1  # "multi" or "single"

DEST=html/$TYPE
rm -rf $DEST; mkdir -p $DEST

cp -r *.tex cug-html.cfg cylc-version.txt titlepic.sty $DEST

cd $DEST
ls *.tex | xargs -n 1 perl -pi -e 's@graphics/png/orig@../../graphics/png/scaled@g'
ls *.tex | xargs -n 1 perl -pi -e 's@\.\./etc/@../../../etc/@g'
perl -pi -e 's@categories/@../../categories/@g' commands.tex
perl -pi -e 's@commands/@../../commands/@g' commands.tex
perl -pi -e 's@cylc.txt@../../cylc.txt@g' commands.tex
perl -pi -e 's@\.\./README@../../../README@g' cug.tex
perl -pi -e 's@\.\./INSTALL@../../../INSTALL@g' cug.tex
perl -pi -e 's@job-host-2.tex@job-host-2-html.tex@g' cug.tex

# NOTE the 5th argument '-halt-on-error' is passed to the latex
# compiler, but htlatex does not return error status if latex aborts.
# This is ok for cylc test purposes as we run pdflatex before htlatex.
if [[ $TYPE == multi ]]; then
    htlatex cug-html.tex "cug-html.cfg,html,fn-in,2,next" "" "" "-halt-on-error"
else
    htlatex cug-html.tex "cug-html.cfg,html,1,fn-in" "" "" "-halt-on-error"
fi
