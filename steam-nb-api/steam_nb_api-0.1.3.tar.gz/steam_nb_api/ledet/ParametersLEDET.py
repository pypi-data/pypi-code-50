import os

import numpy as np
import datetime
import xlrd
import xlsxwriter

from steam_nb_api.resources.ResourceReader import ResourceReader


class ParametersLEDET:
    '''
        Class of LEDET parameters
    '''

    def __init__(self):
        self.variablesInputs = None
        self.variablesOptions = None
        self.variablesPlots = None
        self.variablesVariables = None
        self.variableGroupInputs = None
        self.variableGroupOptions = None
        self.variableGroupPlots = None
        self.variableGroupVariables = None


        # Load and set the default LEDET parameters
        self.fileDefaultParameters = os.path.join('ledet', 'variableNamesDescriptions.xlsx')
        self.loadDefaultParameters(self.fileDefaultParameters)


    def setParameters(self, variablesInputs, variablesOptions, variablesPlots , variablesVariables):
        self.variablesInputs, self.variablesOptions, self.variablesPlots, self.variablesVariables = variablesInputs, variablesOptions, variablesPlots, variablesVariables


    def setVariableGroupInputs(self, variableGroupInputs):
        self.variableGroupInputs = variableGroupInputs


    def setVariableGroupOptions(self, variableGroupOptions):
        self.variableGroupOptions = variableGroupOptions


    def setVariableGroupPlots(self, variableGroupPlots):
        self.variableGroupPlots = variableGroupPlots


    def setVariableGroupVariables(self, variableGroupVariables):
        self.variableGroupVariables = variableGroupVariables


    def loadDefaultParameters(self, fileDefaultParameters: str):
        '''
            **Loads and sets the default LEDET parameters **

            Function to load and set the default LEDET parameters

            :param fileName: String defining the name of the file defining the default LEDET parameters
            :type fileName: str

            :return: None
        '''

        # Load default LEDET parameters
        # Read variable names and descriptions
        fullfileName = ResourceReader.getResourcePath(fileDefaultParameters)
        # print(fullfileName) # for debug
        workbookVariables = xlrd.open_workbook(fullfileName)

        # Load "Inputs" sheet
        worksheetInputs = workbookVariables.sheet_by_name('Inputs')
        variablesInputs = {}
        for i in range(worksheetInputs.nrows):
            variablesInputs[str(worksheetInputs.cell(i, 1).value)] = str(worksheetInputs.cell(i, 0).value)

        # Load "Options" sheet
        worksheetOptions = workbookVariables.sheet_by_name('Options')
        variablesOptions = {}
        for i in range(worksheetOptions.nrows):
            variablesOptions[str(worksheetOptions.cell(i, 1).value)] = str(worksheetOptions.cell(i, 0).value)

        # Load "Plots" sheet
        worksheetPlots = workbookVariables.sheet_by_name('Plots')
        variablesPlots = {}
        for i in range(worksheetPlots.nrows):
            variablesPlots[str(worksheetPlots.cell(i, 1).value)] = str(worksheetPlots.cell(i, 0).value)

        # Load "Variables" sheet
        worksheetVariables = workbookVariables.sheet_by_name('Variables')
        variablesVariables = {}
        for i in range(worksheetVariables.nrows):
            variablesVariables[str(worksheetVariables.cell(i, 1).value)] = str(worksheetVariables.cell(i, 0).value)

        # Set parameters
        self.setParameters(variablesInputs, variablesOptions, variablesPlots, variablesVariables)

    def addVariablesInputs(self,
                           T00, l_magnet, I00, M_m,
                           fL_I, fL_L,
                           GroupToCoilSection, polarities_inGroup, nT, nStrands_inGroup, l_mag_inGroup, ds_inGroup,
                           f_SC_strand_inGroup, f_ro_eff_inGroup, Lp_f_inGroup, RRR_Cu_inGroup,
                           SCtype_inGroup, STtype_inGroup, insulationType_inGroup, internalVoidsType_inGroup,
                           externalVoidsType_inGroup,
                           wBare_inGroup, hBare_inGroup, wIns_inGroup, hIns_inGroup, Lp_s_inGroup, R_c_inGroup,
                           Tc0_NbTi_ht_inGroup, Bc2_NbTi_ht_inGroup, c1_Ic_NbTi_inGroup, c2_Ic_NbTi_inGroup,
                           Tc0_Nb3Sn_inGroup, Bc2_Nb3Sn_inGroup, Jc_Nb3Sn0_inGroup,
                           el_order_half_turns,
                           alphasDEG, rotation_block, mirror_block, mirrorY_block,
                           iContactAlongWidth_From, iContactAlongWidth_To, iContactAlongHeight_From,
                           iContactAlongHeight_To,
                           iStartQuench, tStartQuench, lengthHotSpot_iStartQuench, vQ_iStartQuench,
                           R_circuit, R_crowbar, Ud_crowbar, t_PC, t_PC_LUT, I_PC_LUT,
                           tEE, R_EE_triggered,
                           tCLIQ, directionCurrentCLIQ, nCLIQ, U0, C, Rcapa,
                           tQH, U0_QH, C_QH, R_warm_QH, w_QH, h_QH, s_ins_QH, type_ins_QH, s_ins_QH_He, type_ins_QH_He, l_QH, f_QH,
                           iQH_toHalfTurn_From, iQH_toHalfTurn_To,
                           tQuench, initialQuenchTemp,
                           HalfTurnToInductanceBlock, M_InductanceBlock_m
                           ):
        '''
            **Adds all LEDET parameters to be written in the "Inputs" sheet **

            Function to add "Inputs" LEDET parameters

            :param T00: String defining the name of the file defining the default LEDET parameters
            :type T00: float

            :return: None
        '''

        # Add all Inputs variables to a list
        variableGroupInputs = []
        variableGroupInputs.append(('T00', T00))
        variableGroupInputs.append(('l_magnet', l_magnet))
        variableGroupInputs.append(('I00', I00))
        variableGroupInputs.append('')
        variableGroupInputs.append(('M_m', M_m))
        variableGroupInputs.append('')
        variableGroupInputs.append(('fL_I', fL_I))
        variableGroupInputs.append(('fL_L', fL_L))
        variableGroupInputs.append('')
        variableGroupInputs.append(('GroupToCoilSection', GroupToCoilSection))
        variableGroupInputs.append(('polarities_inGroup', polarities_inGroup))
        variableGroupInputs.append(('nT', nT))
        variableGroupInputs.append(('nStrands_inGroup', nStrands_inGroup))
        variableGroupInputs.append(('l_mag_inGroup', l_mag_inGroup))
        variableGroupInputs.append(('ds_inGroup', ds_inGroup))
        variableGroupInputs.append(('f_SC_strand_inGroup', f_SC_strand_inGroup))
        variableGroupInputs.append(('f_ro_eff_inGroup', f_ro_eff_inGroup))
        variableGroupInputs.append(('Lp_f_inGroup', Lp_f_inGroup))
        variableGroupInputs.append(('RRR_Cu_inGroup', RRR_Cu_inGroup))
        variableGroupInputs.append(('SCtype_inGroup', SCtype_inGroup))
        variableGroupInputs.append(('STtype_inGroup', STtype_inGroup))
        variableGroupInputs.append(('insulationType_inGroup', insulationType_inGroup))
        variableGroupInputs.append(('internalVoidsType_inGroup', internalVoidsType_inGroup))
        variableGroupInputs.append(('externalVoidsType_inGroup', externalVoidsType_inGroup))
        variableGroupInputs.append(('wBare_inGroup', wBare_inGroup))
        variableGroupInputs.append(('hBare_inGroup', hBare_inGroup))
        variableGroupInputs.append(('wIns_inGroup', wIns_inGroup))
        variableGroupInputs.append(('hIns_inGroup', hIns_inGroup))
        variableGroupInputs.append(('Lp_s_inGroup', Lp_s_inGroup))
        variableGroupInputs.append(('R_c_inGroup', R_c_inGroup))
        variableGroupInputs.append(('Tc0_NbTi_ht_inGroup', Tc0_NbTi_ht_inGroup))
        variableGroupInputs.append(('Bc2_NbTi_ht_inGroup', Bc2_NbTi_ht_inGroup))
        variableGroupInputs.append(('c1_Ic_NbTi_inGroup', c1_Ic_NbTi_inGroup))
        variableGroupInputs.append(('c2_Ic_NbTi_inGroup', c2_Ic_NbTi_inGroup))
        variableGroupInputs.append(('Tc0_Nb3Sn_inGroup', Tc0_Nb3Sn_inGroup))
        variableGroupInputs.append(('Bc2_Nb3Sn_inGroup', Bc2_Nb3Sn_inGroup))
        variableGroupInputs.append(('Jc_Nb3Sn0_inGroup', Jc_Nb3Sn0_inGroup))
        variableGroupInputs.append('')
        variableGroupInputs.append(('el_order_half_turns', el_order_half_turns))
        variableGroupInputs.append('')
        variableGroupInputs.append(('alphasDEG', alphasDEG))
        variableGroupInputs.append(('rotation_block', rotation_block))
        variableGroupInputs.append(('mirror_block', mirror_block))
        variableGroupInputs.append(('mirrorY_block', mirrorY_block))
        variableGroupInputs.append('')
        variableGroupInputs.append(('iContactAlongWidth_From', iContactAlongWidth_From))
        variableGroupInputs.append(('iContactAlongWidth_To', iContactAlongWidth_To))
        variableGroupInputs.append(('iContactAlongHeight_From', iContactAlongHeight_From))
        variableGroupInputs.append(('iContactAlongHeight_To', iContactAlongHeight_To))
        variableGroupInputs.append('')
        variableGroupInputs.append(('iStartQuench', iStartQuench))
        variableGroupInputs.append(('tStartQuench', tStartQuench))
        variableGroupInputs.append(('lengthHotSpot_iStartQuench', lengthHotSpot_iStartQuench))
        variableGroupInputs.append(('vQ_iStartQuench', vQ_iStartQuench))
        variableGroupInputs.append('')
        variableGroupInputs.append(('R_circuit', R_circuit))
        variableGroupInputs.append(('R_crowbar', R_crowbar))
        variableGroupInputs.append(('Ud_crowbar', Ud_crowbar))
        variableGroupInputs.append('')
        variableGroupInputs.append(('t_PC', t_PC))
        variableGroupInputs.append(('t_PC_LUT', t_PC_LUT))
        variableGroupInputs.append(('I_PC_LUT', I_PC_LUT))
        variableGroupInputs.append('')
        variableGroupInputs.append(('tEE', tEE))
        variableGroupInputs.append(('R_EE_triggered', R_EE_triggered))
        variableGroupInputs.append('')
        variableGroupInputs.append(('tCLIQ', tCLIQ))
        variableGroupInputs.append(('directionCurrentCLIQ', directionCurrentCLIQ))
        variableGroupInputs.append(('nCLIQ', nCLIQ))
        variableGroupInputs.append(('U0', U0))
        variableGroupInputs.append(('C', C))
        variableGroupInputs.append(('Rcapa', Rcapa))
        variableGroupInputs.append('')
        variableGroupInputs.append(('tQH', tQH))
        variableGroupInputs.append(('U0_QH', U0_QH))
        variableGroupInputs.append(('C_QH', C_QH))
        variableGroupInputs.append(('R_warm_QH', R_warm_QH))
        variableGroupInputs.append(('w_QH', w_QH))
        variableGroupInputs.append(('h_QH', h_QH))
        variableGroupInputs.append(('s_ins_QH', s_ins_QH))
        variableGroupInputs.append(('type_ins_QH', type_ins_QH))
        variableGroupInputs.append(('s_ins_QH_He', s_ins_QH_He))
        variableGroupInputs.append(('type_ins_QH_He', type_ins_QH_He))
        variableGroupInputs.append(('l_QH', l_QH))
        variableGroupInputs.append(('f_QH', f_QH))
        variableGroupInputs.append(('iQH_toHalfTurn_From', iQH_toHalfTurn_From))
        variableGroupInputs.append(('iQH_toHalfTurn_To', iQH_toHalfTurn_To))
        variableGroupInputs.append('')
        variableGroupInputs.append(('tQuench', tQuench))
        variableGroupInputs.append(('initialQuenchTemp', initialQuenchTemp))
        variableGroupInputs.append('')
        variableGroupInputs.append(('HalfTurnToInductanceBlock', HalfTurnToInductanceBlock))
        variableGroupInputs.append(('M_InductanceBlock_m', M_InductanceBlock_m))

        self.setVariableGroupInputs(variableGroupInputs)

        return


    def addVariablesOptions(self,
                            time_vector_params,
                            Iref, flagIron, flagSelfField, headerLines, columnsXY, columnsBxBy, flagPlotMTF,
                            flag_calculateInductanceMatrix, flag_useExternalInitialization, flag_initializeVar,
                            flag_fastMode, flag_controlCurrent, flag_automaticRefinedTimeStepping, flag_IronSaturation,
                            flag_InvertCurrentsAndFields, flag_ScaleDownSuperposedMagneticField, flag_HeCooling,
                            fScaling_Pex, fScaling_Pex_AlongHeight,
                            fScaling_MR, flag_scaleCoilResistance_StrandTwistPitch, flag_separateInsulationHeatCapacity,
                            flag_ISCL, fScaling_Mif, fScaling_Mis, flag_StopIFCCsAfterQuench, flag_StopISCCsAfterQuench,
                            tau_increaseRif, tau_increaseRis,
                            fScaling_RhoSS, maxVoltagePC, flag_symmetricGroundingEE, flag_removeUc, BtX_background,
                            BtY_background,
                            flag_showFigures, flag_saveFigures, flag_saveMatFile, flag_saveTxtFiles,
                            flag_generateReport,
                            flag_hotSpotTemperatureInEachGroup, MinMaxXY_MTF
                           ):
        '''
            **Adds all LEDET parameters to be written in the "Options" sheet **

            Function to add "Options" LEDET parameters

            :param T00: String defining the name of the file defining the default LEDET parameters
            :type T00: float

            :return: None
        '''

        # Add all Options variables to a list
        variableGroupOptions = []
        variableGroupOptions.append(('time_vector_params', time_vector_params))
        variableGroupOptions.append(('Iref', Iref))
        variableGroupOptions.append(('flagIron', flagIron))
        variableGroupOptions.append(('flagSelfField', flagSelfField))
        variableGroupOptions.append(('headerLines', headerLines))
        variableGroupOptions.append(('columnsXY', columnsXY))
        variableGroupOptions.append(('columnsBxBy', columnsBxBy))
        variableGroupOptions.append(('flagPlotMTF', flagPlotMTF))
        variableGroupOptions.append(('flag_calculateInductanceMatrix', flag_calculateInductanceMatrix))
        variableGroupOptions.append(('flag_useExternalInitialization', flag_useExternalInitialization))
        variableGroupOptions.append(('flag_initializeVar', flag_initializeVar))
        variableGroupOptions.append(('flag_fastMode', flag_fastMode))
        variableGroupOptions.append(('flag_controlCurrent', flag_controlCurrent))
        variableGroupOptions.append(('flag_automaticRefinedTimeStepping', flag_automaticRefinedTimeStepping))
        variableGroupOptions.append(('flag_IronSaturation', flag_IronSaturation))
        variableGroupOptions.append(('flag_InvertCurrentsAndFields', flag_InvertCurrentsAndFields))
        variableGroupOptions.append(('flag_ScaleDownSuperposedMagneticField', flag_ScaleDownSuperposedMagneticField))
        variableGroupOptions.append(('flag_HeCooling', flag_HeCooling))
        variableGroupOptions.append(('fScaling_Pex', fScaling_Pex))
        variableGroupOptions.append(('fScaling_Pex_AlongHeight', fScaling_Pex_AlongHeight))
        variableGroupOptions.append(('fScaling_MR', fScaling_MR))
        variableGroupOptions.append(('flag_scaleCoilResistance_StrandTwistPitch', flag_scaleCoilResistance_StrandTwistPitch))
        variableGroupOptions.append(('flag_separateInsulationHeatCapacity', flag_separateInsulationHeatCapacity))
        variableGroupOptions.append(('flag_ISCL', flag_ISCL))
        variableGroupOptions.append(('fScaling_Mif', fScaling_Mif))
        variableGroupOptions.append(('fScaling_Mis', fScaling_Mis))
        variableGroupOptions.append(('flag_StopIFCCsAfterQuench', flag_StopIFCCsAfterQuench))
        variableGroupOptions.append(('flag_StopISCCsAfterQuench', flag_StopISCCsAfterQuench))
        variableGroupOptions.append(('tau_increaseRif', tau_increaseRif))
        variableGroupOptions.append(('tau_increaseRis', tau_increaseRis))
        variableGroupOptions.append(('fScaling_RhoSS', fScaling_RhoSS))
        variableGroupOptions.append(('maxVoltagePC', maxVoltagePC))
        variableGroupOptions.append(('flag_symmetricGroundingEE', flag_symmetricGroundingEE))
        variableGroupOptions.append(('flag_removeUc', flag_removeUc))
        variableGroupOptions.append(('BtX_background', BtX_background))
        variableGroupOptions.append(('BtY_background', BtY_background))
        variableGroupOptions.append(('flag_showFigures', flag_showFigures))
        variableGroupOptions.append(('flag_saveFigures', flag_saveFigures))
        variableGroupOptions.append(('flag_saveMatFile', flag_saveMatFile))
        variableGroupOptions.append(('flag_saveTxtFiles', flag_saveTxtFiles))
        variableGroupOptions.append(('flag_generateReport', flag_generateReport))
        variableGroupOptions.append(('flag_hotSpotTemperatureInEachGroup', flag_hotSpotTemperatureInEachGroup))
        variableGroupOptions.append(('MinMaxXY_MTF', MinMaxXY_MTF))

        self.setVariableGroupOptions(variableGroupOptions)

        return


    def addVariablesPlots(self,
                          suffixPlot, typePlot, outputPlotSubfolderPlot, variableToPlotPlot, selectedStrandsPlot,
                          selectedTimesPlot,
                          labelColorBarPlot, minColorBarPlot, maxColorBarPlot, MinMaxXYPlot, flagSavePlot,
                          flagColorPlot, flagInvisiblePlot
                           ):
        '''
            **Adds all LEDET parameters to be written in the "Plots" sheet **

            Function to add "Plots" LEDET parameters

            :param T00: String defining the name of the file defining the default LEDET parameters
            :type T00: float

            :return: None
        '''

        # Add all Plots variables to a list
        variableGroupPlots = []
        variableGroupPlots.append(('suffixPlot', suffixPlot))
        variableGroupPlots.append(('typePlot', typePlot))
        variableGroupPlots.append(('outputPlotSubfolderPlot', outputPlotSubfolderPlot))
        variableGroupPlots.append(('variableToPlotPlot', variableToPlotPlot))
        variableGroupPlots.append(('selectedStrandsPlot', selectedStrandsPlot))
        variableGroupPlots.append(('selectedTimesPlot', selectedTimesPlot))
        variableGroupPlots.append(('labelColorBarPlot', labelColorBarPlot))
        variableGroupPlots.append(('minColorBarPlot', minColorBarPlot))
        variableGroupPlots.append(('maxColorBarPlot', maxColorBarPlot))
        variableGroupPlots.append(('MinMaxXYPlot', MinMaxXYPlot))
        variableGroupPlots.append(('flagSavePlot', flagSavePlot))
        variableGroupPlots.append(('flagColorPlot', flagColorPlot))
        variableGroupPlots.append(('flagInvisiblePlot', flagInvisiblePlot))

        self.setVariableGroupPlots(variableGroupPlots)

        return


    def addVariablesVariables(self,
                              variableToSaveTxt, typeVariableToSaveTxt, variableToInitialize
                              ):
        '''
            **Adds all LEDET parameters to be written in the "Variables" sheet **

            Function to add "Variables" LEDET parameters

            :param T00: String defining the name of the file defining the default LEDET parameters
            :type T00: float

            :return: None
        '''

        # Add all Variables variables to a list
        variableGroupVariables = []
        variableGroupVariables.append(('variableToSaveTxt', variableToSaveTxt))
        variableGroupVariables.append(('typeVariableToSaveTxt', typeVariableToSaveTxt))
        variableGroupVariables.append(('variableToInitialize', variableToInitialize))

        self.setVariableGroupVariables(variableGroupVariables)

        return


    def printVariableDescNameValue(self, variableGroup, variableLabels):
        """

           **Print variable description, variable name, and variable value**

           Function prints variable description, variable name, and variable value

           :param variableGroup: list of tuples; each tuple has two elements: the first element is a string defining
           the variable name, and the second element is either an integer, a float, a list, or a numpy.ndarray
           defining the variable value :type variableGroup: list :param variableLabels: dictionary assigning a
           description to each variable name
           :type variableLabels: dict

           :return: None

           - Example :

           import numpy as np

            variableGroup = []
            variableGroup.append( ('x1', 12) )
            variableGroup.append( ('x2', 23.42) )
            variableGroup.append( ('x3', [2, 4, 6]) )
            variableGroup.append( ('x3', np.array([2, 4, 6])) )

            variableLabels = {'x1': '1st variable', 'x2': '2nd variable', 'x3': '3rd variable'}

            utils.printVariableDescNameValue(variableGroup, variableLabels)
            # >>> 					1st variable x1 12
            # >>> 					2nd variable x2 23.42
            # >>> 					3rd variable x3 [2, 4, 6]
            # >>> 					3rd variable x3 [2 4 6]

        """

        for vg in variableGroup:
            if vg != '':
                varName = vg[0]
                varValue = vg[1]
                varDesc = variableLabels.get(str(varName))
                print(varDesc + " " + varName + " " + str(varValue))

    def writeFileLEDET(self, nameFileLEDET, verbose: bool = False):
        '''
            **Writes LEDET input file **

            Function to write a LEDET input file composed of "Inputs", "Options", "Plots", and "Variables" sheets

            :param nameFileLEDET: String defining the name of the LEDET input file to be written
            :type nameFileLEDET: string
            :param verbose: flag that determines whether the output are printed
            :type verbose: bool

            :return: None
        '''

        workbook = xlsxwriter.Workbook(nameFileLEDET)

        if verbose:
            print('### Write "Inputs" sheet ###')
        writeLEDETInputsNew(workbook, "Inputs", self.variableGroupInputs, self.variablesInputs, verbose)

        if verbose:
            print('')
            print('### Write "Options" sheet ###')
        writeLEDETInputsNew(workbook, "Options", self.variableGroupOptions, self.variablesOptions, verbose)

        if verbose:
            print('')
            print('### Write "Plots" sheet ###')
        writeLEDETInputsNew(workbook, "Plots", self.variableGroupPlots, self.variablesPlots, verbose)

        if verbose:
            print('')
            print('### Write "Variables" sheet ###')
        writeLEDETInputsNew(workbook, "Variables", self.variableGroupVariables, self.variablesVariables, verbose)

        # Save the workbook
        workbook.close()

        # Display time stamp and end run
        currentDT = datetime.datetime.now()
        print(' ')
        print('Time stamp: ' + str(currentDT))
        print('New file ' + nameFileLEDET + ' generated.')

        return


