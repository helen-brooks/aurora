from settings import *

def setupInput():
    
    createMaterials(False)
    createSettings(False)
    createTallies("copper_air_tetmesh.h5m")

setupInput()
openmc.run()
