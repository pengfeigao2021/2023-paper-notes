from bohb import BOHB
import bohb.configspace as cs


def objective(step, alpha, beta):
    return 1 / (alpha * step + 0.1) + beta


def evaluate(params, n_iterations):
    loss = 0.0
    for i in range(int(n_iterations)):
        loss += objective(**params, step=i)
    return loss/n_iterations


if __name__ == '__main__':
    alpha = cs.CategoricalHyperparameter('alpha', [0.001, 0.01, 0.1])
    beta = cs.CategoricalHyperparameter('beta', [1, 2, 3])
    configspace = cs.ConfigurationSpace([alpha, beta])

    opt = BOHB(configspace, evaluate, max_budget=10, min_budget=1)

    # Parallel
    # opt = BOHB(configspace, evaluate, max_budget=10, min_budget=1, n_proc=4)

    logs = opt.optimize()
    print(logs)