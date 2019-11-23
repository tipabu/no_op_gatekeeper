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
