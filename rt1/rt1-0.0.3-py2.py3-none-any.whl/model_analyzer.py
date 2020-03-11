from rt1.rt1 import RT1
import copy
from rt1.rtfits import Fits
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def getbackscatter(fit = None,
                   SRF=None,
                   V=None,
                   inc=None,
                   params = None,
                   use_fitparams = True,
                   fn_input = None,
                   _fnevals_input = None,
                   int_Q = False,
                   dB=True,
                   sig0=True,
                   lambda_backend='cse_symengine_sympy',
                   verbosity=2):
    '''
    calculate the backscatter based on an input of a rtfits object or
    SRF and V
    '''

    # get incidence-angle from fit if inc is not provided explicitly
    if inc is None and fit is not None:
        inc = copy.deepcopy(fit.result[1].t_0)

    # get parameters from fit if use_fitparams is True
    fitparams = {}
    if use_fitparams is True:
        fitparams = {**fit.result[6], **fit.result[-1]}
    if params is not None:
        for key, val in params.items():
            fitparams[key] = val

    if 'bsf' not in fitparams and use_fitparams is True:
        fitparams['bsf']  = fit.result[1].bsf[0]
    elif 'bsf' not in fitparams:
        fitparams['bsf']  = 0.

    # get V and SRF from fit if not provided explicitly
    if V is None and fit is not None:
        V = copy.deepcopy(fit.result[1].V)
    else:
        V = copy.deepcopy(V)
    if SRF is None and fit is not None:
        SRF = copy.deepcopy(fit.result[1].SRF)
    else:
        SRF = copy.deepcopy(SRF)
    # necessary if t is varied and provided as numerical value instead
    #  of sp.symbol in order to correctly evaluate the fn-coefficients
    #SRF._set_function()
    #SRF._set_legcoefficients()

    R = RT1(1., inc, inc, np.zeros_like(inc), np.full_like(inc, np.pi),
        V=V, SRF=SRF, fn_input=fn_input, _fnevals_input=_fnevals_input,
        geometry='mono', bsf = fitparams['bsf'], param_dict=fitparams,
        int_Q=int_Q, lambda_backend=lambda_backend, verbosity=verbosity)

    ft = Fits(sig0=sig0, dB=dB)
    tot, surf, vol, inter = ft._calc_model(R,
                                           fitparams,
                                           return_components=True)

    return {'inc' : inc,
            'tot' : tot,
            'surf' : surf,
            'vol' : vol,
            'inter' : inter,
            '_fnevals': R._fnevals}




from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons
from functools import partial
from matplotlib import gridspec
import copy

