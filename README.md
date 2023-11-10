The developed algorithm is specific to the problem posed for assignment 1 of Research Track I course. The corresponding flow chart is:
![FlowChart](https://github.com/DndrGunnr/RT_Assignment_1/assets/80176557/2f0058c2-722f-466d-8609-7bc1bb28c30b)

The algorithm allows to robot to collect all the markers near a chosen one using 5 main functions:
  -count_tokens: used at initialization to count all the markers inside the workspace, the result will be later used for the termination condition.
  -find_token: used to identify and keep track of markers, it returns distance and angle for new or tracked markers.
  -find_center: used to choose the center marker and find it when a marker must be moved towards it.
  -move_to_marker: used to compute the trajectory and move the robot towards any marker.
  -main: code inside main function stripped to bare minimum.
  Possible improvements may involve the trajectory computation to minimize the angle adjustments and overshoot of target markers or the implementation of a function to avoid collision with blocks.
