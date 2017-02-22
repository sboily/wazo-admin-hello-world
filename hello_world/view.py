# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import render_template

from flask_menu.classy import classy_menu_item
from flask_classful import FlaskView

class HelloWorldView(FlaskView):

    @classy_menu_item('.hello', 'Hello World', order=1, icon="heart")
    def index(self):
        return render_template('hello_world.html')
