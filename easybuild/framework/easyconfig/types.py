# #
# Copyright 2015-2015 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
# #

"""
Support for checking types of easyconfig parameter values.

@author: Kenneth Hoste (Ghent University)
"""
from vsc.utils import fancylogger

# easy types, that can be verified with isinstance
EASY_TYPES = [basestring, int]
# type checking is skipped for easyconfig parameters names not listed in TYPES
TYPES = {
    'name': basestring,
    'version': basestring,
}


_log = fancylogger.getLogger('easyconfig.types', fname=False)


def check_type_of_param_value(key, value):
    """
    Check value type of specified easyconfig parameter.

    @param key: name of easyconfig parameter
    @param value: easyconfig parameter value, of which type should be checked
    """
    type_ok = True

    if key in TYPES:
        expected_type = TYPES[key]
        if expected_type in EASY_TYPES:
            if isinstance(value, expected_type):
                _log.debug("Value type checking of easyconfig parameter '%s' passed: expected '%s', got '%s'",
                           key, expected_type.__name__, type(value).__name__)
            else:
                type_ok = False
                _log.warning("Value type checking of easyconfig parameter '%s' FAILED: expected '%s', got '%s'",
                             key, expected_type.__name__, type(value).__name__)
    else:
        _log.debug("No type specified for easyconfig parameter '%s', so skipping type check.", key)

    return type_ok