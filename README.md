# GDMC-master
 
 To do:
 1. Implement a better way to iterate over neighbouring blocks for the A* road building
     - Currently it uses all floor blocks, to find one with a step distance of 1, this is wasteful as only neighbours are relevant.
 2. Find a way to iterate over all available floor space after road generation to find spots for buildings of certain sizes.
     - 5x5 houses
     - 3x5 tents
     - 7x12 farms
     - Any size parks (plants and flowers)
