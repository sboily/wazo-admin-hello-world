# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from wazo_admin_ui.helpers.classful import BaseView

class HelloWorldView(BaseView):

    resource = 'hello_world'
    templates = {'list': 'hello_world.html'}

    @classy_menu_item('.hello', 'Hello World', order=1, icon="heart")
    def index(self):
        return super(HelloWorldView, self).index()
