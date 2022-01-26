import math
from scipy.stats import ks_2samp, mannwhitneyu


def ks_statistic(tables, regions, indicator, transform=None):
    columns = [tables[region][indicator].columns[1] for region in regions]
    
    if transform is not None:
        statistic, p_value = ks_2samp(transform(tables[regions[0]][indicator][columns[0]]),
                                      transform(tables[regions[1]][indicator][columns[1]]))
    else:
        statistic, p_value = ks_2samp(tables[regions[0]][indicator][columns[0]],
                                      tables[regions[1]][indicator][columns[1]])
    
    return statistic


def U_statistic(tables, regions, indicator, transform=None, alternative='less'):
    columns = [tables[region][indicator].columns[1] for region in regions]
    
    if transform is not None:
        statistic, p_value = mannwhitneyu(transform(tables[regions[0]][indicator][columns[0]]),
                                          transform(tables[regions[1]][indicator][columns[1]]),
                                          alternative=alternative)
    else:
        statistic, p_value = mannwhitneyu(tables[regions[0]][indicator][columns[0]],
                                          tables[regions[1]][indicator][columns[1]],
                                          alternative=alternative)
    
    return statistic


def Z_statistic(u_statistic, size):
    if isinstance(size, tuple):
        n_1, n_2 = size
    else:
        n_1 = size
        n_2 = size
    
    mu = n_1 * n_2 / 2
    sigma = math.sqrt(mu * (n_1 + n_2 + 1) / 6)
        
    return abs(u_statistic - mu) / sigma


def print_statistic(regions, statistic):
    print('{} vs. {}: {:.3f}'.format(regions[0], regions[1], statistic))
