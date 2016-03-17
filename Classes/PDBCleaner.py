import os

class PDBCleaner:
    """ Clean PDB files. """
    inputFolder = None
    outputFolder = None
    
    def cleanFiles(self, inputFolder, outputFolder):
        """ 
            Clean all pdb files in inputFolder and write in outputFolder
            
            >>> x = PDBCleaner()
            >>> x.cleanFiles('/Users/pedroribeiro/Desktop/Parser/Proteinas/Ligases/', '/Users/pedroribeiro/Desktop/Parser/CleanFiles/Ligases/')
        """
        
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        
        proteinFiles = os.listdir(self.inputFolder)
        for protein in proteinFiles:
            self.extractPrimarySecondaryStructures(protein)
        

    def extractPrimarySecondaryStructures(self, protein):
        """ Read a file """
        proteinFile = open(self.inputFolder + protein, 'r')
        cleanProteinFile = open(self.outputFolder + protein.replace('.pdb', '.txt'), 'w')

        for line in proteinFile:
            if line.startswith('SEQRES') or line.startswith('HELIX') or line.startswith('SHEET'):
                cleanProteinFile.write(line)

        proteinFile.close()
        cleanProteinFile.close()
        
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()