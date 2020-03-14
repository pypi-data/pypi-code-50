from glob import glob
from random import random
from shutil import rmtree

from femos.core import get_number_of_nn_weights, get_random_numbers, get_next_population, get_population_file_name, \
    get_evolved_population, handle_backup_load
from femos.genotypes import SimpleGenotype
from femos.phenotypes import Phenotype
from femos.selections import get_two_size_tournament_parent_selection, get_age_based_offspring_selection


def test_get_random_numbers():
    quantity = 500
    lower_threshold = -1
    upper_threshold = 1

    random_numbers = get_random_numbers(quantity, lower_threshold, upper_threshold)
    assert len(random_numbers) == quantity

    for element in random_numbers:
        assert lower_threshold <= element <= upper_threshold


def test_get_number_of_nn_weights():
    assert get_number_of_nn_weights(9, [4, 4], 9) == 88
    assert get_number_of_nn_weights(9, [], 9) == 81
    assert get_number_of_nn_weights(9, [8, 8, 8], 1) == 208


def test_get_next_population():
    number_of_genotypes = 40
    input_nodes = 4
    hidden_layers_nodes = []
    output_nodes = 3
    number_of_nn_weights = get_number_of_nn_weights(input_nodes, hidden_layers_nodes, output_nodes)
    weight_lower_threshold = -1
    weight_upper_threshold = 1
    mutation_mean = 0
    mutation_standard_deviation = 0.2

    def phenotype_strategy(genotype):
        return Phenotype.get_phenotype_from_genotype(genotype, input_nodes, hidden_layers_nodes, output_nodes)

    # Fake evaluation function, assign random number form 0 to 1 to each phenotype
    def evaluation_strategy(phenotypes):
        number_of_phenotypes = len(phenotypes)

        evaluation = [0] * number_of_phenotypes
        for index in range(number_of_phenotypes):
            evaluation[index] = random()

        return evaluation

    def parent_selection_strategy(phenotypes_values):
        return get_two_size_tournament_parent_selection(phenotypes_values, number_of_genotypes)

    def mutation_strategy(genotype):
        return SimpleGenotype.get_mutated_genotype(genotype, mutation_mean, mutation_standard_deviation)

    def offspring_selection_strategy(parents, mutated_parents):
        return get_age_based_offspring_selection(parents, mutated_parents)

    initial_population = SimpleGenotype.get_random_genotypes(number_of_genotypes, number_of_nn_weights,
                                                             weight_lower_threshold, weight_upper_threshold)

    next_population, phenotype_values, start_time, end_time = get_next_population(initial_population, phenotype_strategy, evaluation_strategy,
                                          parent_selection_strategy, mutation_strategy, offspring_selection_strategy)

    assert len(next_population) == number_of_genotypes

    for element in next_population:
        assert type(element) is SimpleGenotype


def test_get_population_file_name():
   generated_population_name = get_population_file_name('.popu')
   assert generated_population_name.split('.')[-1] == "popu"

   generated_population_name = get_population_file_name('.population')
   assert generated_population_name.split('.')[-1] == "population"


def test_population_backup():
    number_of_genotypes = 40
    input_nodes = 4
    hidden_layers_nodes = []
    output_nodes = 3
    number_of_nn_weights = get_number_of_nn_weights(input_nodes, hidden_layers_nodes, output_nodes)
    weight_lower_threshold = -1
    weight_upper_threshold = 1
    mutation_mean = 0
    mutation_standard_deviation = 0.2

    def phenotype_strategy(genotype):
        return Phenotype.get_phenotype_from_genotype(genotype, input_nodes, hidden_layers_nodes, output_nodes)

    # Fake evaluation function, assign random number form 0 to 1 to each phenotype
    def evaluation_strategy(phenotypes):
        number_of_phenotypes = len(phenotypes)

        evaluation = [0] * number_of_phenotypes
        for index in range(number_of_phenotypes):
            evaluation[index] = random()

        return evaluation

    def parent_selection_strategy(phenotypes_values):
        return get_two_size_tournament_parent_selection(phenotypes_values, number_of_genotypes)

    def mutation_strategy(genotype):
        return SimpleGenotype.get_mutated_genotype(genotype, mutation_mean, mutation_standard_deviation)

    def offspring_selection_strategy(parents, mutated_parents):
        return get_age_based_offspring_selection(parents, mutated_parents)

    initial_population = SimpleGenotype.get_random_genotypes(number_of_genotypes, number_of_nn_weights,
                                                             weight_lower_threshold, weight_upper_threshold)

    backup = [5, "backups/evo1", ".population"]
    evolved_population = get_evolved_population(initial_population, phenotype_strategy, evaluation_strategy,
                                                parent_selection_strategy, mutation_strategy,
                                                offspring_selection_strategy, 0.01, backup)

    backup_files = glob("backups/evo1/*.population")
    assert len(backup_files) > 0

    # Clear after save
    rmtree("backups", ignore_errors=True)


def test_load_population_backup():
    number_of_genotypes = 40
    input_nodes = 4
    hidden_layers_nodes = []
    output_nodes = 3
    number_of_nn_weights = get_number_of_nn_weights(input_nodes, hidden_layers_nodes, output_nodes)
    weight_lower_threshold = -1
    weight_upper_threshold = 1
    mutation_mean = 0
    mutation_standard_deviation = 0.2

    def phenotype_strategy(genotype):
        return Phenotype.get_phenotype_from_genotype(genotype, input_nodes, hidden_layers_nodes, output_nodes)

    # Fake evaluation function, assign random number form 0 to 1 to each phenotype
    def evaluation_strategy(phenotypes):
        number_of_phenotypes = len(phenotypes)

        evaluation = [0] * number_of_phenotypes
        for index in range(number_of_phenotypes):
            evaluation[index] = random()

        return evaluation

    def parent_selection_strategy(phenotypes_values):
        return get_two_size_tournament_parent_selection(phenotypes_values, number_of_genotypes)

    def mutation_strategy(genotype):
        return SimpleGenotype.get_mutated_genotype(genotype, mutation_mean, mutation_standard_deviation)

    def offspring_selection_strategy(parents, mutated_parents):
        return get_age_based_offspring_selection(parents, mutated_parents)

    initial_population = SimpleGenotype.get_random_genotypes(number_of_genotypes, number_of_nn_weights,
                                                             weight_lower_threshold, weight_upper_threshold)

    backup = [1, 'backups/evo1', '.population']
    evolved_population = get_evolved_population(initial_population, phenotype_strategy, evaluation_strategy,
                                                parent_selection_strategy, mutation_strategy,
                                                offspring_selection_strategy, 0.01, backup)

    population = handle_backup_load('backups/evo1', '.population')
    assert len(population) == 40
    assert population == evolved_population

    # Clear after save
    rmtree("backups", ignore_errors=True)
