import PDBCleaner
import ProteinListBuilder
import CrossValidation
import FileBuilder

class Parser:
    """ Parser. """
    
    #Constants
    INPUT_FOLDER = '/Users/pedroribeiro/Desktop/Parser/Proteinas/'
    CLEAR_FILES_FOLDER = '/Users/pedroribeiro/Desktop/Parser/CleanFiles/'
    TESTS_TRAININGS_FOLDER = '/Users/pedroribeiro/Desktop/Parser/TestTraining/'

    """ 
            -maskSize is the size of the mask used to reduce the size of the vector
            -vectorForm is a string that contains information for building the vector
                P -> primary structure
                S -> secondary structure
                I -> each residue followed by the corresponding secondary structure
                F -> Features
            Ex: if vectorForm is 'PS', the vector will have the primary structure concatenated with the secondary
    """
    
    VECTOR_FORM = 'PS'
    NORMALIZATION = True
    MASK_SIZE = 7
    
    oxidoreductaseProteinList = []
    transferaseProteinList = []
    hydrolaseProteinList = []
    lyaseProteinList = []
    isomeraseProteinList = []
    ligaseProteinList = []
    
    crossValidation = None
    
    def __init__(self):
        self.cleanPdbFiles()
        self.buildProteins()
        self.buildTestsTrainings()
        self.printTestTraining()
    
    
    def cleanPdbFiles(self):
        """ Clean pdb files for each protein class """
        pdbCleaner = PDBCleaner.PDBCleaner()
        pdbCleaner.cleanFiles(self.INPUT_FOLDER + 'Oxidoreductases/', self.CLEAR_FILES_FOLDER  + 'Oxidoreductases/')
        pdbCleaner.cleanFiles(self.INPUT_FOLDER + 'Transferases/', self.CLEAR_FILES_FOLDER + 'Transferases/')
        pdbCleaner.cleanFiles(self.INPUT_FOLDER + 'Hydrolases/', self.CLEAR_FILES_FOLDER + 'Hydrolases/')
        pdbCleaner.cleanFiles(self.INPUT_FOLDER + 'Lyases/', self.CLEAR_FILES_FOLDER + 'Lyases/')
        pdbCleaner.cleanFiles(self.INPUT_FOLDER + 'Isomerases/', self.CLEAR_FILES_FOLDER + 'Isomerases/')
        pdbCleaner.cleanFiles(self.INPUT_FOLDER + 'Ligases/', self.CLEAR_FILES_FOLDER + 'Ligases/')
        
    def buildProteins(self):
        """ Create protein objects for each class """
        proteinListBuilder = ProteinListBuilder.ProteinListBuilder()
        self.oxidoreductaseProteinList = proteinListBuilder.buildList(self.CLEAR_FILES_FOLDER + 'Oxidoreductases/', 'oxidorreductase')
        self.transferaseProteinList = proteinListBuilder.buildList(self.CLEAR_FILES_FOLDER + 'Transferases/', 'transferase')
        self.hydrolaseProteinList = proteinListBuilder.buildList(self.CLEAR_FILES_FOLDER + 'Hydrolases/', 'hydrolase')
        self.lyaseProteinList = proteinListBuilder.buildList(self.CLEAR_FILES_FOLDER + 'Lyases/', 'lyase')
        self.isomeraseProteinList = proteinListBuilder.buildList(self.CLEAR_FILES_FOLDER + 'Isomerases/', 'isomerase')
        self.ligaseProteinList = proteinListBuilder.buildList(self.CLEAR_FILES_FOLDER + 'Ligases/', 'ligase')

    def buildTestsTrainings(self):
        """ Do the cross validation with the protein classes """
        self.crossValidation = CrossValidation.CrossValidation()
        self.crossValidation.addClass(self.oxidoreductaseProteinList)
        self.crossValidation.addClass(self.transferaseProteinList)
        self.crossValidation.addClass(self.hydrolaseProteinList)
        self.crossValidation.addClass(self.lyaseProteinList)
        self.crossValidation.addClass(self.isomeraseProteinList)
        self.crossValidation.addClass(self.ligaseProteinList)

    def printTestTraining(self):
        """ Print the tests and trainings """
        FileBuilder.FileBuilder(self.crossValidation, self.TESTS_TRAININGS_FOLDER, self.VECTOR_FORM, self.getGreaterSequence(), self.MASK_SIZE, self.NORMALIZATION)

    def getGreaterSequence(self):
        """ Calculates the greater protein sequence """

        seq = -1
        for oxi in self.oxidoreductaseProteinList:
            if len(oxi) > seq:
                seq = len(oxi)

        for trans in self.transferaseProteinList:
            if len(trans) > seq:
                seq = len(trans)
                
        for hyd in self.hydrolaseProteinList:
            if len(hyd) > seq:
                seq = len(hyd)

        for lya in self.lyaseProteinList:
            if len(lya) > seq:
                seq = len(lya)

        for iso in self.isomeraseProteinList:
            if len(iso) > seq:
                seq = len(iso)

        for lig in self.ligaseProteinList:
            if len(lig) > seq:
                seq = len(lig)

        result = 0
        for char in self.VECTOR_FORM:
            if char == 'P' or char == 'S':
                result += seq
            #elif char == 'I':
                #TODO: result += 2 * seq
            #elif char == 'F':
                #TODO: result += Protein.getNumFeatures()
		print "MAIOR SEQ: " + str(result)
        return result

if __name__ == '__main__':
    parser_exec = Parser()