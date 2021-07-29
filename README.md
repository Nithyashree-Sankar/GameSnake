# SnakeGame
In this repository, I built an automated snake game solver using pytorch and Deep Q network. Implemented a feed forward neural network to predict the snake's next move and trained using the snake's current direction and the food co-ordinate.
![image](https://user-images.githubusercontent.com/85114391/127514040-3c426353-a818-4765-8f69-8b0322a26677.png)
Q-Learning is an off-policy algorithm that learns about the greedy policy  while using a different behaviour policy for acting in the environment/collecting data. This behaviour policy is usually an -greedy policy that selects the greedy action with probability and a random action with probability  to ensure good coverage of the state-action space.
For most problems, it is impractical to represent the -function as a table containing values for each combination of  and . Instead, we train a function approximator, such as a neural network and that is known as Deep Q Network.


