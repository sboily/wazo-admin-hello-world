# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import Blueprint
from flask_menu.classy import register_flaskview


from .view import HelloWorldView

hello_world = Blueprint('hello_world', __name__, template_folder='templates',
                        static_folder='static', static_url_path='/%s' % __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        HelloWorldView.register(hello_world, route_base='/hello')
        register_flaskview(hello_world, HelloWorldView)

        core.register_blueprint(hello_world)
