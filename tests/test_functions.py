import random
import unittest

class HangmanTesting(unittest.TestCase):
    '''Tests for hangman functions

    Args:
        unittest ([type]): [description]
    '''
    def test_select_word(self):
        words = [
            'test',
            'voiture', 
            'avion',
            'programmation',
            'covid',
            'contamination'
        ]
        rdm = random.randrange(len(words))
        self.assertIn(words[rdm], words) 
    
    def test_found_letter(self):
        letters = ['a', 'b', 'c', 'd']
        found_letter = 'c'
        self.assertTrue(found_letter in letters)
    
    def test_check_endgame(self):
        letters = ['a', 'b', 'c', 'd']
        words = ['a', 'b', 'c', 'd']
        test = True
        for w in words:
            if w not in letters:
                test = False
        return self.assertTrue(test)
    
if __name__ == "__main__":
    unittest.main()
        