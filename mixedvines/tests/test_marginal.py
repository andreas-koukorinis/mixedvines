# -*- coding: utf-8 -*-
# Copyright (C) 2017 Arno Onken
#
# This file is part of the mixedvines package.
#
# The mixedvines package is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# The mixedvines package is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
'''
This module implements tests for the marginal module.
'''
from mixedvines.marginal import Marginal
import numpy as np
from numpy.testing import assert_allclose


def test_marginal_fit():
    '''
    Tests the fit method.
    '''
    samples = np.linspace(-2, 2, 3)
    # Normal distribution
    marginal = Marginal.fit(samples, True)
    # Comparison values
    r_logpdf = np.array([-2.15935316, -1.40935316, -2.15935316])
    p_logpdf = marginal.logpdf(samples)
    assert_allclose(p_logpdf, r_logpdf)
