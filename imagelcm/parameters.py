"""
Defines key model parameters.
"""

# whether IMAGE-LAND-LUE is running independently of the rest of IMAGE
STANDALONE = True

# epsilon
EPS = 1e-6

# map shape
SHP = (2160, 4320)

# number of food crops
NFC = 16

# number of food crops, including grass
NGFC = 17

# number of biofuel crop classes
NBC = 5

# number of non-grass crop classes (food RF, biofuel and food IR)
NFBFC = 37

# number of crop classes (grass, food RF, biofuel and food IR)
NGFBFC = 38

# number of fodder (grass), food and biofuel crop classes
NGFBC = 22

# same, but without grass
NFBC = 21

# number of grazing systems
NGS = 2
NGST = NGS + 1 # NGS + 'total'

# number of regions (excl. greenland)
N_REG = 26

# whether to print inputs and ouputs throughout the model for debugging
CHECK_IO = False
