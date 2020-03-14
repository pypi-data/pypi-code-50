from argparse import ArgumentParser
from statistics import mean
from sys import getsizeof

from humanize import naturalsize

from femos.core import get_number_of_nn_weights, get_evolved_population, Summary, get_end_datetime, handle_backup_load
from femos.genotypes import SimpleGenotype, UncorrelatedOneStepSizeGenotype, UncorrelatedNStepSizeGenotype
from femos.phenotypes import Phenotype
from femos.selections import get_two_size_tournament_parent_selection, get_n_size_tournament_parent_selection, \
    get_age_based_offspring_selection

# Available genotype choices
simple_genotype_choice = 'simple_genotype'
uncorrelated_one_step_size_genotype_choice = 'uoss_genotype'
uncorrelated_n_step_size_genotype_choice = 'unss_genotype'

genotype_lookup = {
    simple_genotype_choice: 'Simple genotype (simple_genotype)',
    uncorrelated_one_step_size_genotype_choice: 'Uncorrelated one step size genotype (uoss_genotype)',
    uncorrelated_n_step_size_genotype_choice: 'Uncorrelated n step size genotype (unss_genotype)',
}

# Available summary choices
summary_epoch_choice = 'epoch'
summary_mean_choice = 'mean'
summary_stddev_choice = 'stddev'
summary_population_size_choice = 'population_size'
summary_duration_choice = 'duration'
summary_choices = [summary_epoch_choice, summary_mean_choice, summary_stddev_choice, summary_population_size_choice,
                   summary_duration_choice]

summary_lookup = {
    summary_epoch_choice: Summary.EPOCH,
    summary_mean_choice: Summary.MEAN,
    summary_stddev_choice: Summary.STDDEV,
    summary_population_size_choice: Summary.POPULATION_SIZE,
    summary_duration_choice: Summary.DURATION
}


def get_evolution_summary(arguments, input_nodes, output_nodes, memory_consumption_probe=100):
    output = [str.format('# Basic summary'),
              str.format('Input nodes: {}', input_nodes),
              str.format('Intput nodes: {}', output_nodes),
              str.format('Genotype: {}', genotype_lookup[arguments.genotype]),
              str.format('Hidden layer nodes: {}', arguments.hidden_layer_nodes),
              str.format('Weight lower threshold: {}', arguments.weight_lower_threshold),
              str.format('Weight upper threshold: {}', arguments.weight_upper_threshold),
              str.format('Population size: {}', arguments.population_size),
              str.format('Tournament size: {}', arguments.tournament_size),
              str.format('Duration (hours): {}', arguments.duration),
              str.format('Use bias: {}', arguments.bias),
              str.format('# Genotype specific summary')]

    if arguments.genotype == simple_genotype_choice:
        output.append(str.format('Mutation mean: {}', arguments.mutation_mean))
        output.append(str.format('Mutation standard deviation: {}', arguments.mutation_standard_deviation))

    if arguments.genotype == uncorrelated_one_step_size_genotype_choice or arguments.genotype == uncorrelated_n_step_size_genotype_choice:
        output.append(
            str.format('Mutation step size lower threshold: {}', arguments.mutation_step_size_lower_threshold))
        output.append(
            str.format('Mutation step size upper threshold: {}', arguments.mutation_step_size_upper_threshold))
        output.append(str.format('Tau 1: {}', arguments.tau1))

        if arguments.genotype == uncorrelated_n_step_size_genotype_choice:
            output.append(str.format('Tau 2: {}', arguments.tau2))

    output.append(str.format('# Calculated summary'))
    number_of_nn_weights = get_number_of_nn_weights(input_nodes, arguments.hidden_layer_nodes,
                                                    output_nodes)
    output.append(str.format('Number of neural network weights: {}', number_of_nn_weights))

    # Calculating memory consumption
    demo_genotype_iterator = range(memory_consumption_probe)

    if arguments.genotype == simple_genotype_choice:
        demo_genotypes = map(
            lambda index: SimpleGenotype.get_random_genotype(number_of_nn_weights, arguments.weight_lower_threshold,
                                                             arguments.weight_upper_threshold), demo_genotype_iterator)
        demo_genotype_sizes = list(map(lambda demo_genotype: getsizeof(demo_genotype.weights), demo_genotypes))

    if arguments.genotype == uncorrelated_one_step_size_genotype_choice:
        demo_genotypes = map(lambda index: UncorrelatedOneStepSizeGenotype.get_random_genotype(number_of_nn_weights,
                                                                                               arguments.weight_lower_threshold,
                                                                                               arguments.weight_upper_threshold,
                                                                                               arguments.mutation_step_size_lower_threshold,
                                                                                               arguments.mutation_step_size_upper_threshold),
                             demo_genotype_iterator)
        demo_genotype_sizes = list(
            map(lambda demo_genotype: getsizeof(demo_genotype.weights) + getsizeof([demo_genotype.mutation_step_size]),
                demo_genotypes))

    if arguments.genotype == uncorrelated_n_step_size_genotype_choice:
        demo_genotypes = map(lambda index: UncorrelatedNStepSizeGenotype.get_random_genotype(number_of_nn_weights,
                                                                                             arguments.weight_lower_threshold,
                                                                                             arguments.weight_upper_threshold,
                                                                                             arguments.mutation_step_size_lower_threshold,
                                                                                             arguments.mutation_step_size_upper_threshold),
                             demo_genotype_iterator)
        demo_genotype_sizes = list(
            map(lambda demo_genotype: getsizeof(demo_genotype.weights) + getsizeof(demo_genotype.mutation_step_sizes),
                demo_genotypes))

    mean_demo_genotype_size = mean(demo_genotype_sizes) * arguments.population_size
    output.append(str.format('Calculated memory consumption (Python list): {}', naturalsize(mean_demo_genotype_size)))
    output.append(str.format('Approximate end time: {}', get_end_datetime(arguments.duration).isoformat(sep=' ')))

    output.append(str.format('# Utils summary'))
    output.append(str.format('Epoch summary: {}', arguments.epoch_summary))
    if arguments.epoch_summary:
        output.append(str.format('Epoch summary features: {}', arguments.epoch_summary_features))
        output.append(str.format('Epoch summary interval: {}', arguments.epoch_summary_interval))

    output.append(str.format('Population backup summary: {}', arguments.population_backup))
    if arguments.population_backup:
        output.append(str.format('Population backup directory: {}', arguments.population_backup_directory))
        output.append(str.format('Population backup interval: {}', arguments.population_backup_interval))
        output.append(str.format('Population backup file extension: .{}', arguments.population_backup_file_extension))

    if arguments.initial_population_directory:
        output.append(str.format('Initial population directory: {}', arguments.initial_population_directory))
        output.append(str.format('Initial population file extension: {}', arguments.initial_population_file_extension))

    return '\n'.join(output)


