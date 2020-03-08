import os

from steam_nb_api.resources.ResourceReader import ResourceReader
from steam_nb_api.utils.misc import makeCopyFile


class ParametersCOSIM:
    '''
        Class of COSIM parameters to generate automatically the COSIM folder and file structure
    '''

    def __init__(self, nameFolderCosimModel: str, nameCircuit: str = ''):
        '''

        :param nameFolderCosimModel: String defining the name of the folder where the COSIM model will be saved
        :type nameFolderCosimModel: str
        :param nameCircuit: string defining the circuit name; at the moment, this is just a label
        :type nameCircuit: str

        '''

        self.nameFolderCosimModel = nameFolderCosimModel
        self.circuitName = nameCircuit

        # Load and set the default config files (using ResourceReader allows reading from a "hidden" resource folder)
        self.nameTemplateConfigFileCosim = ResourceReader.getResourcePath(os.path.join('sing', 'STEAMConfig.json'))
        self.nameTemplateConfigFilePSpice = ResourceReader.getResourcePath(os.path.join('sing', 'PSpiceConfig.json'))
        self.nameTemplateConfigFileLedet = ResourceReader.getResourcePath(os.path.join('sing', 'LedetConfig.json'))

    def makeAllFolders(self):
        '''
            **Makes a COSIM folder with the required PSPICE and LEDET subfolders**

            Function to generate all the required subfolders and files for a COSIM model

            :return: None
        '''

        nameFolderCosimModel = self.nameFolderCosimModel

        # Make COSIM folder
        if not os.path.exists(nameFolderCosimModel):
            os.makedirs(nameFolderCosimModel)

        # Make SPICE model folder
        pathFolderPSpice = os.path.join(nameFolderCosimModel, 'PSpice')
        if not os.path.exists(pathFolderPSpice):
            os.makedirs(pathFolderPSpice)

        # Make LEDET model folder and sub-folders
        nameFolderLedetModel = os.path.join(nameFolderCosimModel, 'LEDET')
        if not os.path.isdir(nameFolderLedetModel):
            os.mkdir(nameFolderLedetModel)
        if not os.path.isdir(os.path.join(nameFolderLedetModel, 'LEDET')):
            os.mkdir(os.path.join(nameFolderLedetModel, 'LEDET'))
        # if not os.path.isdir(os.path.join(nameFolderLedetModel, 'Input', 'Control current input')):
        #     os.mkdir(os.path.join(nameFolderLedetModel, 'Input', 'Control current input'))
        # if not os.path.isdir(os.path.join(nameFolderLedetModel, 'Input', 'Initialize variables')):
        #     os.mkdir(os.path.join(nameFolderLedetModel, 'Input', 'Initialize variables'))
        # if not os.path.isdir(os.path.join(nameFolderLedetModel, 'Input', 'InitializationFiles')):
        #     os.mkdir(os.path.join(nameFolderLedetModel, 'Input', 'InitializationFiles'))

    def copyConfigFiles(self):
        '''
            **Makes the configuration files required to run a COSIM model with one PSPICE and one LEDET models **

            Function to generate the configuration files for COSIM, one PSPICE, and one LEDET models

            :return: None
        '''

        nameFolderCosimModel = self.nameFolderCosimModel
        nameTemplateConfigFileCosim = self.nameTemplateConfigFileCosim
        nameTemplateConfigFilePSpice = self.nameTemplateConfigFilePSpice
        nameTemplateConfigFileLedet = self.nameTemplateConfigFileLedet

        # Check that the folder exists; if not, generate all required folders and subfolders
        if not os.path.exists(nameFolderCosimModel):
            self.makeAllFolders()

        # Copy template COSIM config file
        makeCopyFile(nameTemplateConfigFileCosim, os.path.join(nameFolderCosimModel, 'STEAMConfig.json'))

        # Copy template PSpice config file
        makeCopyFile(nameTemplateConfigFilePSpice, os.path.join(nameFolderCosimModel, 'PSpice', 'PSpiceConfig.json'))

        # Copy template LEDET config file
        makeCopyFile(nameTemplateConfigFileLedet, os.path.join(nameFolderCosimModel, 'LEDET', 'LedetConfig.json'))

    def copyIOPortFiles(self, fileName_IOPortDefinition: str, fileName_complementaryIOPortDefinition: str):
        '''
            **Copies the input/output port files required to run a COSIM model with one PSPICE and one LEDET models **

            Function to copy the I/O Port files in the correct subfolders

            :return: None
        '''

        nameFolderCosimModel = self.nameFolderCosimModel

        # Check that the required input files exist
        if not os.path.isfile(fileName_IOPortDefinition):
            raise Exception('Input file fileName_IOPortDefinition = {} not found!'.format(fileName_IOPortDefinition))
        if not os.path.isfile(fileName_complementaryIOPortDefinition):
            raise Exception(
                'Input file fileName_IOPortDefinition = {} not found!'.format(fileName_complementaryIOPortDefinition))

        # Check that the folder exists; if not, generate all required folders and subfolders
        if not os.path.exists(nameFolderCosimModel):
            self.makeAllFolders()

        # Copy PSPICE IOPort file
        makeCopyFile(fileName_IOPortDefinition,
                     os.path.join(nameFolderCosimModel, 'PSpice', 'PspiceInputOutputPortDefinition.json'))

        # Copy LEDET IOPort file
        makeCopyFile(fileName_complementaryIOPortDefinition,
                     os.path.join(nameFolderCosimModel, 'LEDET', 'LedetInputOutputPortDefinition.json'))
