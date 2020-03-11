import xmltodict

from ..services.requests import extract_invoice, validate_vat, validation
from .commons import read_pdf


def convert_to_xml(
    path,
    output_path,
    extractor_endpoint,
    tax_rate_as_percentage=False,
    vat_validator_endpoint=None,
    validation_endpoint=None,
    token=None,
):
    result = {}
    _, pdf = read_pdf(path)

    # Extraction
    _, result["invoiceExtractor"] = extract_invoice(
        (path, pdf), extractor_endpoint, "application/pdf", token
    )

    # Validation
    if validation_endpoint:
        result["validation"] = validation(
            result["invoiceExtractor"], validation_endpoint
        )

    # Vat validation
    if vat_validator_endpoint:
        result["vatValidator"] = validate_vat(
            result["invoiceExtractor"], vat_validator_endpoint
        )

    merge_validation(result)
    clean_extractor(result)
    clean_validation(result["validation"])

    # One of the dirties hack I've ever done, here. I'm sorry
    if tax_rate_as_percentage:
        try:
            for tax_line in result["invoiceExtractor"]["entities"]["totals"]["tax"]:
                tax_line["rate"]["#text"] = str(
                    round(float(tax_line["rate"]["#text"]) * 100, ndigits=2)
                )
        except (KeyError, TypeError):
            # guarding against the structure invoiceExtractor.entities.totals.tax
            # not being respected or whatever is there not being a list of objects
            # with a rate in it; failing silently if that's the case
            pass

    file_name = path.split("/")[-1]
    file_name = file_name.split(".")[0]
    xmltodict.unparse(
        {"hypatosResults": result},
        output=open(f"{output_path}/{file_name}.xml", "w+"),
        pretty=True,
    )


def merge_validation(result):
    return_dict = {}

    def traverse_merge_items(entities, _dict, validation):
        for entity, value in entities.items():
            # TODO: Make propper solution
            if entity == "ibanAll":
                continue

            entity_got_validation = validation and entity in validation

            # Entity is a key and value is a dict
            if isinstance(value, dict):
                _dict[entity] = {}
                traverse_merge_items(
                    entities[entity],
                    _dict[entity],
                    validation[entity][0] if entity_got_validation else None,
                )
            # Entity is a key and value is a list
            elif isinstance(value, list):
                _dict[entity] = []
                validation_idx = 0

                for idx in range(0, len(value)):
                    # Try hack when there is a validation error for a item and previous has not.
                    entity_got_validation = (
                        entity_got_validation and str(idx) in validation[entity][0]
                    )
                    try:
                        _dict[entity].append({})
                        traverse_merge_items(
                            entities[entity][idx],
                            _dict[entity][idx],
                            validation[entity][0][str(idx)][0]
                            if entity_got_validation
                            else None,
                        )
                        # _dict[entity][idx]["@idx"] = str(idx)
                        if entity_got_validation:
                            if entity == "tax":
                                singular = entity
                            else:
                                singular = f"{entity[:-1]}"

                            if singular not in validation[entity][0]:
                                validation[entity][0][singular] = []

                            validation[entity][0][singular].append({})
                            validation[entity][0][singular][
                                validation_idx
                            ] = validation[entity][0][str(idx)][0]
                            del validation[entity][0][str(idx)]
                            validation[entity][0][singular][idx]["@idx"] = idx
                            validation_idx += 1
                    except (KeyError, IndexError):
                        _dict[entity].pop(-1)
            # Entity is a field with no value
            elif not value:
                _dict[entity] = {
                    "@risk": "high",
                    "#text": "",
                }
            # Entity is a dict and value is a string
            else:
                _dict[entity] = {
                    "@risk": create_risk(entity, validation[entity])
                    if entity_got_validation
                    else "low",
                    "#text": str(value),
                }

    if "validation" in result:
        traverse_merge_items(
            result["invoiceExtractor"]["entities"], return_dict, result["validation"]
        )
    else:
        traverse_merge_items(result["invoiceExtractor"]["entities"], return_dict)

    result["invoiceExtractor"]["entities"] = return_dict


def clean_extractor(result):
    """Structures list fields from invoice extractor to be plural key, singles nested dicts.

    Arguments:
        result {[type]} -- [description]
    """
    extractor_resp = result["invoiceExtractor"]

    # Items
    if "items" in extractor_resp["entities"]:
        items = extractor_resp["entities"]["items"]

        del extractor_resp["entities"]["items"]

        extractor_resp["entities"]["items"] = {}
        extractor_resp["entities"]["items"]["item"] = items

    # Taxes
    if "tax" in extractor_resp["entities"]["totals"]:
        taxes = extractor_resp["entities"]["totals"]["tax"]

        del extractor_resp["entities"]["totals"]["tax"]

        extractor_resp["entities"]["totals"]["taxes"] = {}
        extractor_resp["entities"]["totals"]["taxes"]["tax"] = taxes

    # Terms
    if "terms" in extractor_resp["entities"]["payment"]:
        terms = extractor_resp["entities"]["payment"]["terms"]

        del extractor_resp["entities"]["payment"]["terms"]

        extractor_resp["entities"]["payment"]["terms"] = {}
        extractor_resp["entities"]["payment"]["terms"]["term"] = terms

    del (
        extractor_resp["probabilities"],
        extractor_resp["infos"],
    )


def clean_validation(validation):
    if "totals" in validation:
        if "tax" in validation["totals"][0]:
            validation["totals"][0]["taxes"] = validation["totals"][0]["tax"]
            del validation["totals"][0]["tax"]


def create_risk(entity, validation_errors):
    """ Create risk flag """
    err_amount = len(validation_errors)

    if err_amount == 0:
        return "low"
    elif err_amount == 1:
        return "med"
    else:
        return "high"
