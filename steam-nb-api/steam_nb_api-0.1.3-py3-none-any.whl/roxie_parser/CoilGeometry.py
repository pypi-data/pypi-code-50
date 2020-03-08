from steam_nb_api.roxie_parser import ConductorSigma
from steam_nb_api.roxie_parser.BlockParameters import BlockParameters
from steam_nb_api.roxie_parser.GroupParameters import GroupParameters
from steam_nb_api.roxie_parser.TransformationParameters import TransformationParameters


class MagneticCoil:
    '''
        Class of magnetic coil
    '''

    def __init__(self, xS = [], yS = [], iS = []):
        self.xS = xS
        self.yS = yS
        self.iS = iS
        self.xPos = None
        self.yPos = None
        self.iPos = None
        self.xBarePos = None
        self.yBarePos = None
        self.blockParametersList = None
        self.groupParametersList = None
        self.transofrmationParametersList = None
        self.cadatabase = None

    def setBlockParametersList(self, blockParametersList):
        self.blockParametersList = blockParametersList

    def setGroupParametersList(self, groupParametersList):
        self.groupParametersList = groupParametersList

    def setTransformationParametersList(self, transformationParametersList):
        self.transformationParametersList = transformationParametersList

    def setConductorPositions(self, xPos, yPos, iPos, xBarePos, yBarePos):
        self.xPos, self.yPos, self.iPos = xPos, yPos, iPos
        self.xBarePos, self.yBarePos = xBarePos, yBarePos

    def setStrandPositions(self, xS, yS, iS):
        self.xS, self.yS, self.iS = xS, yS, iS

    def setCableDatabase(self, cadatabase):
        self.cadatabase = cadatabase

    def acquireBlockParameters(self, fileName: str, verbose: bool = False) -> list:
        '''
            **Returns list of blockParametersList objects, and sets attribute blockParametersList**

            Function to find block parameters from a ROXIE .data file

            :param fileName: String defining the name of the input ROXIE .data file
            :type fileName: str
            :param verbose: flag that determines whether the output are printed
            :type verbose: bool

            :return: list
        '''

        # Define keywords
        blockStartKeyword = "BLOCK "

        # Read file
        file = open(fileName, "r")
        fileContent = file.read()

        # Separate rows
        fileContentByRow = fileContent.split("\n")

        # Print file content, row by row
        if verbose:
            for row in fileContentByRow:
                print(row)

        # Find block definition
        for i in range(len(fileContentByRow)):
            if blockStartKeyword in fileContentByRow[i]:
                startOfBlockIndex = i

        firstRowBlock = fileContentByRow[startOfBlockIndex]
        nRowsBlockParameters = int(firstRowBlock[5:])
        print('Block definition parameters have {} rows'.format(nRowsBlockParameters))

        # Separate part of the data with block definition information
        blockParameters = fileContentByRow[startOfBlockIndex + 1:startOfBlockIndex + 1 + nRowsBlockParameters]

        # Assign parameters to a list of BlockParameters objects
        blockParametersList = []
        for row in blockParameters:
            rowSplitStr = row.split()

            noBlock = int(rowSplitStr[0])
            typeBlock = int(rowSplitStr[1])
            nco = int(rowSplitStr[2])
            radius = float(rowSplitStr[3])
            phi = float(rowSplitStr[4])
            alpha = float(rowSplitStr[5])
            current = float(rowSplitStr[6])
            condname = rowSplitStr[7]
            n1 = int(rowSplitStr[8])
            n2 = int(rowSplitStr[9])
            imag = int(rowSplitStr[10])
            turn = float(rowSplitStr[11])

            blockParametersList.append(
                BlockParameters(noBlock, typeBlock, nco, radius, phi, alpha, current, condname, n1, n2,
                                              imag, turn))

        # Print each BlockParameters object in the list
        if verbose:
            for i in range(0, len(blockParametersList)):
                print(blockParametersList[i].toString())
        # Note: two additional attributes appear at the end: shift2, roll2, xPos, yPos, xBarePos, yBarePos,
        # which are initiated to [0.0, 0.0], [0.0, 0.0, 0.0], [], [], [], [] respectively

        # Set these parameters in the magneticCoil object
        self.setBlockParametersList(blockParametersList)

        return blockParametersList

    def acquireGroupParameters(self, fileName: str, verbose: bool = False) -> list:
        '''
            **Returns list of groupParametersList objects, and sets attribute groupParametersList**

            Function to find group parameters from a ROXIE .data file

            :param fileName: String defining the name of the input ROXIE .data file
            :type fileName: str
            :param verbose: flag that determines whether the output are printed
            :type verbose: bool

            :return: list
        '''

        # Define keywords
        groupStartKeyword = "LAYER "

        # Read file
        file = open(fileName, "r")
        fileContent = file.read()

        # Separate rows
        fileContentByRow = fileContent.split("\n")

        # Find group definition
        for i in range(len(fileContentByRow)):
            if groupStartKeyword in fileContentByRow[i]:
                startOfGroupIndex = i

        firstRowGroup = fileContentByRow[startOfGroupIndex]
        nRowsGroupParameters = int(firstRowGroup[5:])
        if nRowsGroupParameters == 1:
            print('Group definition parameters have {} row'.format(nRowsGroupParameters))
        else:
            print('Group definition parameters have {} rows'.format(nRowsGroupParameters))

        # Separate part of the data with group definition information
        groupParameters = fileContentByRow[startOfGroupIndex + 1:startOfGroupIndex + 1 + nRowsGroupParameters]

        # Assign parameters to a list of GroupParameters objects
        groupParametersList = []
        for row in groupParameters:
            rowSplitStr = row.split()

            noGroup = int(rowSplitStr[0])
            symm = int(rowSplitStr[1])
            typexy = int(rowSplitStr[2])
            blocks = list(map(int, rowSplitStr[3:-1]))

            groupParametersList.append(
                GroupParameters(noGroup, symm, typexy, blocks))

        # Print each GroupParameters object in the list
        if verbose:
            for i in range(0, len(groupParametersList)):
                print(groupParametersList[i].toString())

        # Set these parameters in the magneticCoil object
        self.setGroupParametersList(groupParametersList)

        return groupParametersList

    def acquireTransformationParameters(self, fileName: str, verbose: bool = False) -> list:
        '''
            **Returns list of transformationParametersList objects, and sets attribute transformationParametersList**

            Function to find transformation parameters from a ROXIE .data file

            :param fileName: String defining the name of the input ROXIE .data file
            :type fileName: str
            :param verbose: flag that determines whether the output are printed
            :type verbose: bool

            :return: list
        '''

        # Define keywords
        transformationStartKeyword = "EULER "

        # Read file
        file = open(fileName, "r")
        fileContent = file.read()

        # Separate rows
        fileContentByRow = fileContent.split("\n")

        # Find transformation definition
        for i in range(len(fileContentByRow)):
            if transformationStartKeyword in fileContentByRow[i]:
                startOfTransformationIndex = i

        firstRowTransformation = fileContentByRow[startOfTransformationIndex]
        nRowsTransformationParameters = int(firstRowTransformation[5:])
        if nRowsTransformationParameters == 1:
            print('Transformation definition parameters have {} row'.format(nRowsTransformationParameters))
        else:
            print('Transformation definition parameters have {} rows'.format(nRowsTransformationParameters))

        # Separate part of the data with transformation definition information
        transformationParameters = fileContentByRow[
                                   startOfTransformationIndex + 1:startOfTransformationIndex + 1 + nRowsTransformationParameters]

        # Assign parameters to a list of TransformationParameters objects
        transformationParametersList = []
        for row in transformationParameters:
            rowSplitStr = row.split()

            noTransformation = int(rowSplitStr[0])
            x = float(rowSplitStr[1])
            y = float(rowSplitStr[2])
            alph = float(rowSplitStr[3])
            bet = float(rowSplitStr[4])
            string = str(rowSplitStr[5])
            act = int(rowSplitStr[6])
            bcs = list(map(int, rowSplitStr[7:-1]))

            transformationParametersList.append(
                TransformationParameters(noTransformation, x, y, alph, bet, string, act, bcs))

        # Print each TransformationParameters object in the list
        if verbose:
            for i in range(0, len(transformationParametersList)):
                print(transformationParametersList[i].toString())

        # Set these parameters in the magneticCoil object
        self.setTransformationParametersList(transformationParametersList)

        return transformationParametersList

    def applySymmetryConditions(self, verbose: bool = False) -> list:
        '''
            **Returns updated list of blockParametersList objects, and sets attribute blockParametersList**

            Apply symmetry conditions to blocks

            :param verbose: flag that determines whether the output are printed
            :type verbose: bool

            :return: list
        '''

        blockParametersList = self.blockParametersList
        groupParametersList = self.groupParametersList

        # Apply symmetry conditions to blocks
        for group in groupParametersList:
            if group.symm == 0:
                print('Group {} has symmetry of type {} --> No symmetry.'.format(group.noGroup, group.symm))

            elif group.symm == 2:
                print('Group {} has symmetry of type {} --> Dipole symmetry.'.format(group.noGroup, group.symm))
                blockParametersList = group.applyMultipoleSymmetry(blockParametersList, N=1)

            elif group.symm == 4:
                print('Group {} has symmetry of type {} --> Quadrupole symmetry.'.format(group.noGroup, group.symm))
                blockParametersList = group.applyMultipoleSymmetry(blockParametersList, N=2)

            elif group.symm == 6:
                print('Group {} has symmetry of type {} --> Sextupole symmetry.'.format(group.noGroup, group.symm))
                blockParametersList = group.applyMultipoleSymmetry(blockParametersList, N=3)

            elif group.symm == 8:
                print('Group {} has symmetry of type {} --> Octupole symmetry.'.format(group.noGroup, group.symm))
                blockParametersList = group.applyMultipoleSymmetry(blockParametersList, N=4)

            elif group.symm == 10:
                print('Group {} has symmetry of type {} --> Decapole symmetry.'.format(group.noGroup, group.symm))
                blockParametersList = group.applyMultipoleSymmetry(blockParametersList, N=5)

            elif group.symm == 12:
                print('Group {} has symmetry of type {} --> Dodecapole symmetry.'.format(group.noGroup, group.symm))
                blockParametersList = group.applyMultipoleSymmetry(blockParametersList, N=6)

            elif group.symm == 31:
                print(
                    'Group {} has symmetry of type {} --> Window frame dipole symmetry. Not currently supported.'.format(
                        group.noGroup, group.symm))

            elif group.symm == 33:
                print(
                    'Group {} has symmetry of type {} --> Window frame quadrupole symmetry. Not currently supported.'.format(
                        group.noGroup, group.symm))

            elif group.symm == 41:
                print('Group {} has symmetry of type {} --> Solenoid symmetry. Not currently supported.'.format(
                    group.noGroup,
                    group.symm))

            elif group.symm == 71:
                print(
                    'Group {} has symmetry of type {} --> Periodic structure (wiggler) symmetry. Not currently supported.'.format(
                        group.noGroup, group.symm))

            else:
                print('Group {} has symmetry of type {} --> Not currently supported.'.format(group.noGroup, group.symm))

        print('Total number of blocks: {}'.format(len(blockParametersList)))

        if verbose:
            # Print each BlockParameters object in the list
            for b, bValue in enumerate(blockParametersList):
                print(bValue.toString())

        return blockParametersList

    def applyTransformations(self, verbose: bool = False) -> list:
        '''
            **Returns updated list of blockParametersList objects, and sets attribute blockParametersList**

            Apply transformationss to blocks

            :param verbose: flag that determines whether the output are printed
            :type verbose: bool

            :return: list
        '''

        blockParametersList = self.blockParametersList
        groupParametersList = self.groupParametersList
        transformationParametersList = self.transformationParametersList

        # Apply transformations to blocks/transformations/conductors
        for transformation in transformationParametersList:
            if transformation.string == 'SHIFT2':
                print(
                    'Transformation {} applies a transformation of type {} --> Cartesian shift of x={} mm and y={} mm.'
                        .format(transformation.noTransformation, transformation.string, transformation.x,
                                transformation.y))
                transformation.applyTranformationShift2(blockParametersList, groupParametersList)

            elif transformation.string == 'ROLL2':
                print(
                    'Transformation {} applies a transformation of type {} --> Counterclockwise rotation of alpha={} deg around point x={} mm and y={} mm.'
                        .format(transformation.noTransformation, transformation.string, transformation.alph,
                                transformation.x,
                                transformation.y))
                transformation.applyTranformationRoll2(blockParametersList, groupParametersList)

            elif transformation.string == 'CONN2':
                print(
                    'Transformation {} applies a transformation of type {} --> Connection of block vertices. Not currently supported.'
                        .format(transformation.noTransformation, transformation.string))

            elif transformation.string == 'CONN2P':
                print(
                    'Transformation {} applies a transformation of type {} --> Connection of block vertices to point XY. Not currently supported.'
                        .format(transformation.noTransformation, transformation.string))

            else:
                print('Transformation {} applies a transformation of type {} --> Not currently supported.'
                      .format(transformation.noTransformation, transformation.string))

        print('Total number of blocks: {}'.format(len(blockParametersList)))

        if verbose:
            # Print each BlockParameters object in the list
            for b, bValue in enumerate(blockParametersList):
                print(bValue.toString())

        return blockParametersList

    def findConductorPositions(self, verbose: bool = False) -> list:
        '''
            **Returns insulated and bare conductor positions, and strand positions**

            Find insulated and bare conductor positions, and strand positions

            :param verbose: flag that determines whether the output are printed
            :type verbose: bool

            :return: list
        '''

        blockParametersList = self.blockParametersList
        cadatabase = self.cadatabase

        # Find conductor positions
        xPos = []
        yPos = []
        iPos = []
        xBarePos = []
        yBarePos = []
        xS = []
        yS = []
        iS = []
        for block in blockParametersList:

            # Get desired conductor data ready for SIGMA
            conductorSigma = ConductorSigma.getConductorSigmaFromCableDatabase(cadatabase, block.condname)

            # Calculate x/y positions of the conductor corners
            if block.typeBlock == 1:
                if verbose:
                    print('Block {} is of type {} --> Cos-theta.'.format(block.noBlock, block.typeBlock))
                x, y, I = block.findCondPos_cosTheta(conductorSigma, flagBare=False)

                xPos = xPos + x
                yPos = yPos + y
                iPos = iPos + I

                xBare, yBare, I = block.findCondPos_cosTheta(conductorSigma, flagBare=True)

                xBarePos = xBarePos + xBare
                yBarePos = yBarePos + yBare

            elif block.typeBlock == 2:
                if verbose:
                    print('Block {} is of type {} --> Block-coil.'.format(block.noBlock, block.typeBlock))
                x, y, I = block.findCondPos_blockCoil(conductorSigma, flagBare=False)

                xPos = xPos + x
                yPos = yPos + y
                iPos = iPos + I

                xBare, yBare, I = block.findCondPos_blockCoil(conductorSigma, flagBare=True)

                xBarePos = xBarePos + xBare
                yBarePos = yBarePos + yBare

            else:
                print('Block {} is of of unknown type: {}. Not supported'.format(block.noBlock, block.typeBlock))

            # Calculate x/y positions of the strands
            xStrand, yStrand, iStrand = block.findStrandPositions(conductorSigma)
            xS = xS + xStrand
            yS = yS + yStrand
            iS = iS + iStrand

        print()

        if verbose:
            print('Total number of conductors (half-turns): {}'.format(len(xPos)))

        self.setConductorPositions(xPos, yPos, iPos, xBarePos, yBarePos)
        self.setStrandPositions(xS, yS, iS)

        return xPos, yPos, iPos, xBarePos, yBarePos, xS, yS, iS
