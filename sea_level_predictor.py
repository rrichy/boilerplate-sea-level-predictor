import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
    # Read data from file
    df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/epa-sea-level.csv')

    # Create scatter plot
    ax = df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter', figsize=(16,9))

    # Create first line of best fit
    lin1 = linregress(df.iloc[:, 0].values, df.iloc[:, 1].values)

    bf1 = pd.DataFrame({'Year': [year for year in range(1880, 2051)],
        '1880-2050 Bestfit': [lin1.intercept + lin1.slope*year for year in range(1880, 2051)]})

    # Create second line of best fit
    lin2 = linregress(df.loc[df['Year'] >= 2000, 'Year'].values, df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'].values)

    bf2 = pd.DataFrame({'Year': [year for year in range(2000, 2051)],
        '2000-2050 Bestfit': [lin2.intercept + lin2.slope*year for year in range(2000, 2051)]})

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')
    
    bf1.plot(x='Year', y='1880-2050 Bestfit', ax=ax)
    bf2.plot(x='Year', y='2000-2050 Bestfit', ax=ax)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()