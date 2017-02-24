class Room():
    def __init__(self, the_name, N, S, E, W, the_description):
        self.name = the_name
        self.description = the_description
        self.north = N
        self.south = S
        self.east = E
        self.west = W
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]
spawn = Room('Shipping Crate', 'alpha', 'beta','charlie', 'delta' \
'There are empty oil barrels in here.')
alpha = Room('alpha', None, 'spawn', None, None, 'controller testing room alpha')
beta = Room('Beta', 'spawn', None, None, None, 'controller testing room beta')
charlie = Room('charlie', None, None, None, 'spawn', 'controller testing room charlie' )
delta = Room('delta', None, None, 'spawn', None, 'controller testing room delta')



node = spawn
