import random
import unittest
import numpy as np
import sys

class RandomGen(object):
     # Values that may be returned by next_num()
     _random_nums = [-1, 0, 1, 2, 3]
     # Probability of the occurence of random_nums
     _probabilities = [0.01, 0.3, 0.58, 0.1, 0.01] 
     # Corresponding cumulative distribution function
     _distribution = np.cumsum(_probabilities)
     def next_num(self):
         """
         Returns one of the randomNums. When this method is called
         multiple times over a long period, it should return the
         numbers roughly with the initialized probabilities.
         """
         
         # Get a uniform random number in [0, 1]
         x = random.random()

         # Loop through the distribution step function and
         # break (return) as soon as the number x is less
         # than the value of the distribution function
         for i, d in enumerate(self._distribution):
             if ( x <= d ):
                 return self._random_nums[i]


class TestRandomGenMethods(unittest.TestCase):
    gen = RandomGen()
    def test_probabilities_non_negative(self):
        self.assertTrue(np.all(np.array(self.gen._probabilities) >= 0 ))
    def test_probabilities_sum_to_one(self):
        self.assertTrue(np.abs(np.sum(self.gen._probabilities) - 1) <= np.spacing(1) )
    def test_lengths_of_arrays(self):
        self.assertTrue(len(self.gen._probabilities) == len(self.gen._random_nums))
    def test_values_of_random_numbers(self):
        """
        Test that the random numbers returned are contained in the 
        list of numbers prescribed
        """
        N = 1000
        for i in range(N):
            num = self.gen.next_num()
            self.assertTrue(num in self.gen._random_nums)


if __name__ == '__main__':
    # Number of times next_num is called can
    # be passed from the command line
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = 100

    # Run the unit tests:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRandomGenMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # A sample run:
    # dictionary to store the count of each random number
    count = {k: 0 for k in RandomGen._random_nums}
    # Create the random number generator object
    gen = RandomGen()
    # Loop to get numbers
    for i in range(N):
        num = gen.next_num()
        count[num] = count[num] + 1

    print('==========================')
    print('Total count = ' + str(N) )
    print('==========================')
    for k in RandomGen._random_nums:
        print(str(k) + ': ' + str(count[k]) + ' times')

    print('==========================')
    print('* probability estimates  *')
    print('==========================')
    for k in RandomGen._random_nums:
        print('P(x = ' + str(k) + ') = ' + str(count[k]/N))

