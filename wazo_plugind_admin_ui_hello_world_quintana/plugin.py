# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint

from .view import HelloWorldView

hello_world = create_blueprint('hello_world', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        HelloWorldView.register(hello_world, route_base='/hello')
        register_flaskview(hello_world, HelloWorldView)

        core.register_blueprint(hello_world)
