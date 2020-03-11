import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from matplotlib.widgets import Slider
from functools import partial
import matplotlib as mpl



#%%
from rt1.rt1 import RT1, _init_lambda_backend
import copy
from rt1.rtfits import Fits
import sympy as sp

def getbackscatter(SRF=None,
                   V=None,
                   inc=None,
                   params = None,
                   fit = None,
                   use_fitparams = True,
                   fn_input = None,
                   _fnevals_input = None,
                   int_Q = True,
                   lambda_backend=_init_lambda_backend,
                   verbosity=2):

    if inc is None and fit is not None:
        inc = copy.deepcopy(fit.result[1].t_0)

    if params is None and use_fitparams is True:
        params = fit.result[6]
        fixed_dict = fit.result[-1]
        print('!! ATTENTION, using parameters from fit !!')
    elif params is not None and use_fitparams is True:
        fitparams = fit.result[6]
        fixed_dict = fit.result[-1]
        for key, val in params.items():
            fitparams[key] = val
        params = fitparams
    else:
        if params is None:
            params = dict()
            fixed_dict = dict()

    if V is None and fit is not None:
        V = copy.deepcopy(fit.result[1].V)
        print('using V from fit')
    if SRF is None and fit is not None:
        SRF = copy.deepcopy(fit.result[1].SRF)
        print('using SRF from fit')

    if 'bsf' not in params and use_fitparams is True:
        params['bsf']  = fit.result[1].bsf
        print('!! ATTENTION, using bsf from fit !!')
    elif 'bsf' not in params:
        params['bsf']  = 0.
        print('!! ATTENTION, using bsf=0 !!')


    bsf = params['bsf']

    # remove all parameters that are not needed for fn-coefficient evaluation
    # TODO is this necessary??
    #if 'omega' in params: params.pop('omega')
    #if 's2' in params: params.pop('s2')
    #if 'bsf' in params: params.pop('bsf')

    # necessary if t is varied and provided as numerical value instead of sp.symbol
    # in order to correctly evaluate the fn-coefficients
    # TODO this does not work for LinCombV and LinCombSRF !!!
    try:
        SRF._set_function()
        SRF._set_legcoefficients()
    except:
        pass

    R = RT1(1., inc, inc, np.zeros_like(inc), np.full_like(inc, np.pi),
        V=V, SRF=SRF, fn_input=fn_input, _fnevals_input=_fnevals_input,
        geometry='mono', bsf = bsf, param_dict=params, int_Q=int_Q,
        lambda_backend=lambda_backend, verbosity=verbosity)

    ft = Fits(sig0=True, dB=True)
    tot, surf, vol, inter = ft._calc_model(R,
                                           params,
                                           fixed_dict,
                                           return_components=True)

    # get incidence-angles
    incs = R.t_0

    return {'incs' : incs,
            'tot' : tot,
            'surf' : surf,
            'vol' : vol,
            'inter' : inter}




# %%
def printsig0analysis(fitselect,
                      dayrange1=10,
                      printcomponents1=False,
                      secondslider=True,
                      dayrange2=1,
                      printcomponents2=False,
                      printfullt_0=True,
                      printfullASCAT=True,
                      dB = True,
                      sig0=True,
                      printparamnames=None,
                      int_Q=True):

    def dBsig0convert(val, inc,
                      dB, sig0,
                      fitdB=fitselect.dB, fitsig0=fitselect.sig0):
        # if results are provided in dB convert them to linear units
        if fitdB is True: val = 10**(val/10.)
        # convert sig0 to intensity
        if sig0 is False and fitsig0 is True:
            val = val/(4.*np.pi*np.cos(inc))
        # convert intensity to sig0
        if sig0 is True and fitsig0 is False:
            val = 4.*np.pi*np.cos(inc)*val
        # if dB output is required, convert to dB
        if dB is True: val = 10.*np.log10(val)
        return val

    if printparamnames is None:
        printparamnames = fitselect.result[6].keys()

    f = plt.figure(figsize=(10, 6))
    # [left, bottom, width, height]
    #ax = plt.axes([0.05, 0.48, 0.9, 0.5])

    ax = plt.axes([0.05, 0.48, 0.425, 0.5])
    ax.grid()

    ax1 = plt.axes([0.525, 0.48, 0.425, 0.5])
    ax1.grid()

    ax2 = plt.axes([0.05, 0.18, 0.9, 0.25])

    slider_ax = plt.axes([0.15, 0.06, 0.7, 0.04])

    if secondslider:
        slider_bx = plt.axes([0.15, 0.02, 0.7, 0.04])

    # calculate backscatter values
    (_, _, data, _, mask, _, _, _, _) = fitselect.result
    sig0_vals = fitselect._calc_model(R=fitselect.result[1],
                                      res_dict=fitselect.result[6],
                                      fixed_dict = fitselect.result[-1],
                                      return_components=True)

    # apply mask and convert to pandas dataframe
    sig0_vals = [np.ma.masked_array(con, mask) for con in sig0_vals]
    sig0_vals += [np.ma.masked_array(data, mask)]
    # add incidence-angles and indexes
    sig0_vals += [np.ma.masked_array(fitselect.result[1].t_0, mask)]
    sig0_vals += [fitselect.index]
    sig0_vals = dict(zip(['tot', 'surf', 'vol', 'inter', 'ASCAT', 'incs', 'indexes'], sig0_vals))


    # convert to sig0 and dB if necessary
    for key in ['tot', 'surf', 'vol', 'inter', 'ASCAT']:
        sig0_vals[key] = dBsig0convert(sig0_vals[key], sig0_vals['incs'],
                                       dB = dB, sig0=sig0)

