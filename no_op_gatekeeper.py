# Copyright (c) 2019-2020 Tim Burke
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

from swift.common import utils


def filter_factory(global_conf, **local_conf):
    conf = dict(global_conf, **local_conf)
    no_log = utils.config_true_value(conf.get("no_log"))

    def filter(app):
        if not no_log:
            logger = utils.get_logger(conf)
            logger.warning("Using INSECURE, DANGEROUS no-op gatekeeper!")

        def new_app(env, start_response):
            env['swift_owner'] = True
            env['reseller_request'] = True
            env.setdefault('HTTP_X_BACKEND_ALLOW_RESERVED_NAMES', 'True')
            env.setdefault('HTTP_X_BACKEND_ALLOW_PRIVATE_METHODS', 'True')
            return app(env, start_response)

        return new_app

    return filter
