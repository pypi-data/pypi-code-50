

def patch_callback(callback, x_sample, y_sample, validation_data, metadata_dict, class_weights, local_name_dict):
    from .callback import (
        build_keras_callback
    )
    return build_keras_callback(base=callback, x_sample=x_sample, y_sample=y_sample, validation_set=validation_data,
                                metadata_dict=metadata_dict, class_weights=class_weights,
                                local_name_dict=local_name_dict)


def get_keras_callback(x_sample, y_sample, validation_data, metadata_dict, class_weights, local_name_dict):
    import keras
    return patch_callback(callback=keras.callbacks.Callback, x_sample=x_sample, y_sample=y_sample,
                          validation_data=validation_data, metadata_dict=metadata_dict, class_weights=class_weights,
                          local_name_dict=local_name_dict)


def get_tf_keras_callback(x_sample, y_sample, validation_data, metadata_dict, class_weights, local_name_dict):
    import tensorflow as tf
    return patch_callback(callback=tf.keras.callbacks.Callback, x_sample=x_sample, y_sample=y_sample,
                          validation_data=validation_data, metadata_dict=metadata_dict, class_weights=class_weights,
                          local_name_dict=local_name_dict)