#    if fitselect.sig0 is False:
#        for key in ['tot', 'surf', 'vol', 'inter', 'ASCAT']:
#            sig0_vals[key] = 4. * np.pi * np.ma.cos(fitselect.result[1].t_0) * sig0_vals[key]
#    if fitselect.dB is False:
#        for key in ['tot', 'surf', 'vol', 'inter', 'ASCAT']:
#            sig0_vals[key] = 10. * np.ma.log10(sig0_vals[key])


    if printfullt_0 is True:
        inc = np.array([np.deg2rad(np.arange(1, 89, 1))]*len(fitselect.index))
        newsig0_vals = getbackscatter(inc=inc,
                                      fit = fitselect,
                                      use_fitparams = True,
                                      verbosity=1,
                                      int_Q = int_Q
                                      )
        for key in ['tot', 'surf', 'vol', 'inter']:
            newsig0_vals[key] = dBsig0convert(newsig0_vals[key],
                                              newsig0_vals['incs'],
                                              fitdB=True, fitsig0=True,
                                              dB = dB, sig0=sig0)

        ax.set_xlim([-2 + np.rad2deg(np.ma.min(newsig0_vals['incs'])),
                      2 + np.rad2deg(np.ma.max(newsig0_vals['incs']))])
        ax.set_ylim([np.min([np.ma.min(newsig0_vals['tot']), np.ma.min(sig0_vals['ASCAT'])]),
                    np.max([np.ma.max(newsig0_vals['tot']), np.ma.max(sig0_vals['ASCAT'])])])
    else:
        ax.set_xlim([-2 + np.rad2deg(np.ma.min(sig0_vals['incs'][0])),
                      2 + np.rad2deg(np.ma.max(sig0_vals['incs'][0]))])
        ax.set_ylim([np.min([np.ma.min(sig0_vals['tot']), np.ma.min(sig0_vals['ASCAT'])]),
                    np.max([np.ma.max(sig0_vals['tot']), np.ma.max(sig0_vals['ASCAT'])])])


    # print full ASCAT points in the background
    if printfullASCAT is True:
        ax.plot(np.rad2deg(sig0_vals['incs']),
                sig0_vals['ASCAT'], lw=0., marker='.', ms=.5, color = 'k', alpha = 0.5)

    # plot first set of lines
    styledict = {'lw':1, 'marker':'o', 'ms':3, 'color':'k'}
    styledictvol = {'lw':1, 'marker':'o', 'ms':3, 'color':'g', 'markerfacecolor':'gray'}
    styledictsurf = {'lw':1, 'marker':'o', 'ms':3, 'color':'y', 'markerfacecolor':'gray'}
    styledictinter = {'lw':1, 'marker':'o', 'ms':3, 'color':'c', 'markerfacecolor':'gray'}
    styledictASCAT = {'lw':0., 'marker':'s', 'ms':5, 'markerfacecolor':'gray', 'color':'k'}

    # get upper and lower boundaries for the indicator-lines in the timeseries
    for key in printparamnames:
        try:
            indicator_bounds = [np.min({**fitselect.result[6],
                                        **fitselect.result[-1]}[key]),
                                np.max({**fitselect.result[6],
                                        **fitselect.result[-1]}[key])]
            # if a constant value is plotted, ensure that the boundaries
            # are not equal
            if indicator_bounds[0] == indicator_bounds[1]:
                indicator_bounds[1] = indicator_bounds[0]*1.1
                indicator_bounds[0] = indicator_bounds[0]*0.9
            break
        except:
            pass

    lines = []
    for day in np.arange(0, dayrange1, 1):
        lines += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                         sig0_vals['tot'][day], **styledict)
        if printcomponents1:
            lines += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                             sig0_vals['surf'][day], **styledictsurf)
            lines += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                             sig0_vals['vol'][day], **styledictvol)
            lines += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                             sig0_vals['inter'][day], **styledictinter)

        lines += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                         sig0_vals['ASCAT'][day], **styledictASCAT,
                         #color = lines[-1].get_color()
                         )
        lines += ax2.plot([sig0_vals['indexes'][day]]*2, indicator_bounds, 'k')

    lines_frac = []
    for day in np.arange(0, dayrange1, 1):
        lintot = dBsig0convert(sig0_vals['tot'][day], sig0_vals['incs'][day],
                      dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
        linsurf = dBsig0convert(sig0_vals['surf'][day], sig0_vals['incs'][day],
                      dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
        linvol = dBsig0convert(sig0_vals['vol'][day], sig0_vals['incs'][day],
                      dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
        lininter = dBsig0convert(sig0_vals['inter'][day], sig0_vals['incs'][day],
                      dB=False, sig0=False, fitdB=dB, fitsig0=sig0)

        lines_frac += ax1.plot(np.rad2deg(sig0_vals['incs'][day]),
                         linsurf/lintot,
                         **styledictsurf)
        lines_frac += ax1.plot(np.rad2deg(sig0_vals['incs'][day]),
                         linvol/lintot
                         , **styledictvol)
        lines_frac += ax1.plot(np.rad2deg(sig0_vals['incs'][day]),
                         lininter/lintot
                         , **styledictinter)

    # plot first set of full-incidence-angle lines
    linesfull = []
    lines_frac_full = []
    if printfullt_0 is True:
        # plot first set of lines
        styledict = {'lw':.25, 'color':'k'}
        styledictvol = {'lw':.25, 'color':'g'}
        styledictsurf = {'lw':.25, 'color':'y'}
        styledictinter = {'lw':.25, 'color':'c'}

        for day in np.arange(0, dayrange1, 1):
            linesfull += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 newsig0_vals['tot'][day], **styledict)
            if printcomponents1:
                linesfull += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 newsig0_vals['surf'][day], **styledictsurf)
                linesfull += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 newsig0_vals['vol'][day], **styledictvol)
                linesfull += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 newsig0_vals['inter'][day], **styledictinter)
        for day in np.arange(0, dayrange1, 1):
            lintot = dBsig0convert(newsig0_vals['tot'][day], newsig0_vals['incs'][day],
                                   dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
            linsurf = dBsig0convert(newsig0_vals['surf'][day], newsig0_vals['incs'][day],
                                    dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
            linvol = dBsig0convert(newsig0_vals['vol'][day], newsig0_vals['incs'][day],
                                   dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
            lininter = dBsig0convert(newsig0_vals['inter'][day], newsig0_vals['incs'][day],
                                     dB=False, sig0=False, fitdB=dB, fitsig0=sig0)

            lines_frac_full += ax1.plot(np.rad2deg(newsig0_vals['incs'][day]),
                             linsurf/lintot,
                             **styledictsurf)
            lines_frac_full += ax1.plot(np.rad2deg(newsig0_vals['incs'][day]),
                             linvol/lintot
                             , **styledictvol)
            lines_frac_full += ax1.plot(np.rad2deg(newsig0_vals['incs'][day]),
                             lininter/lintot
                             , **styledictinter)


    if secondslider:
        # plot second set of lines
        styledict = {'lw':1, 'marker':'o', 'ms':3, 'dashes':[5, 5], 'color':'r', 'markerfacecolor':'none'}
        styledictvol = {'lw':1, 'marker':'o', 'ms':3, 'dashes':[5, 5], 'color':'g', 'markerfacecolor':'r'}
        styledictsurf = {'lw':1, 'marker':'o', 'ms':3, 'dashes':[5, 5], 'color':'y', 'markerfacecolor':'r'}
        styledictinter = {'lw':1, 'marker':'o', 'ms':3, 'dashes':[5, 5], 'color':'c', 'markerfacecolor':'r'}
        styledictASCAT = {'lw':0., 'marker':'s', 'ms':5, 'markerfacecolor':'none', 'color':'r'}

        lines2 = []
        for day in np.arange(1, dayrange2 + 1, 1):
            lines2 += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                             sig0_vals['tot'][day], **styledict)
            if printcomponents2:
                lines2 += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                                 sig0_vals['surf'][day], **styledictsurf)
                lines2 += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                                 sig0_vals['vol'][day], **styledictvol)
                lines2 += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                                 sig0_vals['inter'][day], **styledictinter)

            lines2 += ax.plot(np.rad2deg(sig0_vals['incs'][day]),
                             sig0_vals['ASCAT'][day], **styledictASCAT,
                             #color = lines2[-1].get_color()
                             )

            lines2 += ax2.plot([sig0_vals['indexes'][day]]*2, indicator_bounds, color='r', ls='--')

        lines_frac2 = []
        for day in np.arange(1, dayrange2 + 1, 1):
            lintot = dBsig0convert(sig0_vals['tot'][day], sig0_vals['incs'][day],
                          dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
            linsurf = dBsig0convert(sig0_vals['surf'][day], sig0_vals['incs'][day],
                          dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
            linvol = dBsig0convert(sig0_vals['vol'][day], sig0_vals['incs'][day],
                          dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
            lininter = dBsig0convert(sig0_vals['inter'][day], sig0_vals['incs'][day],
                          dB=False, sig0=False, fitdB=dB, fitsig0=sig0)

            lines_frac2 += ax1.plot(np.rad2deg(sig0_vals['incs'][day]),
                             linsurf/lintot,
                             **styledictsurf)
            lines_frac2 += ax1.plot(np.rad2deg(sig0_vals['incs'][day]),
                             linvol/lintot
                             , **styledictvol)
            lines_frac2 += ax1.plot(np.rad2deg(sig0_vals['incs'][day]),
                             lininter/lintot
                             , **styledictinter)

        # plot second set of full-incidence-angle lines
        linesfull2 = []
        lines_frac_full2 = []
        if printfullt_0 is True:
            # plot first set of lines
            styledict = {'lw':.25, 'color':'r', 'dashes':[5, 5]}
            styledictvol = {'lw':.25, 'color':'g', 'dashes':[5, 5]}
            styledictsurf = {'lw':.25, 'color':'y', 'dashes':[5, 5]}
            styledictinter = {'lw':.25, 'color':'c', 'dashes':[5, 5]}
            for day in np.arange(1, dayrange2 + 1, 1):
                linesfull2 += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 newsig0_vals['tot'][day], **styledict)
                if printcomponents2:
                    linesfull2 += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                     newsig0_vals['surf'][day], **styledictsurf)
                    linesfull2 += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                     newsig0_vals['vol'][day], **styledictvol)
                    linesfull2 += ax.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                     newsig0_vals['inter'][day], **styledictinter)

            for day in np.arange(1, dayrange2 + 1, 1):
                lintot = dBsig0convert(newsig0_vals['tot'][day], newsig0_vals['incs'][day],
                                       dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                linsurf = dBsig0convert(newsig0_vals['surf'][day], newsig0_vals['incs'][day],
                                        dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                linvol = dBsig0convert(newsig0_vals['vol'][day], newsig0_vals['incs'][day],
                                       dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                lininter = dBsig0convert(newsig0_vals['inter'][day], newsig0_vals['incs'][day],
                                         dB=False, sig0=False, fitdB=dB, fitsig0=sig0)

                lines_frac_full2 += ax1.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 linsurf/lintot,
                                 **styledictsurf)
                lines_frac_full2 += ax1.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 linvol/lintot
                                 , **styledictvol)
                lines_frac_full2 += ax1.plot(np.rad2deg(newsig0_vals['incs'][day]),
                                 lininter/lintot
                                 , **styledictinter)


    # plot WG and LAI from SURFEX and retrieval (if available)
    axparamplot = ax2
    handles, labels = [], []
    i = 0
    for key in printparamnames:
        try:
            if i > 0: axparamplot = ax2.twinx()
            l, = axparamplot.plot(fitselect.index,
                                  {**fitselect.result[6],
                                   **fitselect.result[-1]}[key],
                                   label = key, color='C' + str(i))
            # add handles and labels to legend
            handles += axparamplot.get_legend_handles_labels()[0]
            labels += axparamplot.get_legend_handles_labels()[1]

            # change color of axis to fit color of lines
            axparamplot.yaxis.label.set_color(l.get_color())
            axparamplot.tick_params(axis='y', colors=l.get_color())
            # shift twin-axes if necessary
            if i > 1: axparamplot.spines["right"].set_position(('axes', .95))
            i += 1
        except:
            pass
    axparamplot.legend(handles=handles, labels=labels, loc='upper center', ncol=5)

    ax2.xaxis.set_minor_locator(mpl.dates.MonthLocator())
    ax2.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%m'))

    ax2.xaxis.set_major_locator(mpl.dates.YearLocator())
    ax2.xaxis.set_major_formatter(mpl.dates.DateFormatter('\n%Y'))

    # define function to update lines based on slider-input
    def animate(day0, lines, linesfull,
                lines_frac, lines_frac_full,
                dayrange, printcomponents):

        day0 = int(day0)
        i = 0
        for day in np.arange(day0, day0 + dayrange, 1):
            lines[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))  # update the data
            lines[i].set_ydata(sig0_vals['tot'][day])  # update the data
            i += 1
            if printcomponents:
                lines[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))  # update the data
                lines[i].set_ydata(sig0_vals['surf'][day])  # update the data
                i += 1
                lines[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))  # update the data
                lines[i].set_ydata(sig0_vals['vol'][day])  # update the data
                i += 1
                lines[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))  # update the data
                lines[i].set_ydata(sig0_vals['inter'][day])  # update the data
                i += 1

            # update ascat measurements
            lines[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))
            lines[i].set_ydata(sig0_vals['ASCAT'][day])
            i += 1
            # update day-indicator line
            lines[i].set_xdata([sig0_vals['indexes'][day]]*2)
            i += 1

        i = 0
        for day in np.arange(day0, day0 + dayrange, 1):
                lintot = dBsig0convert(sig0_vals['tot'][day], sig0_vals['incs'][day],
                              dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                linsurf = dBsig0convert(sig0_vals['surf'][day], sig0_vals['incs'][day],
                              dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                linvol = dBsig0convert(sig0_vals['vol'][day], sig0_vals['incs'][day],
                              dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                lininter = dBsig0convert(sig0_vals['inter'][day], sig0_vals['incs'][day],
                              dB=False, sig0=False, fitdB=dB, fitsig0=sig0)

                lines_frac[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))  # update the data
                lines_frac[i].set_ydata(linsurf/lintot)  # update the data
                i += 1
                lines_frac[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))  # update the data
                lines_frac[i].set_ydata(linvol/lintot)  # update the data
                i += 1
                lines_frac[i].set_xdata(np.rad2deg(sig0_vals['incs'][day]))  # update the data
                lines_frac[i].set_ydata(lininter/lintot)  # update the data
                i += 1

        if printfullt_0 is True:
            i = 0
            for day in np.arange(day0, day0 + dayrange, 1):
                linesfull[i].set_xdata(np.rad2deg(newsig0_vals['incs'][day]))  # update the data
                linesfull[i].set_ydata(newsig0_vals['tot'][day])  # update the data
                i += 1
                if printcomponents:
                    linesfull[i].set_xdata(np.rad2deg(newsig0_vals['incs'][day]))  # update the data
                    linesfull[i].set_ydata(newsig0_vals['surf'][day])  # update the data
                    i += 1
                    linesfull[i].set_xdata(np.rad2deg(newsig0_vals['incs'][day]))  # update the data
                    linesfull[i].set_ydata(newsig0_vals['vol'][day])  # update the data
                    i += 1
                    linesfull[i].set_xdata(np.rad2deg(newsig0_vals['incs'][day]))  # update the data
                    linesfull[i].set_ydata(newsig0_vals['inter'][day])  # update the data
                    i += 1
            i = 0
            for day in np.arange(day0, day0 + dayrange, 1):
                    lintot = dBsig0convert(newsig0_vals['tot'][day], newsig0_vals['incs'][day],
                                  dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                    linsurf = dBsig0convert(newsig0_vals['surf'][day], newsig0_vals['incs'][day],
                                  dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                    linvol = dBsig0convert(newsig0_vals['vol'][day], newsig0_vals['incs'][day],
                                  dB=False, sig0=False, fitdB=dB, fitsig0=sig0)
                    lininter = dBsig0convert(newsig0_vals['inter'][day], newsig0_vals['incs'][day],
                                  dB=False, sig0=False, fitdB=dB, fitsig0=sig0)

                    lines_frac_full[i].set_xdata(np.rad2deg(newsig0_vals['incs'][day]))  # update the data
                    lines_frac_full[i].set_ydata(linsurf/lintot)  # update the data
                    i += 1
                    lines_frac_full[i].set_xdata(np.rad2deg(newsig0_vals['incs'][day]))  # update the data
                    lines_frac_full[i].set_ydata(linvol/lintot)  # update the data
                    i += 1
                    lines_frac_full[i].set_xdata(np.rad2deg(newsig0_vals['incs'][day]))  # update the data
                    lines_frac_full[i].set_ydata(lininter/lintot)  # update the data
                    i += 1

        return lines

    # define function to update slider-range based on zoom
    def updatesliderboundary(evt, slider):
        indexes = sig0_vals['indexes']
        # Get the range for the new area
        xstart, ystart, xdelta, ydelta = ax2.viewLim.bounds
        xend = xstart + xdelta

        # convert to datetime-objects and ensure that they are in the
        # same time-zone as the sig0_vals indexes
        xend = mpl.dates.num2date(xend).replace(tzinfo=sig0_vals['indexes'].tzinfo)
        xstart = mpl.dates.num2date(xstart).replace(tzinfo=sig0_vals['indexes'].tzinfo)

        zoomindex = np.where(np.logical_and(indexes > xstart, indexes < xend))[0]


        slider.valmin = zoomindex[0]
        slider.valmax = zoomindex[-1]

        slider.ax.set_xlim(slider.valmin,
                             slider.valmax)


    # create the slider
    a_slider = Slider(slider_ax,            # the axes object containing the slider
                      'solid lines',        # the name of the slider parameter
                      1.,                   # minimal value of the parameter
                      len(fitselect.index), # maximal value of the parameter
                      valinit=1.,  # initial value of the parameter
                      valfmt="%i"   # print slider-value as integer
                      )

    # set slider to call animate function when changed
    a_slider.on_changed(partial(animate,
                                lines=lines,
                                linesfull=linesfull,
                                lines_frac = lines_frac,
                                lines_frac_full = lines_frac_full,
                                dayrange=dayrange1,
                                printcomponents=printcomponents1))

    # update slider boundary with respect to zoom of second plot
    ax2.callbacks.connect('xlim_changed', partial(updatesliderboundary,
                                                  slider=a_slider))

    if secondslider:
        # here we create the slider
        b_slider = Slider(slider_bx,             # the axes object containing the slider
                          'dashed lines',        # the name of the slider parameter
                          1.,                    # minimal value of the parameter
                          len(fitselect.index),  # maximal value of the parameter
                          valinit=2.,            # initial value of the parameter
                          valfmt="%i"
                          )

        b_slider.on_changed(partial(animate,
                                    lines=lines2,
                                    linesfull=linesfull2,
                                    lines_frac = lines_frac2,
                                    lines_frac_full = lines_frac_full2,
                                    dayrange=dayrange2,
                                    printcomponents=printcomponents2))

        ax2.callbacks.connect('xlim_changed', partial(updatesliderboundary,
                                                      slider=b_slider))


    # !!! a reference to the sliders must be returned in order to be interactive !!!
    if secondslider:
        return f, a_slider, b_slider
    else:
        return f, a_slider



# %%
#resultsdict['BF_invert_WG_precalib']
#_ = printsig0analysis(inversefit0[0],
#                  dayrange1 = 5,
#                  dayrange2 = 1,
#               '   secondslider=False,
#                  printcomponents1 = True,
#                  printcomponents2 = True)
#
#
#_ = printsig0analysis(resultsdict['BF_invert_WG_precalib'][5],
#                  dayrange1 = 10,
#                  dayrange2 = 1,
#                  secondslider=True,
#                  printcomponents1 = False,
#                  printcomponents2 = True)
