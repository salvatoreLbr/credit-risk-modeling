import numpy as np
from typing import Tuple

from src.credit_risk_modeling.utils import get_binomial_coefficient


def indipendent_binomial_loss_distribution_simulation(
    n: int, m: int, p: np.array, c: np.array
) -> np.array:
    """Generate indipendent binomial loss distribution.

    Args:
        n: counterparty's number
        m: # of simulation
        p: success's probability
        c: costant exposure for all counterparties
        alpha: significance level

    Returns:
        A numpy array content sorted loss distribution

    """
    u = np.random.uniform(0, 1, [m, n])
    default_indicator = np.where(u < p, 1, 0)
    loss_distribution = np.dot(default_indicator, c)
    sorted_loss_distribution = np.sort(loss_distribution)

    return sorted_loss_distribution


def indipendent_binomial_loss_distribution_analytic(
    N: int, p: float
) -> Tuple[np.array, np.array]:
    """Given N and p get pmf (probability mass function) and cdf (cumulative density function) of an indipendent binomial loss distribution.

    Args:
        N: counterparty's number
        p: default probability (common for each obligor)

    Returns:
        A tuple contains two array: the pmf distribution and the cdf distribution.
    """
    pmf_binomial = np.zeros(N + 1)
    for i in range(N + 1):
        pmf_binomial[i] = (
            get_binomial_coefficient(N, i) * (p**i) * ((1 - p) ** (N - i))
        )
    cdf_binomial = np.cumsum(pmf_binomial)

    return pmf_binomial, cdf_binomial
