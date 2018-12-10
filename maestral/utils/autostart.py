#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 23:08:47 2018

@author: samschott
"""

import sys
import os
import shutil

_root = os.path.abspath(os.path.dirname(__file__))


class AutoStart(object):

    def __init__(self):
        if sys.platform == "darwin":
            self.filename = "com.maestral.loginscript.plist"
            self.distnation_dir = os.path.expanduser("~/Library/LaunchAgents")
        elif sys.platform in ["linux1", "linux2"]:
            self.filename = "maestral.desktop"
            self.distnation_dir = os.path.expanduser("~/.config/autostart")

        self.source = os.path.join(_root, self.filename)
        self.destination = os.path.join(self.distnation_dir, self.filename)

    def enable(self):
        shutil.copyfile(self.source, self.destination)

    def disable(self):
        if os.path.exists(self.destination):
            os.remove(self.destination)

    @property
    def enabled(self):
        return os.path.isfile(self.destination)