def get_core_argument_parser():
    parser = ArgumentParser(description='Femos CLI - Command line interface for my small library for neuroevolution.')
    parser.add_argument('genotype', metavar='G', type=str,
                        choices=[simple_genotype_choice, uncorrelated_one_step_size_genotype_choice,
                                 uncorrelated_n_step_size_genotype_choice],
                        help='Describes genotype type: simple_genotype - SimpleGenotype, uoss_genotype - UncorrelatedOneStepSizeGenotype, '
                             'unss_genotype - UncorrelatedNStepSizeGenotype')

    parser.add_argument('--bias', help='Use bias', action='store_true', default=False)
    parser.add_argument('--hidden_layer_nodes', help='List of nodes in hidden layer', type=int, default=[],
                        nargs='+')
    parser.add_argument("--weight_lower_threshold", help="Lower threshold value of ann weights", type=float,
                        default=-1.0)
    parser.add_argument("--weight_upper_threshold", help="Upper threshold value of ann weights", type=float,
                        default=1.0)
    parser.add_argument("--mutation_step_size_lower_threshold",
                        help="Lower threshold value for genotype mutation step size",
                        type=float, default=-0.2)
    parser.add_argument("--mutation_step_size_upper_threshold",
                        help="Upper threshold value for genotype mutation step size",
                        type=float, default=0.2)
    parser.add_argument("--population_size", help="Number of individuals in population", type=int, default=20)
    parser.add_argument("--tournament_size", help="Number of individuals to rival in tournament selection",
                        type=int, default=3)
    parser.add_argument('--duration', help="Duration of evolution in hours", type=float, default=1)
    parser.add_argument("--tau1", help="Mutation operator parameter - tau1", type=float, default=0.001)
    parser.add_argument("--tau2", help="Mutation operator parameter - tau2", type=float, default=0.01)

    parser.add_argument('--mutation_mean', type=float, default=0)
    parser.add_argument('--mutation_standard_deviation', type=float, default=0.1)

    parser.add_argument('--epoch_summary', action='store_true', default=False)
    parser.add_argument('--epoch_summary_features', type=str, nargs='+', choices=summary_choices,
                        default=[summary_epoch_choice, summary_mean_choice, summary_stddev_choice,
                                 summary_duration_choice])
    parser.add_argument('--epoch_summary_interval', type=int, default=5)

    parser.add_argument('--population_backup', action='store_true', default=False)
    parser.add_argument('--population_backup_directory', type=str, default='backups')
    parser.add_argument('--population_backup_interval', type=int, default=5)
    parser.add_argument('--population_backup_file_extension', type=str, default='.population')
    parser.add_argument('--initial_population_directory', type=str)
    parser.add_argument('--initial_population_file_extension', type=str, default='.population')
    parser.add_argument('--dry_run', action='store_true', default=False)
    return parser


