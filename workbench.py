import numpy as np

class Cube:
    def __init__(self):
        self._face = ['u', 'd', 'f', 'b', 'l', 'r']
        self._color = {face: np.array([idx] * 9).reshape(3, 3) for idx, face in enumerate(self._face)}



    def __repr__(self):
        string = ''
        string += '\s' * 3









if __name__ == '__main__':
    cube = Cube()
    print(cube)