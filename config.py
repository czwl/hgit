#
#
# Copyright (C) 2020 Czwl Cd
# Website: https://github.com/czwl
#
# SPDX-License-Identifier: Apache-2.0
#

from pathlib import Path
import configparser

cwd = Path.cwd()
config_filename = ".hgitconf"


def read_config(path):
    config = configparser.ConfigParser()
    config.read_string(config_filename)
    return config["config"]["remote"]


def write_config(url):
    cfgfile = cwd.joinpath(config_filename)
    config = configparser.ConfigParser()
    config.add_section("config")
    config.set("config", "remote", url)
    with open(cfgfile, mode="w") as configfile:
        config.write(configfile)
    configfile.close()
