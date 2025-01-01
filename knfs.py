#!/usr/bin/env python

## Copyright (C) 2004, Julien Morot

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sys
import os

try:
    from qt import *
except:
    print """Could not locate the PyQt module.  Please make sure that
you have installed PyQt for the version of Python that you are running."""
    sys.exit(1)

from mainwindow import *

def main():
    app = QApplication(sys.argv)
    gui = MainWin()
    QObject.connect(app,SIGNAL("lastWindowClosed()"),app,SLOT("quit()"))
    app.setMainWidget(gui)
    gui.show()
    app.exec_loop()

if __name__ == '__main__':
    main()

