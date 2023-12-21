# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date:   2023-12-21 11:36:15
# @Last Modified by:   SashaChernykh
# @Last Modified time: 2023-12-21 11:36:43
from crtime import get_crtimes_in_dir

for fname, date in get_crtimes_in_dir(
        ".", raise_on_error=True, as_epoch=False):
    print(fname, date)
