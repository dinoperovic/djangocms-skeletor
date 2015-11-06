# -*- coding: utf-8 -*-
try:
    from .local import *  # noqa
except ImportError:
    from .prod import *  # noqa
