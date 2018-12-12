import unittest
from firstlastj import yesno, ret_last_name, func

class myclass(unittest.TestCase):
    def test_lastname1(self):
        self.assertEqual(ret_last_name("Jack"), ("Leiper"))
    def test_lastname2(self):
        self.assertEqual(ret_last_name("Chelsea"), ("Brown"))
    def test_error(self):
        self.assertEqual(ret_last_name("J"), ("Error! No name found."))
    def test_restartno(self):
        self.assertEqual(yesno("n"), ("Thank you for using the program."))

    
    

if __name__ == '__main__' :
    unittest.main()


