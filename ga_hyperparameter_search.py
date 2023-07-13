"""
From https://github.com/aralab-unr/ReinforcementLearningWithGA

@INPROCEEDINGS{8675632,  
  author={Sehgal, Adarsh and La, Hung and Louis, Sushil and Nguyen, Hai},  
  title={Deep Reinforcement Learning Using Genetic Algorithm for Parameter Optimization},   
  booktitle={2019 Third IEEE International Conference on Robotic Computing (IRC)},   
  year={2019},  
  volume={},  
  number={},  
  pages={596-601},  
  doi={10.1109/IRC.2019.00121}
}

Modifications made to suit Stable Baselines 3
"""
from sb3_contrib import RecurrentPPO
from stable_baselines3.common.evaluation import evaluate_policy
from mchgenalg import GeneticAlgorithm
import mchgenalg
import argparse
from datetime import datetime



# First, define function that will be used to evaluate the fitness
def fitness_function(genome):
    
    #setting parameter values using genome
    gae_lambda = decode_function(genome[0:10])
    if gae_lambda > 1:
        gae_lambda = 1
    gamma = decode_function(genome[11:21])
    if gamma > 1:
        gamma = 1
    learning_rate = decode_function(genome[22:33])
    if learning_rate > 1:
        learning_rate = 1
    clip_range = decode_function(genome[34:44])
    if clip_range > 1:
        clip_range = 1
    ent_coef = decode_function(genome[45:55])
    if ent_coef > 1:
        ent_coef = 1
    vf_coef = decode_function(genome[56:66])
    if vf_coef > 1:
        vf_coef = 1
    
    
    model = RecurrentPPO(
        policy="MlpLstmPolicy",
        env=ENV,
        learning_rate=learning_rate,
        gamma=gamma,
        gae_lambda=gae_lambda,
        clip_range=clip_range,
        ent_coef=ent_coef,
        vf_coef=vf_coef,
    )
    model.learn(TIMESTEPS)

    env = model.get_env()
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10, warn=False)
    
    return mean_reward - std_reward

def decode_function(genome_partial):

    prod = 0
    for i,e in reversed(list(enumerate(genome_partial))):
        if e == False:
            prod += 0
        else:
            prod += 2**abs(i-len(genome_partial)+1)
    return prod/1000

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, default="CartPole-v1", help="environment ID")
    parser.add_argument("-n", "--n-timesteps", help="number of timesteps", default=100, type=int)
    args = parser.parse_args()
    
    ENV = args.env
    TIMESTEPS = args.n_timesteps

    # Configure the algorithm:
    population_size = 30
    genome_length = 66
    ga = GeneticAlgorithm(fitness_function)
    ga.generate_binary_population(size=population_size, genome_length=genome_length)

    # How many pairs of individuals should be picked to mate
    ga.number_of_pairs = 5

    # Selective pressure from interval [1.0, 2.0]
    # the lower value, the less will the fitness play role
    ga.selective_pressure = 1.5
    ga.mutation_rate = 0.1

    # If two parents have the same genotype, ignore them and generate TWO random parents
    # This helps preventing premature convergence
    ga.allow_random_parent = True # default True
    # Use single point crossover instead of uniform crossover
    ga.single_point_cross_over = False # default False

    print("starting GA run for ", ENV)

    ga.run(1000)

    best_genome, best_fitness = ga.get_best_genome()
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('hyperparameter_search/BestParameters_' + ENV + '_' + timestamp + '.txt', 'a') as output:
        output.write("gae_lambda = " + str(decode_function(best_genome[0:10])) + '\n')
        output.write("gamma = " + str(decode_function(best_genome[11:22])) + '\n')
        output.write("learning_rate = " + str(decode_function(best_genome[23:33])) + '\n')
        output.write("clip_range = " + str(decode_function(best_genome[34:44])) + '\n')
        output.write("ent_coef = " + str(decode_function(best_genome[45:55])) + '\n')
        output.write("vf_coef = " + str(decode_function(best_genome[56:66])) + '\n')

    print("done")