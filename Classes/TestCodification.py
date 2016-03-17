import Codification
import Protein
import unittest

class TestCodification(unittest.TestCase):
    """ Tests the Codification class methods """
    
    def test_buildSVMProteinVector(self):
        """ Tests the buildProteinVector function """
        
        name = 'TestProtein'
        primaryStructure = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLU', 'GLN', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL', 'ALA', 'ARG']
        secondaryStructure = ['N', 'N', 'N', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
        protein = Protein.Protein(name, 'hydrolase',primaryStructure, secondaryStructure)

        codification = Codification.Codification()
        actual_str_nohash1 = codification.buildSVMProteinVector(protein, 0, 'PS', 44)
        actual_str_nohash2 = codification.buildSVMProteinVector(protein, 0, 'SP', 44)
        actual_str_nohash3 = codification.buildSVMProteinVector(protein, 0, 'PS', 88)
    
        actual_str_hash1 = codification.buildSVMProteinVector(protein, 2, 'PS', 44)
        actual_str_hash2 = codification.buildSVMProteinVector(protein, 3, 'PS', 44)


        self.assertEqual(actual_str_nohash1, '3 1:1.0 2:2.0 3:3.0 4:4.0 5:5.0 6:6.0 7:7.0 8:8.0 9:9.0 10:10.0 11:11.0 12:12.0 13:13.0 14:14.0 15:15.0 16:16.0 17:17.0 18:18.0 19:19.0 20:20.0 21:1.0 22:2.0 23:21.0 24:21.0 25:21.0 26:21.0 27:21.0 28:21.0 29:22.0 30:22.0 31:22.0 32:22.0 33:22.0 34:22.0 35:22.0 36:23.0 37:23.0 38:23.0 39:23.0 40:23.0 41:23.0 42:23.0 43:23.0 44:23.0')
    
        self.assertEqual(actual_str_nohash2, '3 1:21.0 2:21.0 3:21.0 4:21.0 5:21.0 6:21.0 7:22.0 8:22.0 9:22.0 10:22.0 11:22.0 12:22.0 13:22.0 14:23.0 15:23.0 16:23.0 17:23.0 18:23.0 19:23.0 20:23.0 21:23.0 22:23.0 23:1.0 24:2.0 25:3.0 26:4.0 27:5.0 28:6.0 29:7.0 30:8.0 31:9.0 32:10.0 33:11.0 34:12.0 35:13.0 36:14.0 37:15.0 38:16.0 39:17.0 40:18.0 41:19.0 42:20.0 43:1.0 44:2.0')
    
        self.assertEqual(actual_str_nohash3, '3 1:1.0 2:2.0 3:3.0 4:4.0 5:5.0 6:6.0 7:7.0 8:8.0 9:9.0 10:10.0 11:11.0 12:12.0 13:13.0 14:14.0 15:15.0 16:16.0 17:17.0 18:18.0 19:19.0 20:20.0 21:1.0 22:2.0 23:21.0 24:21.0 25:21.0 26:21.0 27:21.0 28:21.0 29:22.0 30:22.0 31:22.0 32:22.0 33:22.0 34:22.0 35:22.0 36:23.0 37:23.0 38:23.0 39:23.0 40:23.0 41:23.0 42:23.0 43:23.0 44:23.0 88:0.0')

        self.assertEqual(actual_str_hash1, '3 1:1.0 2:2.0 3:3.0 4:4.0 5:5.0 6:6.0 7:7.0 8:8.0 9:9.0 10:10.0 11:1.0 12:11.0 13:11.0 14:11.0 15:12.0 16:12.0 17:12.0 18:13.0 19:14.0 20:14.0 21:14.0 22:14.0')
        self.assertEqual(actual_str_hash2, '3 1:1.0 2:2.0 3:3.0 4:4.0 5:5.0 6:6.0 7:7.0 8:8.0 9:9.0 10:10.0 11:11.0 12:12.0 13:13.0 14:13.0 15:14.0')







if __name__ == '__main__':
    unittest.main(exit=False)