###### START OF FUNCTION DEFINITIONS
def getValueType(value):
    """

        **Define the type of input variable**

        Function returns an an integer defining the type of input variable:
        - float: 0
        - int: 0
        - list: 1
        - numpy.ndarray: 2

        :param value: a variable
        :type value: float, int, list, or numpy.ndarray
        :return: int

        - Example :

        import numpy as np

        print( utils.getValueType(2) ) # expected: 0
        # >>> 					0

        print( utils.getValueType(2.31) ) # expected: 0
        # >>> 					0

        print( utils.getValueType([2, 3, 5]) ) # expected: 1
        # >>> 					1

        print( utils.getValueType(np.array([2, 3, 5])) ) # expected: 2
        # >>> 					2

    """

    if isinstance(value, (float, int)):
        return 0
    if isinstance(value, list):
        return 1
    if isinstance(value, np.ndarray):
        return 2
    raise Exception('Input parameter type {} not supported!'.format(type(value)))


def writeLEDETInputsNew(book, sheet, variableGroup, variableLabels, verbose: bool = False):
    """

        **Write one sheet of a LEDET input file**

        Function writes one sheet of a LEDET input file

        :param book: workbook object to write
        :type book: xlsxwriter.Workbook
        :param sheet: name of the sheet to write (first sheet = 0)
        :type sheet: string
        :param variableGroup: list of tuples; each tuple has two elements: the first element is a string defining the variable name, and the second element is either an integer, a float, a list, or a numpy.ndarray defining the variable value
        :type variableGroup: list
        :param variableLabels: dictionary assigning a description to each variable name
        :type variableLabels: dict
        :param verbose: flag that determines whether the output are printed
        :type verbose: bool
        :return:

    """

    worksheet = book.add_worksheet(sheet)

    cell_format = book.add_format({'bold': False, 'font_name': 'Calibri', 'font_size': 11})

    # Write to the sheet of the workbook
    currentRow = 0
    for i in range(len(variableGroup)):
        vg = variableGroup[i]
        if vg != '':
            varName = vg[0]
            varValue = vg[1]
            varDesc = variableLabels.get(str(varName))

            worksheet.write(currentRow, 0, varDesc, cell_format)
            worksheet.write(currentRow, 1, varName, cell_format)

            if verbose:
                print('i=' + str(i) + ', currentRow=' + str(currentRow) + ' - ' + str(varName))

            # get variable type
            # 0 - scalar, 1 - vector, 2 - matrix
            varType = getValueType(varValue)
            if varType == 0:
                worksheet.write(currentRow, 2, varValue, cell_format)
                currentRow = currentRow + 1
            if varType == 1:
                worksheet.write_row(currentRow, 2, varValue, cell_format)
                currentRow = currentRow + 1
            if varType == 2:
                for row, data in enumerate(varValue):
                    worksheet.write_row(currentRow, 2, data, cell_format)
                    currentRow = currentRow + 1
        if vg == '':
            if verbose:
                print('i=' + str(i) + ', currentRow=' + str(currentRow) + ' - ' + 'BLANK LINE')
            currentRow = currentRow + 1

    worksheet.set_column(0, 0, 80)
    worksheet.set_column(1, 1, 40)
    worksheet.set_column(2, 1000, 20)