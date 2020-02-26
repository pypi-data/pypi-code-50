"""Calculates the correct price of an ilab request, sends email if it's not."""
import math


def check_request(
        tools, req_id, req_type, all_samples, rxn_multiplier=None):
    """Validates that the request has the correct cost associated with it.

    Arguments:
        tools (IlabTools): An authenticated IlabTools object.
        req_id (string): The unique string of ints that represent a request.
        req_type (string): The contents of the 'category-name' in the request
            xml.
        all_samples (list of samples): The samples associated with the
            request.
    Keyword Arguments:
        rxn_multiplier (string): The value of the field within each sample
            that contains the reactions the sample will go through, separated
            by a ','.
    """

    # Reads (seq), prep (exome), tubes(PCR) not in this dict because the
    # pricing structure is too variable for now.
    unit_definitions = {
        "reactions": None,
        "hour": 1,
        "each": 1,
        "prep": 11,
        "application": 12,
        "plate": 96,
        "array": 384}

    charges_uri_soup = tools.get_request_charges(req_id)
    req_cost = 0
    true_cost = 0
    for soup in charges_uri_soup.values():
        service_id = soup.find("price-id").string
        # Skip services that aren't yet quantified enough for this script.
        if soup.find("name").string.split()[0] in [
                "HiSeq", "MiSeq", "NextSeq500", "Polymerase"]:
            continue

        # Skip consumables, as the price-id of these charges is falsey,
        #   and there isn't a way to find the price it should be.
        if not service_id:
            continue

        # If the service_id is not None, harvest the price info.
        cart_price = float(soup.find("cart-price").string)
        req_quant = float(soup.find("quantity").string)
        req_cost += (cart_price * req_quant)
        service_cost = tools.get_service_cost(service_id)

        # Charges that are by reaction (reactions).
        if service_cost.samples_per_unit == "reactions":
            units_used = 0
            for udf in rxn_multiplier:
                for smp in all_samples:
                    if udf in smp.udf_to_value.keys():
                        units_used += (
                            len(smp.udf_to_value[udf].split(',')))

        # Charges that are not whole numbers.
        elif service_cost.samples_per_unit == "hour":
            units_used = req_quant

        # Charges that are whole numbers or sets (
        # each, prep, plate, array, application).
        else:
            units_used = (
                math.ceil(
                    len(all_samples)
                    / unit_definitions[service_cost.samples_per_unit]))
        true_cost += service_cost.price * units_used

    return req_cost, true_cost
