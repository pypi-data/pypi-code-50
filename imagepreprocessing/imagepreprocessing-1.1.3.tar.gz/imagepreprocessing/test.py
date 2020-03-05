from imagepreprocessing import create_training_data_keras, make_prediction_from_directory_keras, make_prediction_from_array_keras, create_training_data_yolo, yolo_annotation_tool, draw_bounding_boxes,create_cfg_file_yolo, make_prediction_from_directory_yolo, create_confusion_matrix, train_test_split, auto_annotation_by_random_points

source_path = "C:\\Users\\can\\ProjectDependencies\\datasets\\deep_learning\\17flowers\\jpg"
# source_path = "\\Users\can\\ProjectDependencies\\datasets\\deep_learning\\catdog_data\\PetImages"

save_path = "C:\\Users\\can\\Desktop\\food"

images_path = "C:\\Users\\can\\PROJECTS\\PythonProjects\\deep_learning\\test_images\\food2"
model_path = "C:\\Users\\can\\PROJECTS\\PythonProjects\\deep_learning\\saved_models\\a.h5"

class_names = ["elma","ayva","armut"]



# create_training_data_keras(source_path,grayscale=False,image_size=(224),normalize=255,validation_split=0.2,convert_array_and_reshape=True,percent_to_use=1)



# auto_annotation_by_random_points("C:\\Users\\can\\Desktop\\0",1)

yolo_annotation_tool("test_stuff\\images", "test_stuff\\obj.names")

# yolo_annotation_tool("\\Users\\can\\Desktop\\yolo_context_test_trafic_sign\\trafic_sign_elle_montaj\\Train", "\\Users\\can\\Desktop\\yolo_context_test_trafic_sign\\trafic_sign_elle_montaj\\obj.names")


# draw_bounding_boxes("test_stuff\\img_pats.txt", "test_stuff\\obj.names", save_path="test_stuff\\annoted_images")


# auto creates random annotations for all images it needs 4 values (smallest_center, biggest_center, smallest_dimension, biggest_dimension) ex:(0.4,0.6,0.8,0.9)
# values should be between 0 and 1 
# if your dataset is cropped and all of your objects at the center (0.4,0.6,0.8,0.9) this mostly works fine 


# create_training_data_yolo(source_path, train_machine_path_sep = "/", percent_to_use = 1, auto_label_by_center=(0.4,0.6,0.8,0.9),validation_split = 0.2, create_cfg_file = True)


# create_cfg_file_yolo("C:\\Users\\can\\Desktop", 50, batch=64, sub=16, width=416, height=416)


# x, y, x_val, y_val = create_training_data_keras(source_path, save_path = None, validation_split=0.2, percent_to_use=0.1)

# x, y, test_x, test_y =  train_test_split(x,y, save_path=None)


# predictions = make_prediction_from_array(test_x, model_path, print_output=False)

# create_confusion_matrix(predictions,test_y,class_names=class_names, one_hot=True)




# class_names = ["elma","ayva","armut"]
# classes =     [0,0,0, 1,1,1, 2,2,2]
# predictions = [0,0,0, 0,1,1, 2,1,2]

# pred = make_prediction_from_directory(images_path, model_path, print_output=False)

# create_confusion_matrix(predictions,classes,class_names=class_names)






# # BUNU YAP BI ARA
# import keras
# import numpy as np
# model = keras.models.load_model(model_path)
# score = model.evaluate(test_x, test_y, verbose=0)
# print('Test loss:', score[0])
# print('Test accuracy:', score[1])
# print(score)