def handle_evolution_run(input_nodes, output_nodes, evaluation_strategy):
    argument_parser = get_core_argument_parser()
    arguments = argument_parser.parse_args()
    evolution_summary = get_evolution_summary(arguments, input_nodes, output_nodes)

    print(evolution_summary)
    if not arguments.dry_run:

        def phenotype_strategy(genotype):
            return Phenotype.get_phenotype_from_genotype(genotype, input_nodes, arguments.hidden_layer_nodes,
                                                         output_nodes, arguments.bias)

        def parent_selection_strategy(phenotype_values):
            if arguments.tournament_size == 2:
                return get_two_size_tournament_parent_selection(phenotype_values, arguments.population_size)
            else:
                return get_n_size_tournament_parent_selection(phenotype_values, arguments.tournament_size,
                                                              arguments.population_size)

        def mutation_strategy(genotype):
            if arguments.genotype == simple_genotype_choice:
                return SimpleGenotype.get_mutated_genotype(genotype, arguments.mutation_mean,
                                                           arguments.mutation_standard_deviation)

            if arguments.genotype == uncorrelated_one_step_size_genotype_choice:
                return UncorrelatedOneStepSizeGenotype.get_mutated_genotype(genotype, arguments.tau1)

            if arguments.genotype == uncorrelated_n_step_size_genotype_choice:
                return UncorrelatedNStepSizeGenotype.get_mutated_genotype(genotype, arguments.tau1, arguments.tau2)

        def offspring_selection_strategy(parents, mutated_parents):
            return get_age_based_offspring_selection(parents, mutated_parents)

        number_of_nn_weights = get_number_of_nn_weights(input_nodes, arguments.hidden_layer_nodes,
                                                        output_nodes, arguments.bias)
        if arguments.genotype == simple_genotype_choice:
            initial_population = SimpleGenotype.get_random_genotypes(arguments.population_size, number_of_nn_weights,
                                                                     arguments.weight_lower_threshold,
                                                                     arguments.weight_upper_threshold)

        if arguments.genotype == uncorrelated_one_step_size_genotype_choice:
            initial_population = UncorrelatedOneStepSizeGenotype.get_random_genotypes(arguments.population_size,
                                                                                      number_of_nn_weights,
                                                                                      arguments.weight_lower_threshold,
                                                                                      arguments.weight_upper_threshold,
                                                                                      arguments.mutation_step_size_lower_threshold,
                                                                                      arguments.mutation_step_size_upper_threshold)

        if arguments.genotype == uncorrelated_n_step_size_genotype_choice:
            initial_population = UncorrelatedNStepSizeGenotype.get_random_genotypes(arguments.population_size,
                                                                                    number_of_nn_weights,
                                                                                    arguments.weight_lower_threshold,
                                                                                    arguments.weight_upper_threshold,
                                                                                    arguments.mutation_step_size_lower_threshold,
                                                                                    arguments.mutation_step_size_upper_threshold)

        population_backup = None
        if arguments.population_backup:
            population_backup = [arguments.population_backup_interval, arguments.population_backup_directory,
                                 arguments.population_backup_file_extension]

        epoch_summary_strategy = None
        if arguments.epoch_summary:
            summary_features = list(
                map(lambda summary_choice: summary_lookup[summary_choice], arguments.epoch_summary_features))
            epoch_summary_strategy = [summary_features, arguments.epoch_summary_interval]

        if arguments.initial_population_directory:
            initial_population = handle_backup_load(arguments.initial_population_directory,
                                                    arguments.initial_population_file_extension)

        return get_evolved_population(initial_population, phenotype_strategy, evaluation_strategy,
                                      parent_selection_strategy, mutation_strategy, offspring_selection_strategy,
                                      arguments.duration, population_backup, epoch_summary_strategy)
