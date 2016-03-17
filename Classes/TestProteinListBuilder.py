import ProteinListBuilder
import unittest

class TestProteinListBuilder(unittest.TestCase):
    """ Test class for functions in ProteinListBuilder. """
    
    def test_buildList(self):
        """ Test buildList """
        
    	expectedPrimaryList1 = ['GLU', 'ILE', 'SER', 'GLY', 'HIS', 'ILE', 'VAL', 'ARG', 'SER', 'PRO', 'MET', 'VAL', 'GLY', 'THR', 'PHE', 'TYR', 'ARG', 'THR', 'PRO', 'SER', 'PRO', 'ASP', 'ALA', 'LYS', 'ALA', 'PHE', 'ILE', 'GLU', 'VAL', 'GLY', 'GLN', 'LYS', 'VAL', 'ASN', 'VAL', 'GLY', 'ASP', 'THR', 'LEU', 'CYS', 'ILE', 'VAL', 'GLU', 'ALA', 'MET', 'LYS', 'MET', 'MET', 'ASN', 'GLN', 'ILE', 'GLU', 'ALA', 'ASP', 'LYS', 'SER', 'GLY', 'THR', 'VAL', 'LYS', 'ALA', 'ILE', 'LEU', 'VAL', 'GLU', 'SER', 'GLY', 'GLN', 'PRO', 'VAL', 'GLU', 'PHE', 'ASP', 'GLU', 'PRO', 'LEU', 'VAL', 'VAL', 'ILE', 'GLU' ]
    	expectedSecondaryList1 = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
         
        expectedPrimaryList2 = ['GLU', 'ILE', 'SER', 'GLY', 'HIS', 'ILE', 'VAL', 'ARG', 'SER', 'PRO', 'MET', 'VAL', 'GLY', 'THR', 'PHE', 'TYR', 'ARG', 'THR', 'PRO', 'SER', 'PRO', 'ASP', 'ALA', 'LYS', 'ALA', 'PHE', 'ILE', 'GLU', 'VAL', 'GLY', 'GLN', 'LYS', 'VAL', 'ASN', 'VAL', 'GLY', 'ASP', 'THR', 'LEU', 'CYS', 'ILE', 'VAL', 'GLU', 'ALA', 'MET', 'LYS', 'MET', 'MET', 'ASN', 'GLN', 'ILE', 'GLU', 'ALA', 'ASP', 'LYS', 'SER', 'GLY', 'THR', 'VAL', 'LYS', 'ALA', 'ILE', 'LEU', 'VAL', 'GLU', 'SER', 'GLY', 'GLN', 'PRO', 'VAL', 'GLU', 'PHE', 'ASP', 'GLU', 'PRO', 'LEU', 'VAL', 'VAL', 'ILE', 'GLU' ]
        expectedSecondaryList2 = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']   
        
        proteinListBuilder = ProteinListBuilder.ProteinListBuilder()
        LigaseList = proteinListBuilder.buildList('/Users/pedroribeiro/Desktop/Parser/ProteinasTeste/ClasseTeste/', 'class')

        self.assertEqual(len(LigaseList), 2)
        self.assertProtein(LigaseList[0], expectedPrimaryList1, expectedSecondaryList1, 'proteina1')
        self.assertProtein(LigaseList[1], expectedPrimaryList2, expectedSecondaryList2, 'proteina2')
        

    def assertProtein(self, actualProtein, expectedPrimaryList, expectedSecondaryList, expectedName):
        """ 
            Function for asserting a protein object.
            Assert the primary structure, the secondary and the caracteristics.
        """
        
        self.assertEqual(actualProtein.getName(), expectedName)
        
        self.assertPrimaryStructure(actualProtein.getPrimaryStructure(), expectedPrimaryList)
        self.assertSecondaryStructure(actualProtein.getSecondaryStructure(), expectedSecondaryList)

        #TODO
        #self.assertEqual(actualProtein.getHydrophilicNumber(), )
        #self.assertEqual(actualProtein.getHydrophobicNumber(), )
        #self.assertEqual(actualProtein.getNegativeNumber(), )
        #self.assertEqual(actualProtein.getPositiveNumber(), )
        #self.assertEqual(actualProtein.getPolarNumber(), )


    def assertPrimaryStructure(self, actualList, expectedList):
        """ 
            Function for asserting the protein primary structure.
        """

        self.assertEqual(len(actualList), 80)
                
        for index in range(80):
            self.assertEqual(actualList[index], expectedList[index])

    def assertSecondaryStructure(self, actualList, expectedList):
        """
            Function for asserting the protein secondary structure.
        """
        
        self.assertEqual(len(actualList), 80)

        for index in range(80):
            self.assertEqual(actualList[index], expectedList[index])



        
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
