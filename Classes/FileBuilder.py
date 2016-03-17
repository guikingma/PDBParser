import Codification
import pdb

class FileBuilder:
	""" Class for writing the tests and training files. """
	
	crossValidation = None
	folder = None
	greaterSequence = None
	vectorForm = None
	codification = None
	maskSize = None
	normalization = None
    
	hash = {}
	HASH_INDEX = 1.0

	final_test1 = []
	final_test2 = []
	final_test3 = []
	final_test4 = []
	final_test5 = []
	final_test6 = []
	final_test7 = []
	final_test8 = []
	final_test9 = []
	final_test10 = []
    
	final_training1 = []
	final_training2 = []
	final_training3 = []
	final_training4 = []
	final_training5 = []
	final_training6 = []
	final_training7 = []
	final_training8 = []
	final_training9 = []
	final_training10 = []
    
	def __init__(self, crossValidation, folder, vectorForm, greaterSequence, maskSize, normalization):
		self.crossValidation = crossValidation
		self.folder = folder
		self.vectorForm = vectorForm
		self.greaterSequence = greaterSequence
		self.codification = Codification.Codification()
		self.maskSize = maskSize
		self.normalization = normalization
		self.start()
        
	def start(self):
		"""Write a file for each test and training"""
    	
		self.buildTestsTrainings()
		if(self.normalization):
			self.normalizeVectors()
		self.writeFiles()

##############################################BUILD VECTORS########################################################

	def buildTestsTrainings(self):
		""" Build the tests and training vectors with the proteins final vectors """
    	
		self.buildVector(1, 'test', self.crossValidation.getTest(1))
		self.buildVector(2, 'test', self.crossValidation.getTest(2))
		self.buildVector(3, 'test', self.crossValidation.getTest(3))
		self.buildVector(4, 'test', self.crossValidation.getTest(4))
		self.buildVector(5, 'test', self.crossValidation.getTest(5))
		self.buildVector(6, 'test', self.crossValidation.getTest(6))
		self.buildVector(7, 'test', self.crossValidation.getTest(7))
		self.buildVector(8, 'test', self.crossValidation.getTest(8))
		self.buildVector(9, 'test', self.crossValidation.getTest(9))
		self.buildVector(10, 'test', self.crossValidation.getTest(10))
    	
		self.buildVector(1, 'training', self.crossValidation.getTraining(1))
		self.buildVector(2, 'training', self.crossValidation.getTraining(2))
		self.buildVector(3, 'training', self.crossValidation.getTraining(3))
		self.buildVector(4, 'training', self.crossValidation.getTraining(4))
		self.buildVector(5, 'training', self.crossValidation.getTraining(5))
		self.buildVector(6, 'training', self.crossValidation.getTraining(6))
		self.buildVector(7, 'training', self.crossValidation.getTraining(7))
		self.buildVector(8, 'training', self.crossValidation.getTraining(8))
		self.buildVector(9, 'training', self.crossValidation.getTraining(9))
		self.buildVector(10, 'training', self.crossValidation.getTraining(10))
    	
	def buildVector(self, vecNum, vecType, vec):
		""" Build the final vector """
		final_vec = []
    	
		for protein in vec:
			final_vec.append(self.buildFinalProtein(protein))
    		
		if vecType == 'test':
			self.addTestVector(vecNum, final_vec)
		elif vecType == 'training':
			self.addTrainingVector(vecNum, final_vec)
    		
	def addTestVector(self, vecNum, final_vec):
		if vecNum == 1:
			self.final_test1 = final_vec
		elif vecNum == 2:
			self.final_test2 = final_vec
		elif vecNum == 3:
			self.final_test3 = final_vec
		elif vecNum == 4:
			self.final_test4 = final_vec
		elif vecNum == 5:
			self.final_test5 = final_vec
		elif vecNum == 6:
			self.final_test6 = final_vec
		elif vecNum == 7:
			self.final_test7 = final_vec
		elif vecNum == 8:
			self.final_test8 = final_vec
		elif vecNum == 9:
			self.final_test9 = final_vec
		elif vecNum == 10:
			self.final_test10 = final_vec
    	
	def addTrainingVector(self, vecNum, final_vec):
		if vecNum == 1:
			self.final_training1 = final_vec
		elif vecNum == 2:
			self.final_training2 = final_vec
		elif vecNum == 3:
			self.final_training3 = final_vec
		elif vecNum == 4:
			self.final_training4 = final_vec
		elif vecNum == 5:
			self.final_training5 = final_vec
		elif vecNum == 6:
			self.final_training6 = final_vec
		elif vecNum == 7:
			self.final_training7 = final_vec
		elif vecNum == 8:
			self.final_training8 = final_vec
		elif vecNum == 9:
			self.final_training9 = final_vec
		elif vecNum == 10:
			self.final_training10 = final_vec
    	
	def buildFinalProtein(self, protein):
		""" Returns the final protein vector """
    	
		final_vector = []
    	
		for char in self.vectorForm:
			if char == 'P':
				self.addPrimary(final_vector, protein)
			elif char == 'S':
				self.addSecondary(final_vector, protein)
            #elif char == 'I':
                #TODO: addPrimarySecondary(vector, protein)
            #elif char == 'F':
                #TODO: addFeatures(vector, protein)
                
		final_vector = self.reduceVector(final_vector)
		final_vector.insert(0, protein.getECNumber())
		return final_vector
        
	def addPrimary(self, vector, protein):
		""" Add the primary structure to the vector with the codification """
		primary_structure = protein.getPrimaryStructure()
		for residues in primary_structure:
			vector.append(self.codification.getValue(residues))

		for zeros in range(0, self.greaterSequence - len(primary_structure)):
			vector.append(0)
            
	def addSecondary(self, vector, protein):
		""" Add the secondary structure to the vector with the codification """
    
		secondary_structure = protein.getSecondaryStructure()
		for struc in secondary_structure:
			vector.append(self.codification.getValue(struc))

		for zeros in range(0, self.greaterSequence - len(secondary_structure)):
			vector.append(0)
                
	def reduceVector(self, vector):
		""" Reduce the vector using the given mask """
		#pdb.set_trace()
		if(self.maskSize > 1):
			new_vector = []
			divisible_pos = len(vector) - (len(vector) % self.maskSize)

			for itens in range(0, divisible_pos, self.maskSize):
				key = ''
				for i in range(itens, itens + self.maskSize):
					key += str(vector[i]) + ' '
				if key in self.hash:
					new_item = self.hash[key]
				else:
					self.hash[key] = self.HASH_INDEX
					new_item = self.HASH_INDEX
					self.HASH_INDEX += 1.0
				new_vector.append(new_item)

			#if divisible_pos < len(vector):
			#	new_vector.append(self.HASH_INDEX)

			if divisible_pos < len(vector):
				key = ''
				for i in range(divisible_pos, len(vector)):
					key += str(vector[i]) + ' '
					
				if key in self.hash:
					new_item = self.hash[key]
				else:
					self.hash[key] = self.HASH_INDEX
					new_item = self.HASH_INDEX
					self.HASH_INDEX += 1.0

			return new_vector
		else:
			return vector
    	
