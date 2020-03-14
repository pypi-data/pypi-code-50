from datetime import datetime, timedelta
from enum import Enum
from glob import glob
from os import path, makedirs
from pickle import dump, HIGHEST_PROTOCOL, load
from random import uniform
from statistics import mean, stdev
from time import time


class Summary(Enum):
    EPOCH = 1,
    MEAN = 2,
    STDDEV = 3,
    POPULATION_SIZE = 4,
    DURATION = 5,


def get_random_numbers(quantity, lower_threshold, upper_threshold):
    numbers = []
    for index in range(quantity):
        numbers.append(uniform(lower_threshold, upper_threshold))

    return numbers


def get_number_of_nn_weights(input_nodes, hidden_layers_nodes, output_nodes, use_bias=False):
    grouped_nodes = [input_nodes] + hidden_layers_nodes + [output_nodes]

    total = 0
    for index in range(len(grouped_nodes) - 1):
        total += grouped_nodes[index] * grouped_nodes[index + 1]

    if use_bias:
        number_of_bias_weights = sum(hidden_layers_nodes) + output_nodes
        total += number_of_bias_weights

    return total


def get_next_population(population, phenotype_strategy, evaluation_strategy, parent_selection_strategy,
                        mutation_strategy, offspring_selection_strategy):
    start_time = time()
    phenotypes = map(phenotype_strategy, population)
    phenotypes_values = evaluation_strategy(list(phenotypes))

    parent_indices = parent_selection_strategy(phenotypes_values)
    parents = map(lambda parent_index: population[parent_index], parent_indices)

    mutated_parents = map(mutation_strategy, parents)
    offspring = offspring_selection_strategy(population, list(mutated_parents))
    end_time = time()

    return offspring, phenotypes_values, start_time, end_time


def get_population_file_name(extension=".population"):
    current_timestamp = str(int(time()))
    return current_timestamp + extension


def handle_backup(backup_strategy, current_epoch, population):
    if backup_strategy is not None:
        interval = backup_strategy[0]

        if current_epoch % interval == 0:
            backup_directory = backup_strategy[1]
            file_extension = backup_strategy[2]

            makedirs(backup_directory, exist_ok=True)

            file_name = get_population_file_name(file_extension)
            backup_path = path.join(backup_directory, file_name)

            with open(backup_path, "wb+") as dump_file:
                dump(population, dump_file, HIGHEST_PROTOCOL)


def handle_backup_load(backup_path, extension):
    glob_search_string = path.join(backup_path, "*{}".format(extension))
    backup_files = glob(glob_search_string)

    if len(backup_files) == 0:
        raise FileNotFoundError('There are no backups files to load in selected directory and file extension.')

    sorted_backup_files = sorted(backup_files)
    last_backup_file = sorted_backup_files[-1]

    with open(last_backup_file, "rb") as loaded_file:
        population = load(loaded_file)

    return population


def get_epoch_summary(summary, epoch, phenotype_values, start_time, end_time):
    results = {}

    if Summary.EPOCH in summary:
        results.update({Summary.EPOCH: epoch})

    if Summary.MEAN in summary:
        results.update({Summary.MEAN: mean(phenotype_values)})

    if Summary.STDDEV in summary:
        results.update({Summary.STDDEV: stdev(phenotype_values)})

    if Summary.POPULATION_SIZE in summary:
        population_size = len(phenotype_values)
        results.update({Summary.POPULATION_SIZE: population_size})

    if Summary.DURATION in summary:
        duration = end_time - start_time
        results.update({Summary.DURATION: duration})

    return results


def handle_epoch_summary(summary_strategy, epoch, phenotype_values, start_time, end_time):
    if summary_strategy is not None:
        interval = summary_strategy[1]

        if epoch % interval == 0:
            summary = summary_strategy[0]
            output = []
            epoch_summary = get_epoch_summary(summary, epoch, phenotype_values, start_time, end_time)

            if Summary.EPOCH in summary:
                output.append(str(epoch_summary[Summary.EPOCH]))

            if Summary.MEAN in summary:
                output.append(str(epoch_summary[Summary.MEAN]))

            if Summary.STDDEV in summary:
                output.append(str(epoch_summary[Summary.STDDEV]))

            if Summary.POPULATION_SIZE in summary:
                output.append(str(epoch_summary[Summary.POPULATION_SIZE]))

            if Summary.DURATION in summary:
                output.append(str(epoch_summary[Summary.DURATION]))

            print(','.join(output))


def get_end_datetime(duration):
    start_datetime = datetime.now()
    duration_timedelta = timedelta(hours=duration)
    return start_datetime + duration_timedelta


def get_evolved_population(initial_population, phenotype_strategy, evaluation_strategy, parent_selection_strategy,
                           mutation_strategy, offspring_selection_strategy, duration, backup_strategy=None,
                           epoch_summary_strategy=None):
    tmp_population = initial_population
    end_datetime = get_end_datetime(duration)
    epoch = 0

    while datetime.now() <= end_datetime:
        tmp_population, phenotype_values, start_time, end_time = get_next_population(tmp_population, phenotype_strategy,
                                                                                     evaluation_strategy,
                                                                                     parent_selection_strategy,
                                                                                     mutation_strategy,
                                                                                     offspring_selection_strategy)

        epoch += 1
        handle_backup(backup_strategy, epoch, tmp_population)
        handle_epoch_summary(epoch_summary_strategy, epoch, phenotype_values, start_time, end_time)

    return tmp_population
