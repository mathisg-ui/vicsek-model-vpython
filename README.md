# vicsek-model-vpython
Here a simple code to modelize vicsek model. The first code "viscek model" compute the positions and the orientation of each agents and store it in a file. To optimize the time of computation for searching the close neighboor I use the NearestNeighbors function from the sklearn which permit to go to large number of agents without exploding the computation time. To visualize the movement of the agents, you can use the code "simu_vicsek" which takes the data from the file created with the 1st code and then diplays it using the library vpython.


