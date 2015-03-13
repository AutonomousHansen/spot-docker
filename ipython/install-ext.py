#!/usr/bin/ipython3

import os
from IPython.html.services.config import ConfigManager
from IPython.utils.path import locate_profile

if __name__ == '__main__':
    cm = ConfigManager(profile_dir = locate_profile('rise'))
    cm.update('notebook', {"load_extensions": { 'IPython-notebook-extensions/usability/hide_input': True, 'IPython-notebook-extensions/usability/hide_input_all': True }})

