# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from . import models
from .hooks import post_init_hook, pre_init_hook

assert models
assert pre_init_hook
assert post_init_hook
