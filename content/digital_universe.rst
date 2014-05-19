================
Digital Universe
================

:date: 2014-05-05 23:24
:tags: alan, turing, dyson, computing
:category: computing
:slug: digital_universe

..

    "In the digital universe, there are two kinds of bits:
    bits that represent structures (differences in space)
    and bits that represent sequence (differences in time).
    Digital computers - as formalized by Alan Turing, and
    developed by John von Neumann - are devices that translate
    between these two species of bits according to definite rules."

    -- George Dyson: Turing's Cathedral

.. code-block:: python

    import sys
    import os

    import matplotlib.pyplot as plt
    from pandas import read_table

    def header(data):
        with open(data, 'rt') as dat:
            return dat.readline().split()[-4:]

    def main(data):
        month, day, time, year = header(data)

        df = read_table(
                data,
                skiprows=6,
                header=0,
                comment='*',
                usecols=['toptemp', 'bottemp', 'chpress', 'membpress', 'force'])

        name = data.strip('.dat').split('/')[-1].strip('lid bond').strip('basebond').strip()

        fig, axes = plt.subplots(nrows=5, ncols=1, dpi=400)

        for iteration, param in enumerate(df.columns):
            df[param].plot(kind='line',
                           ax=axes[iteration],
                           figsize=(16,28),
                           title=param,
                           linewidth=2)

            axes[iteration].set_xlabel('{date}: {time}'.format(time=time, date=' '.join([month,day,year])), fontsize=14)
            axes[iteration].set_title('{var} vs time'.format(var=param), fontsize=18)
            axes[iteration].set_ylabel(param, fontsize=16)
            axes[iteration].set_xticklabels('')

        plt.savefig('{year} {month}_{day}_{name}.png'.format(year=year,month=month,day=day,name=name))


    if __name__ == '__main__':
        if not os.path.isfile(sys.argv[1]):
            sys.stderr.write('file {0} does not exist\n'.format(sys.argv[1]))
            sys.exit(1)
        main(sys.argv[1])
