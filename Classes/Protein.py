class Protein:
    """ Parser. """
    name = None
    className = None
    primaryStructure = None
    secondaryStructure = None
    hydrophilicNumber = None
    hydrophobicNumber = None
    negativeNumber = None
    positiveNumber = None
    polarNumber = None
    sequenceSize = None
    
    def __init__(self, name, className, primaryStructure, secondaryStructure):
        self.name = name
        self.className = className
        self.primaryStructure = primaryStructure
        self.secondaryStructure = secondaryStructure
        self.sequenceSize = len(primaryStructure)
        #TODO: fazer outras caracteristicas

    def getName(self):
        return self.name

    def getPrimaryStructure(self):
        return self.primaryStructure

    def getSecondaryStructure(self):
        return self.secondaryStructure

    def getHydrophilicNumber(self):
        return self.hydrophilicNumber

    def getHydrophobicNumber(self):
        return self.hydrophobicNumber

    def getNegativeNumber(self):
        return self.negativeNumber

    def getPositiveNumber(self):
        return self.positiveNumber

    def getPolarNumber(self):
        return self.polarNumber
   
    def getSequenceSize(self):
        return self.sequenceSize
    
    def getClassName(self):
        return self.className
        
    def getECNumber(self):
    	""" Returns the EC number of the class """
        
        if self.className == 'oxidorreductase':
            return 1
        elif self.className == 'transferase':
            return 2
        elif self.className == 'hydrolase':
            return 3
        elif self.className == 'lyase':
            return 4
        elif self.className == 'isomerase':
            return 5
        elif self.className == 'ligase':
            return 6

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.primaryStructure)