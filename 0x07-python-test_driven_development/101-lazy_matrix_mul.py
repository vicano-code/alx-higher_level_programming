#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul

function that multiplies 2 matrices by using the module NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy"""

    return np.dot(m_a, m_b)
