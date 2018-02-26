## importar la clase de test
import unittest

## declaracion del test
class TestTablero(unittest.TestCase):

	## definir primer test
    def test_tablero(self):
        tablero = [
            [0,1,2,3,4,5,6,7],
            [0,1,2,3,4,5,6,7],
            [0,1,2,3,4,5,6,7],
            [0,1,2,3,4,5,6,7],
   		    [0,1,2,3,4,5,6,7],
            [0,1,2,3,4,5,6,7],
            [0,1,2,3,4,5,6,7],
            [0,1,2,3,4,5,6,7],
        ] ## code
        # self.assertEqual(tablero)

    def test_tablero(self):
        tablero = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] ## code
        self.assertEqual(tablero)

if __name__ == "__main__":
    unittest.main()