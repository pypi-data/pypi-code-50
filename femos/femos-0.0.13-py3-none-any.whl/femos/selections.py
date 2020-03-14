from random import randint, sample


def get_two_size_tournament_parent_selection(individual_values, number_of_individuals):
    indices = [0] * number_of_individuals

    for index in range(number_of_individuals):
        first_individual_index = randint(0, number_of_individuals - 1)
        second_individual_index = randint(0, number_of_individuals - 1)

        first_individual_value = individual_values[first_individual_index]
        second_individual_value = individual_values[second_individual_index]

        if first_individual_value >= second_individual_value:
            indices[index] = first_individual_index
        else:
            indices[index] = second_individual_index

    return indices


def get_n_size_tournament_parent_selection(individual_values, tournament_size, number_of_individuals):
    indices = [0] * number_of_individuals
    individuals_indices = list(range(number_of_individuals))

    for index in range(number_of_individuals):
        selected_individuals = sample(individuals_indices, tournament_size)
        selected_individual_values = map(lambda individual_index: individual_values[individual_index],
                                         selected_individuals)

        zipped_values_with_indices = zip(selected_individual_values, selected_individuals)
        indices[index] = max(list(zipped_values_with_indices))[1]

    return indices


def get_age_based_offspring_selection(parents, updated_parents):
    return updated_parents
