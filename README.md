# TD3

### Step 1 : Initialisation

* We initialise the experience replay memory. We will populate it with each new Transition.
* Since we have 2 critics learning the Q values, and we learn Q values using the historical data which we get from Experience replay memory
* When we train an off policy model, we always use an experience replay memory that stores past transitions which we use to learn our Q values
* Experience memory contains different transitions composed of < Current State, The action played, Next State , Reward >

### Step 2 :

* We build one neural network for **Actor Model** and one neural network for **Actor Target**
* Actor Model is our AI that takes in input the state and outputs the actions to play
* Actor Target will be initialised same as Actor Model, overtime the weights of this will updated so as to return optimal actions

### Step 3 :

* We build two neural networks for two Critic Models and two Neural network for Two critic Target

## Training :

We run full episodes with the first 10,000 actions played randomly, and then with actions played by the Actor Model. This is because to learn Q values we are required to fill up the Replay Memory. The first 10,000 actions are random for exploration.

### Step 4 : 

Sampling the batch of transitions(current state,next state, action , reward) from the memory. After this we create 4 seperate batches, one batch for current state, one for next state, one for action and one batch for reward

## Now for each element of the batch do following:

### Step 5 :

From next state s' , the actor target plays action a' i.e we give input to actor target model next state s' and it outputs a' i.e next action

### Step 6 :
We add Gaussian noise to this next action a`(technique of exploration which either will get us into some better state or avoid the agent being stuck in a state) and we clamp it in a range of values supported by the environment.This is just to avoid too large actions getting played which can disturb the state of the environment.

### Step 7 :

The two Critic Targets each take (s`, a`) as input and return two Q-values as output.

### Step 8 :

We keep the minimum of these two Q-values

It represents the approximated values of the next state. Taking minimum prevents the too optimistic estimate of value of state which was one of the drawback in classic actor critic method. Taking minimum allows to add some stability to the training process.

### Step 9 :

We get the final target of the two Critic Models, which is = reward + gamma * min(q values predicted by two critic targets). Now we have the targets, we will compare it to the predictions of the critic model.

### Staep 10 :

The two Critic Models each take the couple (s, a) as input and return two Q-values.

### Step 11: Loss computation

We compute the loss coming from two critic models as follows :

Critic_loss = MSE(Qcritic1,QT) + MSE(Qcritic2,QT)
This loss does the sum of all the mean squared error loss between the predicted Q values of all the states and actions in the transition of a batch i.e we are computing the loss over the whole batch

### Step 12 :

Now as we have the loss we want to update the parameters of the critic model so as to reduce the loss over iterations and we do this by back propogating the loss into two Critic models and update the weights using ADAM optimizer.

##### Till this point we have done the Q learning part of the





