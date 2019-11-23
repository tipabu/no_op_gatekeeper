# Copyright (c) 2019 Tim Burke
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

setuptools.setup(
    name="no_op_gatekeeper",
    author="Tim Burke",
    author_email="tim.burke@gmail.com",
    url="https://github.com/tipabu/no-op-gatekeeper",
    version="1.0",
    description="An insecure no-op gatekeeper for OpenStack Swift",
    long_description="""
No-op Gatekeeper
================

OpenStack Swift has a ``gatekeeper`` middleware that gets automatically
inserted in ``proxy-server`` pipelines if not present. Its job is to
act as a firewall, both preventing Swift internals like backend and
sysmeta headers from leaking out to the client and also ensuring that
such headers coming from clients are ignored.

That's all well and good, but sometimes as a developer you just want a
persistent ``internal_client`` with ``curl`` as an interface. This lets
you have that.

Usage
-----
Update your ``[filter:gatekeeper]`` to look like::

   [filter:gatekeeper]
   use = egg:no_op_gatekeeper#gatekeeper
   # no_log = false
""".strip(),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: OpenStack",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Software Development",
    ],
    py_modules=["no_op_gatekeeper"],
    requires=["swift"],
    entry_points={
        "paste.filter_factory": "gatekeeper = no_op_gatekeeper:filter_factory"
    },
)
