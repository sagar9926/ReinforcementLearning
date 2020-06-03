8.  The action predicted by the model is a single value ranging from -5 to +5 where 5 is max action value and negative action values corresponds to steer left and positive action values would be for steering right.

9. Replay buffer will have one storage variable to store past transitions, maximum size to limit the number of stored transitions in memory and a pointer to update the stored transitions in replay buffer memory.Each transition will have state , next state, action,reward and done parameters.
 State variable will be :
•	An image of size 28x28 of the location of car on map to keep the car on road

•	An orientation variable which is a measure of angle between the velocity vector of car and the displacement vector of destination w.r.t the centre of the car to balance the motion of the car and make the car learn to move toward destination

•	Remaining distance to reach the destination
Action Variable : Control the steering for the car
Done : True if the episode is completed

10.  step(action) will return :
•	new state which consists of following:

o	Updated 28x28 patch of map

o	Updated angle between the velocity vector of car and the destination displacement angle w.r.t center of car

o	Updated distance between the car position and destination

•	Reward : Reward for taking a particular action i.e taking left or right

•	Done : True if episode completed




