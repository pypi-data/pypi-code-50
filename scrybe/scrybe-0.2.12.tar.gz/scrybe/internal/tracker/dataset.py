# TODO(chandra): Point this to the actual function in dataset tracker
def get_db_dataset_id(dataset_obj):
    if dataset_obj is None:
        return None
    return id(dataset_obj)