##############################################NORMALIZE VECTORS####################################################  
    		
	def normalizeVectors(self):
		""" Normalize all values to be between 0 and 1 """
    	
		min_max_values = self.getMinMaxValue()
    	
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test1)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test2)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test3)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test4)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test5)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test6)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test7)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test8)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test9)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_test10)
    	
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training1)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training2)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training3)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training4)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training5)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training6)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training7)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training8)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training9)
		self.changeValues(min_max_values[0], min_max_values[1], self.final_training10)
    	
	def getMinMaxValue(self):
		""" Return a tuple with the min and max values """
    	
		min = 999999
		max = -999999
    	
		for vector in self.final_test1:
			for item in vector:
				min = item if item < min else min
				max = item if item > max else max
    			
		for vector in self.final_training1:
			for item in vector:
				min = item if item < min else min
				max = item if item > max else max
    			
		return min, max
    	
	def changeValues(self, min_value, max_value, vector):
		""" Normalize values with the formula: A' = (A - MIN)/(MAX - MIN) """
    	
		for protein in vector:
			for i in range(1, len(protein)):# starts in 1 because of the class number(ecnumber)
				protein[i] = (protein[i] - min_value) / (max_value - min_value)
    			
    
##############################################WRITE FILES###########################################################

  	def writeFiles(self):
		""" Write the vectors in the files """
		
		self.write('testet1', self.final_test1)
		self.write('testet2', self.final_test2)
		self.write('testet3', self.final_test3)
		self.write('testet4', self.final_test4)
		self.write('testet5', self.final_test5)
		self.write('testet6', self.final_test6)
		self.write('testet7', self.final_test8)
		self.write('testet8', self.final_test8)
		self.write('testet9', self.final_test9)
		self.write('testet10', self.final_test10)
		
		self.write('treinot1', self.final_training1)
		self.write('treinot2', self.final_training2)
		self.write('treinot3', self.final_training3)
		self.write('treinot4', self.final_training4)
		self.write('treinot5', self.final_training5)
		self.write('treinot6', self.final_training6)
		self.write('treinot7', self.final_training7)
		self.write('treinot8', self.final_training8)
		self.write('treinot9', self.final_training9)
		self.write('treinot10', self.final_training10)
		
	def write(self, file_name, vector):
		""" Write a file with the vector proteins """
		#pdb.set_trace()
		file = open(self.folder + file_name, 'w')
		
		for protein in range(0,  len(vector) - 1):
			line = self.getProteinString(vector[protein]) + '\n'
			file.write(line)
			
		line = self.getProteinString(vector[len(vector) - 1])
		file.write(line)
		
		file.close()

	def getProteinString(self, protein):
		""" Returns a string with the given protein in the SVM format """
		
		protein_str = str(protein[0]) + ' '
		for i in range(1, len(protein) - 1):
			if protein[i] != 0.0:
				protein_str += '{0}:{1} '.format(str(i), str(protein[i]))
				
		#if protein[len(protein) - 1] != 0.0:
			protein_str += '{0}:{1}'.format(str(len(protein) - 1), protein[len(protein) - 1])
			
		return protein_str
		
    
""" 
    def start(self):
        """ """Write a file for each test and training""" """
        #pdb.set_trace()
        for test_training in range(1, 11):
            self.writeFile('testet' + str(test_training), self.crossValidation.getTest(test_training))
            self.writeFile('treinot' + str(test_training), self.crossValidation.getTraining(test_training))

    def writeFile(self, fileName, proteinList):
        """ """Write the proteinList in the fileName""" """

        file = open(self.folder + fileName + '.txt', 'w')

        for item in proteinList:
           line = self.codification.buildSVMProteinVector(item, 7, self.vectorForm, self.greaterSequence) + '\n'
           file.write(line)
 """          