def analyzemodel(fit=None, SRF=None, V=None,
                 varyparams = {'WG':[0.05, 1.], 'LAI':[0.05, 2.], 'omega':[.05, .5], 'bsf':[.05, .5]},
                 startparams = {'WG':.2},
                 labels = {'WG':'soil moisture'},
                 dB=True, sig0=True, int_Q=False,
                 fillcomponents=False,
                 componentvariations = False):

    #assert not int_Q, 'NOT yet implemented!'
    if fit is not None:
        _fnevals_input = fit.result[1]._fnevals
    else:
        _fnevals_input = None


    if fit is not None:
        fitdB = fit.dB
        fitsig0 = fit.sig0
    else:
        fitdB = dB
        fitsig0 = sig0

    def dBsig0convert(val, inc,
                      dB, sig0,
                      fitdB=fitdB, fitsig0=fitsig0):
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



    inc = np.array([np.deg2rad(np.linspace(1, 89, 100))])

    # if fit is provided set all parameter that are not varied to the fist
    # values provided in the fit
    if fit is not None:
        params ={key : np.array([val[0]]) for key, val in {**fit.result[6], **fit.result[-1]}.items()}
    else:
        params = {}


    for key, val in varyparams.items():
        if key in startparams:
            print('setting startparam')
            params[key] = np.array([startparams[key]])
        else:
            params[key] = np.array([np.mean(val)])

    modelresult = getbackscatter(fit=fit, V=V, SRF=SRF, int_Q=int_Q, inc=inc,
                                 use_fitparams=False, params=params,
                                 dB=dB, sig0=sig0,
                                 _fnevals_input = _fnevals_input)

    _fnevals_input = modelresult['_fnevals']

    f = plt.figure(figsize=(12,9))
    f.subplots_adjust(top=0.93, right=0.98, left=0.07)
                  # generate figure grid and populate with axes
    gs = gridspec.GridSpec(1 + len(varyparams)//2, 1 + 3 ,
                       height_ratios=[8] + [1]*(len(varyparams) // 2),
                       width_ratios=[.75, 1, 1, 1]
                       )
    gsbuttonslider = gridspec.GridSpec(1 + len(varyparams)//2, 1 + 3 ,
                   height_ratios=[8] + [1]*(len(varyparams) // 2),
                   width_ratios=[.75, 1, 1, 1]
                   )


    gs.update(wspace=.3)
    gsbuttonslider.update(wspace=.3, bottom=0.05)

    ax = plt.subplot(gs[0,0:])
    paramaxes = {}
    col = 0
    for i, key in enumerate(varyparams):
        if i%3 == 0: col += 1
        paramaxes[key] = plt.subplot(gsbuttonslider[col, 1 + i%3])

    buttonax = plt.subplot(gsbuttonslider[1:, 0])


    # plot data
    try:
        ax.plot(fit.result[1].t_0.T,
                dBsig0convert(fit.result[2].T, fit.result[1].t_0.T, dB, sig0), '.')
    except:
        pass

    # plot initial curves
    ltot, = ax.plot(modelresult['inc'].T, modelresult['tot'].T, 'k', label = 'total contribution')

    lsurf, = ax.plot(modelresult['inc'].T, modelresult['surf'].T, 'b', label = 'surface contribution')

    lvol, = ax.plot(modelresult['inc'].T, modelresult['vol'].T, 'g', label = 'volume contribution')

    if int_Q is True:
        lint, = ax.plot(modelresult['inc'].T, modelresult['inter'].T, 'y', label = 'interaction contribution')

    if componentvariations is True:
        ltotmin, = ax.plot(modelresult['inc'].T, modelresult['tot'].T, 'k', lw=0.5, dashes=[5,5])
        ltotmax, = ax.plot(modelresult['inc'].T, modelresult['tot'].T, 'k', lw=0.5, dashes=[5,5])
        lsurfmin, = ax.plot(modelresult['inc'].T, modelresult['surf'].T, 'b', lw=0.5, dashes=[5,5])
        lsurfmax, = ax.plot(modelresult['inc'].T, modelresult['surf'].T, 'b', lw=0.5, dashes=[5,5])
        lvolmin, = ax.plot(modelresult['inc'].T, modelresult['vol'].T, 'g', lw=0.5, dashes=[5,5])
        lvolmax, = ax.plot(modelresult['inc'].T, modelresult['vol'].T, 'g', lw=0.5, dashes=[5,5])
        if int_Q is True:
            lintmin, = ax.plot(modelresult['inc'].T, modelresult['inter'].T, 'y', lw=0.5, dashes=[5,5])
            lintmax, = ax.plot(modelresult['inc'].T, modelresult['inter'].T, 'y', lw=0.5, dashes=[5,5])



    if dB is True: ax.set_ylim(-35, 5)
    ax.set_xticks(np.deg2rad(np.arange(5,95, 10)))
    ax.set_xticklabels(np.arange(5,95, 10))

    # a legend for the lines
    leg0 = ax.legend(ncol=4, bbox_to_anchor=(.5, 1.1), loc='upper center')
    # add the line-legend as individual artist
    ax.add_artist(leg0)

    if dB is True and sig0 is True: ax.set_ylabel(r'$\sigma_0$ [dB]')
    if dB is True and sig0 is False: ax.set_ylabel(r'$I/I_0$ [dB]')
    if dB is False and sig0 is True: ax.set_ylabel(r'$\sigma_0$')
    if dB is False and sig0 is False: ax.set_ylabel(r'$I/I_0$')

    ax.set_xlabel(r'$\theta_0$ [deg]')


    # create the slider for the parameter
    paramslider = {}
    buttonlabels = []
    for key, val in varyparams.items():
        # replace label of key with provided label
        if key in labels:
            keylabel = labels[key]
        else:
            keylabel = key
        buttonlabels += [keylabel]
        if key in startparams:
            startval = startparams[key]
        else:
            startval = np.mean(val)
        paramslider[key] = Slider(paramaxes[key],             # the axes object containing the slider
                          keylabel,                                # the name of the slider parameter
                          val[0],                             # minimal value of the parameter
                          val[1],                             # maximal value of the parameter
                          startval,                           # initial value of the parameter
                          #valfmt="%i"                        # print slider-value as integer
                          color='gray')
        paramslider[key].label.set_position([.05, 0.5])
        paramslider[key].label.set_bbox(dict(boxstyle="round,pad=0.5", facecolor='w'))
        paramslider[key].label.set_horizontalalignment('left')
        paramslider[key].valtext.set_position([.8, 0.5])


    buttons = CheckButtons(buttonax, buttonlabels, [False for i in buttonlabels])

    # define function to update lines based on slider-input
    def animate(value, key):

        params[key] = np.array([value])
        modelresult = getbackscatter(fit=fit, V=V, SRF=SRF, int_Q=int_Q, inc=inc,
                                     use_fitparams=False, params=params,
                                     dB=dB, sig0=sig0,
                                     _fnevals_input = _fnevals_input)
        # update the data
        ltot.set_ydata(modelresult['tot'].T)
        lsurf.set_ydata(modelresult['surf'].T)
        lvol.set_ydata(modelresult['vol'].T)
        if int_Q is True: lint.set_ydata(modelresult['inter'].T)

        # poverprint boundaries
        hatches = ['//', '\\\ ', '+', 'oo', '--', '..']
        colors = ['C' + str(i) for i in range(10)]
        ax.collections.clear()
        legendhandles = []
        for i, [key_i, key_Q] in enumerate(printvariationQ.items()):
            # replace label of key_i with provided label
            if key_i in labels:
                keylabel = labels[key_i]
            else:
                keylabel = key_i

            # reset color of text-backtround
            paramslider[key_i].label.get_bbox_patch().set_facecolor('w')
            if key_Q is True:
                # set color of text-background to hatch-color
                #paramslider[key_i].label.set_color(colors[i%len(colors)])
                paramslider[key_i].label.get_bbox_patch().set_facecolor(colors[i%len(colors)])

                fillparams = copy.deepcopy(params)
                fillparams[key_i] = np.array([varyparams[key_i][0]])
                modelresultmin = getbackscatter(fit=fit, V=V, SRF=SRF, int_Q=int_Q, inc=inc,
                                     use_fitparams=False, params=fillparams,
                                     dB=dB, sig0=sig0,
                                     _fnevals_input = _fnevals_input)

                fillparams[key_i] = np.array([varyparams[key_i][1]])
                modelresultmax = getbackscatter(fit=fit, V=V, SRF=SRF, int_Q=int_Q, inc=inc,
                                     use_fitparams=False, params=fillparams,
                                     dB=dB, sig0=sig0,
                                     _fnevals_input = _fnevals_input)

                if componentvariations is True:
                    # update minimum and maximum lines
                    ltotmin.set_ydata(modelresultmin['tot'].T)
                    lsurfmin.set_ydata(modelresultmin['surf'].T)
                    lvolmin.set_ydata(modelresultmin['vol'].T)
                    if int_Q is True: lintmin.set_ydata(modelresultmin['inter'].T)

                    ltotmax.set_ydata(modelresultmax['tot'].T)
                    lsurfmax.set_ydata(modelresultmax['surf'].T)
                    lvolmax.set_ydata(modelresultmax['vol'].T)
                    if int_Q is True: lintmax.set_ydata(modelresultmax['inter'].T)
#

                legendhandles += [ax.fill_between(modelresultmax['inc'].T.flatten(),
                                modelresultmax['tot'].T.flatten(),
                                modelresultmin['tot'].T.flatten(), facecolor='none', hatch=hatches[i%len(hatches)], edgecolor=colors[i%len(colors)], label = 'total variability (' + keylabel + ')')]
                if fillcomponents is True:
                    legendhandles += [ax.fill_between(modelresultmax['inc'].T.flatten(),
                                    modelresultmax['surf'].T.flatten(),
                                    modelresultmin['surf'].T.flatten(), color='b', alpha = 0.1, label = 'surf variability (' + keylabel + ')')]

                    legendhandles += [ax.fill_between(modelresultmax['inc'].T.flatten(),
                                    modelresultmax['vol'].T.flatten(),
                                    modelresultmin['vol'].T.flatten(), color='g', alpha = 0.1, label = 'vol variability (' + keylabel + ')')]
                    if int_Q is True:
                        legendhandles += [ax.fill_between(modelresultmax['inc'].T.flatten(),
                                        modelresultmax['inter'].T.flatten(),
                                        modelresultmin['inter'].T.flatten(), color='y', alpha = 0.1, label = 'int variability (' + keylabel + ')')]
            # a legend for the hatches
            leg1 = ax.legend(handles=legendhandles, labels=[i.get_label() for i in legendhandles])
            if len(legendhandles) == 0: leg1.remove()

    printvariationQ = {key: False for key in varyparams}
    def buttonfunc(label):
        # in case the labels of the buttons have been changed by the labels-argument
        # set the name to the corresponding key (i.e. the actual parameter name)
        for key, val in labels.items():
            if label == val:
                label = key

        #ax.collections.clear()

        if printvariationQ[label] is True:
            ax.collections.clear()
            printvariationQ[label] = False
        elif printvariationQ[label] is False:
            printvariationQ[label] = True

        animate(paramslider[label].val, label)
        plt.draw()

    buttons.on_clicked(buttonfunc)

    for key, slider in paramslider.items():
        slider.on_changed(partial(animate, key=key))

    return f, paramslider, buttons

