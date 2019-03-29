from __future__ import division, print_function
from write_to_file import save_single_histograms, write_csv_rasters
from plotfunctions import single_in_cohort_soc_plot, make_RasterPlot, single_heat_map
import utility_functions as utils
import numpy as np

def evaluate_whole_experiment(ehd, cf, main_directory, prefix, func, fname, xlabel, ylabel, title, args=[], remove_mouse=None):
    phases = cf.sections()
    phases = utils.filter_dark(phases)
    mice = [mouse[-4:] for mouse in ehd.mice]
    add_info_mice = utils.add_info_mice_filename(remove_mouse)
    result = np.zeros((len(phases), len(mice), len(mice)))
    fname_ = '%s_%s%s.csv' % (fname, prefix, add_info_mice)
    hist_dir = fname + '/histograms'
    rast_dir = fname + '/raster_plots'
    for i, phase in enumerate(phases):
        if len(args):
            result[i] = func(ehd, cf, phase, *args)
        else:
            result[i] = func(ehd, cf, phase)
        save_single_histograms(result[i],
                               fname,
                               ehd.mice,
                               phase,
                               main_directory,
                               hist_dir,
                               prefix,
                               additional_info=add_info_mice)
        single_heat_map(result[i],
                        fname,
                        main_directory,
                        mice,
                        prefix,
                        phase,
                        xlabel=xlabel,
                        ylabel=ylabel,
                        subdirectory=hist_dir,
                        vmax=None,
                        vmin=None,
                        xticks=mice,
                        yticks=mice)
    write_csv_rasters(ehd.mice,
                      phases,
                      result,
                      main_directory,
                      rast_dir,
                      fname_)
    make_RasterPlot(main_directory,
                    rast_dir,
                    result,
                    phases,
                    fname_,
                    mice,
                    title=title)
