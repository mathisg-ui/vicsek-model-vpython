# vicsek-model-vpython
Here a simple code to modelize vicsek model. The first code "viscek model" computes the positions and the orientations of each agents and stores it in a file. To optimize the time of computation for searching the close neighbors I use the NearestNeighbors function from the sklearn library which permits to go to large numbers of agents without exploding the computation time. To visualize the movement of the agents, you can use the code "simu_vicsek" which takes the data from the file created with the 1st code and then diplays it using the library vpython.


