# HPO
Hyperparameter Optimization
todo:
* CMA-ES
* BO Shahriari et al. [132] and Brochu et al. [16].
* TPE

## common black box opt methods?
1. Grid Search: Cartesian product of these sets, bad when increasing the resolution
2. Random Search(baseline): until a certain budget, good when some hyperparameters are much more important than others, easier parallelization
3. Population-based methods, such as genetic algorithms, CMA-ES(SOTA)
   
## Bayesian optimization is an iterative algorithm with which two key ingredients?
1. surrogate model : the surrogate model is fitted to all observations of the target function made so far
2. acquisition function

## what is this acquisition function: [$$] E[I(\lambda)] = E[max(f_{min} - Y, 0)] [/$$]
expected improvement (EI)


## Multi-fidelity methods cast such manual heuristics into formal algorithms, using so-called [???] approximations of the actual loss function to minimize?
low fidelity

## Multi-fidelity methods cast such manual heuristics into formal algorithms. A common technique to speed up manual tuning is therefore to probe an algorithm/hyperparameter configuration on [???] the data
a small subset of

## (Multi-fidelity)Successive halving: for a budget, query [???] for that budget; then, and [???] successively repeat until only a single algorithm is left. Suffers from the budget- vs-number of configurations trade off.

1. all algorithms 
2. remove the half that performed worst
3. double the budget 2 


## HyperBand [87] is a hedging strategy designed to combat this problem when selecting from randomly sampled configurations. It divides the total budget into [???], to then call successive halving as a subroutine on each set of random configurations. 
several combinations of number of configurations vs. budget for each

##  BOHB combines [???] and HyperBand
Bayesian optimization