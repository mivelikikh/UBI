import os
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


def read_tables(directory):
    tables = {}
    regions = [file_name for file_name in os.listdir(directory) if os.path.isdir(directory + os.sep + file_name)]
    
    for region in tqdm(regions):
        tables[region] = {}
        
        files = [file_name for file_name in os.listdir(directory + os.sep + region)
                                            if file_name.endswith('.csv') or file_name.endswith('.xlsx')]
        for file_name in files:
            if file_name.endswith('.csv'):
                tables[region][os.path.splitext(file_name)[0]] = pd.read_csv(directory + os.sep + region + os.sep + file_name,
                                                                             sep=';', parse_dates=['Year'])
            elif file_name.endswith('.xlsx'):
                tables[region][os.path.splitext(file_name)[0]] = pd.read_excel(directory + os.sep + region + os.sep + file_name,
                                                                               parse_dates=['Year'])
    
    return tables


def plot_indicator(ax, tables, region, indicator, transform=None,
                   color='black', save=False):
    table = tables[region][indicator]
    
    xlabel = table.columns[0]
    ylabel = table.columns[1]

    if transform is not None:
        ax.plot(table[xlabel], transform(table[ylabel]),
                label=indicator, linewidth=2, color=color)
    else:
        ax.plot(table[xlabel], table[ylabel],
                label=indicator, linewidth=2, color=color)
    
    ax.set_title(region, fontsize=16)
    ax.legend(loc='best', prop={'size': 12})
    
    ax.set_xlabel(xlabel, fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    if save:
        os.makedirs('./plots/', exist_ok=True)
        plt.savefig('./plots/' + region + '_' + indicator + '.png', bbox_inches='tight')
