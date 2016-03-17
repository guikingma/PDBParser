import math
import pdb

class CrossValidation:
    """ k-fold CrossValidation. k default value is 10 """
    k = 10.0
    
    test1 = []
    test2 = []
    test3 = []
    test4 = []
    test5 = []
    test6 = []
    test7 = []
    test8 = []
    test9 = []
    test10 = []

    training1 = []
    training2 = []
    training3 = []
    training4 = []
    training5 = []
    training6 = []
    training7 = []
    training8 = []
    training9 = []
    training10 = []
    
    def getNumberTests(self, classSize):
        """ Returns a tuple with the number of tests in the sets 1 to 9 and the last set """
        
        num_tests_ceil = int(math.ceil(classSize / self.k))
        last_test_ceil = classSize - (num_tests_ceil * 9)

        num_tests_floor = int(math.floor(classSize / self.k))
        last_test_floor = classSize - (num_tests_floor * 9)
        
        sub_ceil = abs(num_tests_ceil - last_test_ceil)
        sub_floor = abs(num_tests_floor - last_test_floor)
    
        if num_tests_ceil * 9 > classSize:
            if num_tests_floor * 9 > classSize:
                return None
            else:
                return num_tests_floor, last_test_floor
        elif num_tests_floor * 9 > classSize:
                return num_tests_ceil, last_test_ceil
        elif sub_floor < sub_ceil:
            return num_tests_floor, last_test_floor
        else:
            return num_tests_ceil, last_test_ceil


    def addClass(self, classList):
        """ Do the cross validation to the given class """
        
        test_numbers_tuple = self.getNumberTests(len(classList))
        number_of_tests = test_numbers_tuple[0]
        number_of_last_tests = test_numbers_tuple[1]
        
        test_start = 0

        self.addTestTraining(self.test1, self.training1, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test2, self.training2, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test3, self.training3, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test4, self.training4, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test5, self.training5, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test6, self.training6, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test7, self.training7, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test8, self.training8, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test9, self.training9, test_start, number_of_tests, classList)
        test_start += number_of_tests
        
        self.addTestTraining(self.test10, self.training10, test_start, number_of_last_tests, classList)
    
    def addTestTraining(self, test, training, test_start, number_of_tests, classList):
        """ Add the samples to its respective test and training sets """
        
        for item in range(0, len(classList)):
            if item in range(test_start, test_start + number_of_tests):
                test.append(classList[item])
            else:
                training.append(classList[item])


    def getTest(self, test_number):
        """ Returns the test set corresponding to the given number """

        if test_number == 1:
            return self.test1
        elif test_number == 2:
            return self.test2
        elif test_number == 3:
            return self.test3
        elif test_number == 4:
            return self.test4
        elif test_number == 5:
            return self.test5
        elif test_number == 6:
            return self.test6
        elif test_number == 7:
            return self.test7
        elif test_number == 8:
            return self.test8
        elif test_number == 9:
            return self.test9
        elif test_number == 10:
            return self.test10

    def getTraining(self, training_number):
        """ Returns the training set corresponding to the given number """

        if training_number == 1:
            return self.training1
        elif training_number == 2:
            return self.training2
        elif training_number == 3:
            return self.training3
        elif training_number == 4:
            return self.training4
        elif training_number == 5:
            return self.training5
        elif training_number == 6:
            return self.training6
        elif training_number == 7:
            return self.training7
        elif training_number == 8:
            return self.training8
        elif training_number == 9:
            return self.training9
        elif training_number == 10:
            return self.training10

