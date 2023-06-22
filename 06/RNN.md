# RNN
Mengye Ren mren@cs.toronto.edu
LSTM & GRU
Bag of tricks

## Basic Formula
[$$] a^t = b + Wh^{t-1} + Ux^t[/$$]

## [$$] a^t = b + Wh^{t-1} + Ux^t[/$$] h^t = ?
[$$] h^t = tanh(o^t) [/$$]
## [$$] a^t = b + Wh^{t-1} + Ux^t[/$$] o^t = ?
[$$] o^t = V*h^t + c[/$$]
## [$$] a^t = b + Wh^{t-1} + Ux^t[/$$] y^t = ?
[$$] y^t = softmax(o^t) [/$$]

## train RNN with BPTT
● BPTT = Backpropagation through time
● Unroll the RNN as if they are sharing weights every layer.
● Each time step generates a gradient vector towards the weights.
● Average all the gradients collected at each time step.
 
##  vanishing gradients, max of tanh/sigmoid grads?

● Vanilla RNNs suffers at vanishing gradients problems.
● The derivative the activation nonlinearities, sigmoid or tanh, is smaller
than 1.
● max sigmoid/tanh grad is 1
● Therefore, the hidden transfer function should be a linear function.
 
## Beam search for seq decoding
● While optimal decoding is combinatorial, we can allow keeping a candidate list of size B (beam size).
● Keep top N most probable sequences, and expand each of them with the next output choice, and take N top candidates.
 ● Similar to sequential Monte Carlo.
● End up running B forward passes.

## what is  Scheduled Sampling, how to simulate test time output?

● At training stage, the network has never seen any fake sentences as input.
● At test stage, once the network generates something unlike a real
sentence, it will have less experience keep generating.
● Remedy #1: At training, at each timestep, we do a coinflip:
○ Either feed in the groundtruth input
○ Or use the network’s current output as input
But we still train the output against the groundtruth, even if the input is already sampled from the network.
● Annealing, and eventually always using network’s output as input.
● Used in Google’s Image Captioning algorithm (Bengio et al., 2015).
 
