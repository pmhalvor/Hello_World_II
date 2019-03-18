from numpy import genfromtxt

class MassRadiusObservations:
    """
    Lightweight class storing data complied by Joyce et al. (2018), MNRAS 
    479, 1612 (Table 4).  To use:
    
    In [1]: from observations import MassRadiusObservations

    In [2]: obs = MassRadiusObservations()

    In [3]: obs.mass
    Out[3]: 
    array([ 0.927,  0.607,  0.643,  0.541,  0.59 ,  0.398,  0.277,  0.729,
            0.543,  0.723,  0.559,  0.524,  0.633,  0.376])

    In [4]: obs.radius
    Out[4]: 
    array([ 0.802,  1.461,  1.457,  1.34 ,  1.378,  1.418,  1.464,  1.235,
            1.42 ,  1.717,  2.183,  1.452,  1.993,  1.504])

    In [5]: obs.radius_err
    Out[5]: 
    array([ 0.011,  0.009,  0.036,  0.013,  0.011,  0.009,  0.018,  0.018,
            0.014,  0.009,  0.043,  0.024,  0.009,  0.042])
    
    and so on.  See the test at bottom for an example.
    """

    def __init__(self):
        self._data = genfromtxt(\
            'Joyce.txt',
            delimiter=[16,12,7,7,12,8],
            names=['source','instrument','R','R_err','M','M_err'],
            dtype=['S16','S12','f8','f8','f8','f8'],
            autostrip=True) 

    @property
    def source(self):
        return [str(s,'utf-8') for s in self._data['source']]

    @property
    def instrument(self):
        return [str(s,'utf-8') for s in self._data['instrument']]

    @property
    def mass(self):
        return self._data['M']

    @property
    def radius(self):
        return self._data['R']

    @property
    def mass_err(self):
        return self._data['M_err']

    @property
    def radius_err(self):
        return self._data['R_err']

    def gen_latex_table(self):
        lines=[ r'\begin{tabular}{llrrrr}' ]
        lines.append(\
        "source     & instrument & $M$   & $\Delta M$ & $R$ & $\Delta R$ \\")
        lines.append(\
        "           &     & \multicolumn{2}{c}{$(\Msun)$} & \multicolumn{2}{c}{$(0.01\,\Rsun)$}\\")
        lines.append("\hline")
        for s, i, m, r, me, re in zip(\
                self.source, self.instrument, self.mass, self.radius,
                self.mass_err, self.radius_err):
            lines.append(r'{0:16s} & {1:4s} & {2:5.3f} & {3:5.3f} & {4:5.3f} & {5:5.3f}\\'.format(s,i,m,me,r,re))
        lines.append(r'\end{tabular}')
        return lines


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    obs = MassRadiusObservations()
    plotfile = 'MR_Joyce.png'
    plt.xlabel(r'$M/M_\odot$')
    plt.ylabel(r'$R/(0.01\,R_\odot)$')
    plt.errorbar(obs.mass,obs.radius,\
        yerr=obs.radius_err,xerr=obs.mass_err,fmt='ko',markersize=4)
    plt.savefig(plotfile)
    print('saving plot to {}'.format(plotfile))
