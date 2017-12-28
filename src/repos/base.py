#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Repos API
# Copyright (c) 2008-2017 Hive Solutions Lda.
#
# This file is part of Hive Repos API.
#
# Hive Repos API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Repos API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Repos API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

BASE_URL = "https://repos.bemisc.com/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """

class API(appier.API):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("REPOS_BASE_URL", BASE_URL)
        self.username = appier.conf("REPOS_USERNAME", None)
        self.password = appier.conf("REPOS_PASSWORD", None)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.username = kwargs.get("username", self.username)
        self.password = kwargs.get("password", self.password)
        self._build_url()

    def _build_url(self):
        if not self.username:
            raise appier.OperationalError(message = "No username provided")
        if not self.password:
            raise appier.OperationalError(message = "No password provided")
        parsed = appier.legacy.urlparse(self.base_url)
        self.base_url = "%s://%s:%s@%s/" % (
            parsed.scheme,
            self.username,
            self.password,
            self.base_url
        )
