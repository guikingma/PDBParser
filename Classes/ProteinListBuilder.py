import os
import Protein

class ProteinListBuilder:
    classFolder = None
    proteinClass = None
    
    def buildList(self, classFolder, proteinClass):
        """ Return a list with all Proteins objects of the classFolder files """

        self.proteinClass = proteinClass
        self.classFolder = classFolder
        proteinFiles = self.listProteinFiles()
        
        proteinList = []
        
        for proteinFileName in proteinFiles:
            proteinList.append(self.createProtein(proteinFileName))

        return proteinList

    def listProteinFiles(self):
        """ List the protein clean files """
        proteinFiles = []
        for file in os.listdir(self.classFolder):
            if file.endswith('.txt'):
                proteinFiles.append(file)
        return proteinFiles

    def createProtein(self, proteinFileName):
        """ Create a protein object with the given file """
        
        proteinFile = open(self.classFolder + proteinFileName, 'r')
        primaryStructure = self.buildPrimaryStructure(proteinFile)
        proteinFile.close()
        
        proteinFile = open(self.classFolder + proteinFileName, 'r')
        secondaryStructure = self.buildSecondaryStructure(proteinFile, len(primaryStructure), proteinFileName)#tirar ultimo par
        proteinFile.close()

        return Protein.Protein(os.path.basename(proteinFileName).replace('.txt', ''), self.proteinClass,primaryStructure, secondaryStructure)

    def buildPrimaryStructure(self, proteinFile):
        """ Build the primary structure """
        primaryStructure = []
            
        for line in proteinFile:
            if line.startswith('SEQRES'):
                cleanLine = self.removeExtraWhiteSpace(line)
                words = cleanLine.split(' ')
                for aminoacids in range(4, len(words)):
                    primaryStructure.append(words[aminoacids])

        return primaryStructure
    
    def removeExtraWhiteSpace(self, line):
        """ Remove extra whitespace, leaving only single whitespaces """
        return ' '.join(line.split())

    def buildSecondaryStructure(self, proteinFile, size, x):
        """ Build the secondary structure """
        secondaryStructure = []

        for itens in range(size):
            secondaryStructure.append('N')

        for line in proteinFile:
            cleanLine = self.removeExtraWhiteSpace(line)
            if cleanLine.startswith('HELIX'):
                words = cleanLine.split(' ')
                try:
                    start = int(words[5]) - 1
                    end = int(words[8])
                except ValueError:
                    print str(x) + ' ' + words[5]
                
                for itens in range(start , end):
                    if itens < len(secondaryStructure): #proteins that have wrong helix information
                        secondaryStructure[itens] = 'H'
            elif cleanLine.startswith('SHEET'):
                words = cleanLine.split(' ')
                try:
                  start = int(words[6]) - 1
                  end = int(words[9])
                except ValueError:
                  print str(x)
                for itens in range(start, end):
                    if itens < len(secondaryStructure): #proteins that have wrong sheet information
                        secondaryStructure[itens] = 'S'

        return secondaryStructure
