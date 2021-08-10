class Cell():

    def __init__(self, prime=False, col=None):
        self._prime = prime
        self._col = col

    @property
    def prime(self):
        return self._prime
    
    @property
    def col(self):
        return self._col
   
    @col.setter
    def col(self, val):
        self._col = val 
