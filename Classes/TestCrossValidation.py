import CrossValidation
import unittest
import Protein
import pdb

class TestCrossValidation(unittest.TestCase):
    """ Tests the CrossValidation class. """
    class1 = None
    class2 = None
    
    def test_getNumberTests(self):
        """ Tests the getNumberTests method """
        crossValidation = CrossValidation.CrossValidation()
        actual_test1 = crossValidation.getNumberTests(73)
        actual_test2 = crossValidation.getNumberTests(117)
        actual_test3 = crossValidation.getNumberTests(131)
        actual_test4 = crossValidation.getNumberTests(51)
        actual_test5 = crossValidation.getNumberTests(47)
        actual_test6 = crossValidation.getNumberTests(17)
        
        expected_test1 = 7, 10
        expected_test2 = 12, 9
        expected_test3 = 13, 14
        expected_test4 = 5, 6
        expected_test5 = 5, 2
        expected_test6 = 1, 8
        
        self.assertEqual(actual_test1, expected_test1)
        self.assertEqual(actual_test2, expected_test2)
        self.assertEqual(actual_test3, expected_test3)
        self.assertEqual(actual_test4, expected_test4)
        self.assertEqual(actual_test5, expected_test5)
        self.assertEqual(actual_test6, expected_test6)

        
    
    def test_addClass(self):
        """ test adding a class """
        crossValidation = CrossValidation.CrossValidation()
        
        self.class1 = self.createClass('1', 148)
        self.class2 = self.createClass('2', 17)
        
        crossValidation.addClass(self.class1)
        crossValidation.addClass(self.class2)

        self.assertCrossValidation(crossValidation)

    def createClass(self, classNumber, classSize):
        """ Create a protein list for testing """
        proteinList = []

        for index in range(0, classSize):
            name = 'pc' + classNumber + '-' + str(index)
            proteinList.append(Protein.Protein(name, '',[], []))

        return proteinList

    def assertCrossValidation(self, crossValidation):
        """ Assert the tests, trainings and their sizes """
        self.assertSizes(crossValidation)
        self.assertTestsTrainings(crossValidation, self.class1, 15, 13)
        self.assertTestsTrainings(crossValidation, self.class2, 1, 8)

        
    def assertSizes(self, crossValidation):
        """ Assert the size of witch test and training """
        # test1 to test9: 16(15+1)
        # test10: 21(13+8)
        for test in range(1, 10):
            self.assertEqual(len(crossValidation.getTest(test)), 16)
        self.assertEqual(len(crossValidation.getTest(10)), 21)

        #training1 to training9: 149(133+16)
        #training10: 144(135+9)
        for test in range(1, 10):
            self.assertEqual(len(crossValidation.getTraining(test)), 149)
        self.assertEqual(len(crossValidation.getTraining(10)), 144)

    def assertTestsTrainings(self, crossValidation, protein_class, test_size, last_test_size):
        """ Asserts if the tests was built correctly """
        
        str_class = self.getStrArray(protein_class)
        test_start = 0
        
        for set_index in range(1, 10):
            actual_test = self.getStrArray(crossValidation.getTest(set_index))
            actual_training = self.getStrArray(crossValidation.getTraining(set_index))

            for item in range(0, len(protein_class)):
                if item in range(test_start, test_start + test_size):
                    self.assertTrue(str_class[item] in actual_test)
                else:
                    self.assertTrue(str_class[item] in actual_training)

            test_start += test_size


        actual_test = self.getStrArray(crossValidation.getTest(10))
        actual_training = self.getStrArray(crossValidation.getTraining(10))

        for item in range(0, len(protein_class)):
            if item in range(test_start, test_start + last_test_size):
                self.assertTrue(str_class[item] in actual_test)
            else:
                self.assertTrue(str_class[item] in actual_training)


    def getStrArray(self, protein_array):
        """ Returns a List with the proteins names """
        str_array = []
        for protein in protein_array:
            str_array.append(protein.getName())
        return str_array




if __name__ == '__main__':
    unittest.main(exit=False)
