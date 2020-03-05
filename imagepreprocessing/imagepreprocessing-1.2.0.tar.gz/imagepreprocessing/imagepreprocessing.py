import os
import random
import pickle
import itertools 
from shutil import copyfile

from .file_operations import __read_from_file, __write_to_file
from .convert_annotations import __convert_annotations_opencv_to_yolo, __convert_annotations_yolo_to_opencv
from .other_fuctions import __run_shell_command
from .cfg_templates import __get_cfg_template


# from file_operations import __read_from_file, __write_to_file
# from convert_annotations import __convert_annotations_opencv_to_yolo, __convert_annotations_yolo_to_opencv
# from other_fuctions import __run_shell_command
# from cfg_templates import __get_cfg_template

 


# keras functions

def create_training_data_keras(source_path, save_path = None, image_size = (224,224), percent_to_use = 1, validation_split = 0, normalize = 255, grayscale = False, one_hot = True, shuffle = True, convert_array_and_reshape = True, files_to_exclude = [".DS_Store",""]):
    """
    Creates train ready data for classification from image data
    Takes all the image directories alphabetically in a main directory 

    # Arguments:
        source_path: source path of the images see input format
        save_path (None): save path for clean training data 
        image_size ((224,224)): size of the images for resizing tuple of 2 ints or a single int
        percent_to_use (1): percentage of data that will be used
        validation_split (0.2): splits validation data with given percentage give 0 if you don't want validation split
        normalize (255): (pass None or False if you don't want normalization) divides all images by 255 this normalizes images if pixel values are maximum of 255 if it is different change this value   
        grayscale (False): converts images to grayscale
        one_hot (True): makes one hot encoded y train if True if not uses class indexes as labels
        shuffle (True): shuffle the data
        convert_array_and_reshape (True): converts list to numpy array and reshapes images at the and if True
        files_to_exclude ([".DS_Store",""]): list of file names to exclude in the image directory (can be hidden files)

    # Returns:
        List or numpy array of train data optionally validation data
        if validation_split is 0 -> x, y
        if validation_split is not 0 -> x, y, x_val, y_val

    # Save:
        Saves x train and y train optionally validation x and y 
        Save format is .pkl (pickle data)
        If you want you can prevent saveing the file by passing None as save_path

    # Input format:
        source_path = some_dir
        
        /some_dir
        ├──/class1
            ├──img1.jpg
            ├──img2.jpg
        ├──/class2
            ├──img1.jpg

    # Output format:
        save_path = save/food_data

        save/food_data_x_train.pkl
        save/food_data_y_train.pkl   
        save/food_data_x_validation.pkl
        save/food_data_y_validation.pkl   
        
    # Example:
        ``python
            source_path = "C:\\Users\\can\\datasets\\deep_learning\\food-101\\only3"
            save_path = "C:\\Users\\can\\Desktop\\food10class1000sampleeach"
            create_training_data_keras(source_path, save_path, image_size = 299, validation_split=0.1, percent_to_use=0.1, grayscale = True, files_to_exclude=["excludemoe","hi.txt"])
        ``                      
    """

    import numpy as np
    import cv2

    # image_size parsing
    if(type(image_size) == tuple):
        if(len(image_size) == 2 and type(image_size[0]) == int and type(image_size[1]) == int):
            img_width = image_size[0]
            img_height = image_size[1]
        else:
            raise ValueError("image_size tuple should have 2 int values")
    elif(type(image_size) == int):
        img_width = image_size
        img_height = image_size
    else:
        raise ValueError("image_size should be an int or a tuple with 2 int values")

    if(img_width < 1 or img_height < 1):
        raise ValueError("image_size should be bigger than 0")


    # raise error on wrong percentage
    if(validation_split < 0 or validation_split > 1):
        raise ValueError("Validation_split should be between 0 and 1")

    


    x = []
    y = [] 
    x_val = []
    y_val = []

    CATEGORIES = os.listdir(source_path)  # get all file names from main dir
    CATEGORIES.sort()                     # sort the directories

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in CATEGORIES: 
            CATEGORIES.remove(exclude)
    


    # loop in the main directory
    for category_index, category in enumerate(CATEGORIES):

        path = os.path.join(source_path, category)
        number_of_categories = len(CATEGORIES)
        index_of_category = CATEGORIES.index(category)

        # if wrong directory style given raise error
        try:
            images = os.listdir(path)
        except NotADirectoryError as e:
            raise NotADirectoryError(e,"""
        Your dataset should look like this
        /source_path
        |---/dir1(class1)
            |---img1.jpg
            |---img2.jpg
        |---/dir2(class2)
            |---img1.jpg
            ... 
        """)

        # raise error on wrong percentage
        if(percent_to_use <= 0 or percent_to_use > 1):
            raise ValueError("Percentage should be between 0 and 1")
        elif(int(percent_to_use * len(images)) == 0):
            raise ValueError("Percentage is too small for this directory {0}".format(category))
        else:
            stop_index = int(len(images)*percent_to_use)
        
        
        is_there_broken_images = ""
        # loop inside each category folder with itertools for stoping on a percentage
        for image_index, img in enumerate(itertools.islice(images , 0, stop_index)):

            # print percent info
            print("File name: {0} - {1}/{2}  Image:{3}/{4} {5}".format(category, index_of_category+1, number_of_categories, image_index+1, stop_index, is_there_broken_images), end="\r")
            
            # there can be broken images
            try:
                # convert grayscale
                if(grayscale):
                    temp_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                else:
                    temp_array = cv2.imread(os.path.join(path, img)) 

                # resize image
                img_array = cv2.resize(temp_array, (img_width, img_height))   

                # one hot encoding
                if(one_hot):  
                    temp_y = []
                    for i in range(len(CATEGORIES)):
                        if(i == category_index):
                            temp_y.append(1)
                        else:
                            temp_y.append(0)
                    y.append(temp_y)
                # if one hot is not selected use index of the file as label
                else:
                    y.append(index_of_category)  

                x.append(img_array)
            except:
                is_there_broken_images = " ---There are some corrupted images in this directory, skiping those images---"
                pass

        print("")


    if(shuffle):
        print("\n...shuffling...")
        xy = list(zip(x,y))
        random.shuffle(xy)
        x, y = list(zip(*xy))
    

    # validation split
    if(validation_split):
        print("\n...splitting validation...")
        if(int(validation_split * len(images)) == 0):
            raise ValueError("Validation split is too small for this set")

        # split
        train_percent = int(len(x) - (validation_split * len(x)))
        x_val = x[train_percent:]
        y_val = y[train_percent:]
        x = x[:train_percent]
        y = y[:train_percent]

        print("train x: {0} train y: {1}\nvalidation x: {2} validation y: {3}".format(len(x),len(y),len(x_val),len(y_val)))
    else:
        print("\ntrain x: {0} train y: {1}".format(len(x),len(y)))



    # convert array and reshape 
    if(convert_array_and_reshape):
        print("\n...converting train to array...")
        if(grayscale):
            third_dimension = 1
        else:
            third_dimension = 3
    
        x = np.array(x).reshape(-1, img_width, img_height, third_dimension)
        y = np.array(y)

        print("Array converted shape of train x: {0}\nArray converted shape of train y: {1}".format(x.shape,y.shape))

        if(validation_split):
            print("\n...converting validation to array...")
            x_val = np.array(x_val).reshape(-1, img_width, img_height, third_dimension)
            y_val = np.array(y_val)    
            print("Array converted shape of validation x: {0}\nArray converted shape of validation y: {1}".format(x_val.shape,y_val.shape))


    # normalize 
    if(normalize):
        if(convert_array_and_reshape):
            print("\n...normalizing train x...")
            x = x/normalize
            print("Normalized example from train set (x[0][0][0]): {0}".format(x[0][0][0]))
            if(validation_split):
                print("\n...normalizing validation x...")
                x_val = x_val/normalize
                print("Normalized example from validation set (x_val[0][0][0]): {0}".format(x_val[0][0][0]))
        else:
            print("\n...normalizing train x (if normalization is slow use convert_array_and_reshape with normalization)...")
            x = (np.array(x)/normalize).tolist()
            print("Normalized example from train set (x[0][0][0]): {0}".format(x[0][0][0]))
            if(validation_split):
                print("\n...normalizing validation x...")
                x_val = (np.array(x_val)/normalize).tolist()
                print("Normalized example from validation set (x_val[0][0][0]): {0}".format(x_val[0][0][0]))


    # save
    if(save_path != None):
        with open(save_path + "_x_train.pkl", "wb") as file:
            pickle.dump(x, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("\nfile saved -> {0}{1}".format(save_path,"_x_train.pkl"))

        with open(save_path + "_y_train.pkl", "wb") as file:
            pickle.dump(y, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}".format(save_path,"_y_train.pkl"))
        
        if(validation_split != 0):
            with open(save_path + "_x_validation.pkl", "wb") as file:
                pickle.dump(x_val, file, protocol=pickle.HIGHEST_PROTOCOL)
                print("file saved -> {0}{1}".format(save_path,"_x_validation.pkl"))

            with open(save_path + "_y_validation.pkl", "wb") as file:
                pickle.dump(y_val, file, protocol=pickle.HIGHEST_PROTOCOL)
                print("file saved -> {0}{1}\n".format(save_path,"_y_validation.pkl"))
        
    if(validation_split):
        return x, y, x_val, y_val
    else:
        return x, y


def make_prediction_from_directory_keras(images_path, keras_model_path, image_size = (224,224), print_output=True, model_summary=True, show_images=False, grayscale = False, files_to_exclude = [".DS_Store",""]):
    """
    Reads test data from directory resizes it and makes prediction with using a keras model

    # Arguments:
        images_path: source path of the test images see input format
        keras_model_path: path of the keras model 
        img_size (224): size of the images for resizing
        print_output (True): prints output
        model_summary (True): shows keras model summary 
        show_images (False): shows the predicted image
        grayscale (False): converts images to grayscale
        files_to_exclude ([".DS_Store",""]): list of file names to exclude in the image directory (can be hidden files)

    # Returns:
        Prediction results in a list
    
    # Input format:
        images_path = some_dir
        
        /some_dir
            ├──img1.jpg
            ├──img2.jpg
    """

    import warnings
    warnings.filterwarnings("ignore")

    import matplotlib.pyplot as plt
    import numpy as np
    import keras
    import cv2

    # image_size parsing
    if(type(image_size) == tuple):
        if(len(image_size) == 2 and type(image_size[0]) == int and type(image_size[1]) == int):
            img_width = image_size[0]
            img_height = image_size[1]
        else:
            raise ValueError("image_size tuple should have 2 int values")
    elif(type(image_size) == int):
        img_width = image_size
        img_height = image_size
    else:
        raise ValueError("image_size should be an int or a tuple with 2 int values")


    test_images = []
    test_image_names = []

    images = os.listdir(images_path)
    images.sort()

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in images: 
            images.remove(exclude)

    # load model
    model = keras.models.load_model(keras_model_path)

    # get all images
    for image in images:
        abs_path = os.path.join(images_path, image)

        try:
            if(grayscale):
                third_dimension = 1
                img_array = cv2.imread(abs_path, cv2.IMREAD_GRAYSCALE)
            else:
                third_dimension = 3
                img_array = cv2.imread(abs_path)

            new_array = cv2.resize(img_array, (img_width, img_height))
            test_images.append(new_array.reshape(-1, img_width, img_height, third_dimension))    
            test_image_names.append(image)
        except:
            pass
    
    # show model summary
    if(model_summary):
        model.summary()

    predictions = []

    for image, name in zip(test_images,test_image_names):
        prediction = model.predict(image)
        prediction_class = np.argmax(prediction)
        predictions.append(prediction_class)
        if(print_output):
            print("{0} : {1}".format(name,prediction_class))

        if(show_images):
            abs_path = os.path.join(images_path, name)
            img = cv2.imread(abs_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgplot = plt.imshow(img)
            plt.show()

    return predictions


def make_prediction_from_array_keras(test_x, keras_model_path, print_output=True, model_summary=True, show_images=False):
    """
    makes prediction with using a keras model

    # Arguments:
        test_x: numpy array of images
        keras_model_path: path of the keras model
        print_output (True): prints output
        model_summary (True): shows keras model summary 
        show_images (False): shows the predicted image
        grayscale (False): converts images to grayscale
        files_to_exclude ([".DS_Store",""]): list of file names to exclude in the image directory (can be hidden files)

    # Returns:
        Prediction results in a list
    """

    import warnings
    warnings.filterwarnings("ignore")

    import matplotlib.pyplot as plt
    import numpy as np
    import keras
    import cv2

    # load model
    model = keras.models.load_model(keras_model_path)

    # show model summary
    if(model_summary):
        model.summary()

    
    if(type(test_x) == list):
        multi_input_model = True
    else:
        multi_input_model = False

    # add an extra dimension to array since we are iterating over the array the first dimension is disapeares
    if(multi_input_model):
        print("...multi input received reshapeing...")
        new_x = []
        for i in range(test_x[0].shape[0]):
            temp = []
            for test_arr in test_x:
                temp.append(np.expand_dims(test_arr[i], axis=0))
            new_x.append(temp)
        test_x = new_x
    else:
        new_x = []
        for image in test_x:
            new_x.append(np.expand_dims(image, axis=0))
        test_x = new_x

    predictions = []
    for index, image in enumerate(test_x):
        prediction = model.predict(image)
        prediction_class = np.argmax(prediction)
        predictions.append(prediction_class)

        if(print_output):
            print("{0}/{1} -> {2}".format(len(test_x), index, prediction_class))
        else:
            print("{0}/{1}".format(len(test_x),index),end="\r")

        if(show_images):
            try:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                imgplot = plt.imshow(image)
                plt.show()
            except TypeError  as e:
                raise TypeError(e,"""
            input array is not representable as image try with option show_images=False""")

    return predictions



# yolo functions

def create_training_data_yolo(source_path, percent_to_use = 1, validation_split = 0.2, create_cfg_file=True, train_machine_path_sep = "/", shuffle = True, files_to_exclude = [".DS_Store","train.txt","test.txt","obj.names","obj.data","yolo-obj.cfg"]):
    """
    Creates required training files for yolo 

    # Arguments:
        source_path: source path of the images see input format (source folder name of the images will be used to create paths see output format)
        percent_to_use (1): percentage of data that will be used
        validation_split (0.2): splits validation data with given percentage give 0 if you don't want validation split
        create_cfg_file (True): creates a cfg file with default options for yolov3
        auto_label_by_center (False): creates label txt files for all images labels images by their center automatically (use it if all of your datasets images are centered)
        train_machine_path_sep ("/"): if you are going to use a windows machine for training change this  
        shuffle (True): shuffle the paths
        files_to_exclude ([".DS_Store","train.txt","test.txt","obj.names","obj.data","yolo-obj.cfg"]): list of file names to exclude in the image directory (can be hidden files)

    # Save:
        Creates train.txt and test.txt files

    # Input format:
        source_path = some_dir
        
        /some_dir
        ├──/class1
            ├──img1.jpg
            ├──img2.jpg
        ├──/class2
            ├──img3.jpg

    # Output format:
        /some_dir
        train.txt --> data/your_source_folder_name/class1/img1.jpg
        test.txt   
        obj.data
        obj.names                
    """


    # get all file names from main dir and sort the directories
    CATEGORIES = os.listdir(source_path)  
    CATEGORIES.sort()           

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in CATEGORIES: 
            CATEGORIES.remove(exclude)
    
    source_folder = os.path.basename(source_path)

    # change path seperator if needed
    save_path = "data/{0}/".format(source_folder).replace("/",train_machine_path_sep)

    # prepare obj.data
    objdata = []
    objdata.append("classes = {0}".format(len(CATEGORIES)))
    objdata.append("train  = data/{0}/train.txt".format(source_folder).replace("/",train_machine_path_sep))
    objdata.append("valid  = data/{0}/test.txt".format(source_folder).replace("/",train_machine_path_sep))
    objdata.append("names = data/{0}/obj.names".format(source_folder).replace("/",train_machine_path_sep))
    objdata.append("backup = backup")


    total_image_count = 0
    image_names = []
    # loop in the main directory
    for category_index, category in enumerate(CATEGORIES):

        path = os.path.join(source_path, category)
        number_of_categories = len(CATEGORIES)
        index_of_category = CATEGORIES.index(category)
        images = os.listdir(path)

        # exclude possible annotation files
        for image in images:
            if ".txt" in image: 
                images.remove(image)

        # fix possible percentage error
        if(percent_to_use <= 0 or percent_to_use > 1):
            raise ValueError("Percentage should be between 0 and 1")
        elif(int(percent_to_use * len(images)) == 0):
            raise ValueError("Percentage is too small for this set")
        else:
            stop_index = int(len(images)*percent_to_use)


        # loop inside each category folder   itertools for stoping on a percentage
        for image_index, img in enumerate(itertools.islice(images , 0, stop_index)):

            # percent info
            print("File name: {} - {}/{}  Image:{}/{}".format(category, index_of_category+1, number_of_categories, image_index+1, stop_index), end="\r")

            # using save_path's last character (data/obj/ or data\\obj\\) to separete inner paths so if operating system is different inner paths will be matches 
            img_and_path = save_path + category + save_path[-1] + img
            image_names.append(img_and_path)
            
            # count images for dividing validation later
            total_image_count += 1
        
        print("")


    # shuffle and divide train and test sets
    if(shuffle):
        random.shuffle(image_names)
    image_names_train = []
    image_names_test = []
    train_percent = int((validation_split * total_image_count))
    image_names_train += image_names[train_percent:]
    image_names_test += image_names[:train_percent]


    # create files
    __write_to_file(image_names_train, file_name = os.path.join(source_path, "train.txt"), write_mode="w")
    __write_to_file(image_names_test, file_name = os.path.join(source_path, "test.txt"), write_mode="w")

    __write_to_file(CATEGORIES, file_name = os.path.join(source_path, "obj.names"), write_mode="w")
    __write_to_file(objdata, file_name = os.path.join(source_path, "obj.data"), write_mode="w")

    print("\n")

    if(create_cfg_file):
        create_cfg_file_yolo(source_path, number_of_categories, batch=64, sub=16, width=416, height=416)

    print("file saved -> {0}\nfile saved -> {1}\nfile saved -> {2}\nfile saved -> {3}".format("train.txt", "test.txt","obj.names","obj.data"))


def yolo_annotation_tool(images_path, class_names_file, max_windows_size=(1200,700), image_extensions = [".jpg", ".JPG", ".jpeg", ".png", ".PNG"]):
    """
    annotation tool for yolo labeling
    
    # warning it uses two global variables (__coords__, __drawing__) due to the opencvs mouse callback function

    # usage 
    a go backward
    d go forward
    s save selected annotations
    z delete last annotation
    r remove unsaved annotations
    c clear all saved annotations
    """
    import cv2 
    import numpy as np


    # read images
    images = os.listdir(images_path)
    images.sort()

    # remove not included files
    for image in images:
        image_name, image_extension = os.path.splitext(image)
        if image_extension not in image_extensions: 
            images.remove(image)        

    # add paths to images
    images = [os.path.join(images_path, image) for image in images]

    # read class names
    class_names = __read_from_file(class_names_file)
    class_names = class_names.split()


    # -----unused-----
    def __on__trackbar_change(image):
        """
        Callback function for trackbar
        """
        pass
        
    def __resize_with_aspect_ratio(image, width, height, inter=cv2.INTER_AREA):
        """
        resize image while saving aspect ratio
        """
        (h, w) = image.shape[:2]

        if width is None and height is None:
            return image
        if h > w:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        image = cv2.resize(image, dim, interpolation=inter)

        return image
    # ---------------



    def __draw_rectangle_on_mouse_drag(event, x, y, flags, param):
        """
        draws rectangle with mouse events
        """
        global __coords__, __drawing__

        if event == cv2.EVENT_LBUTTONDOWN:
            __coords__ = [(x, y)]
            __drawing__ = True
        
        elif event == 0 and __drawing__:
            __coords__[1:] = [(x, y)]
            im = image.copy()
            cv2.rectangle(im, __coords__[0], __coords__[1], (255, 0, 0), 2)
            cv2.imshow(window_name, im) 

        elif event == cv2.EVENT_LBUTTONUP:
            # __coords__.append((x, y))
            __coords__[1:] = [(x, y)]
            __drawing__ = False
    
            cv2.rectangle(image, __coords__[0], __coords__[1], (255, 0, 0), 2)

            # add points
            points.append(((label),__coords__[0],__coords__[1]))


        elif event == cv2.EVENT_RBUTTONDOWN:
            pass

    def __save_annotations_to_file(image_path, yolo_labels_lists, write_mode):
        """
        saves yolo annnotations lists to annotations file list of lists:[[0,1,1,1,1],[1,0,0,0,0]]
        returns annotation_file_path 
        """

        # prepare the annotations
        yolo_labels = []
        for yolo_labels_list in yolo_labels_lists:
            yolo_labels.append("{0} {1:.6} {2:.6} {3:.6} {4:.6}".format(yolo_labels_list[0], yolo_labels_list[1], yolo_labels_list[2], yolo_labels_list[3], yolo_labels_list[4]))

        image_name, image_extension = os.path.splitext(image_path)
        annotation_file_path = "{0}.txt".format(image_name)

        # if last character of the file is not \n we cant append directly we should add another line 
        # since __write_to_file function writes lists to line inserting an empty string automatically creates a new line
        if(os.path.exists(annotation_file_path)):
            temp_file_content = __read_from_file(annotation_file_path)
            if(temp_file_content):
                if(temp_file_content[-1][-1] != "\n"):
                    yolo_labels.insert(0,"")

        # write prepared annotations to file
        __write_to_file(yolo_labels, annotation_file_path, write_mode=write_mode)

        return annotation_file_path

    def __load_annotations_from_file(image_path):
        """
        loads an images annotations with using that images path returns none if annotation is not exists
        """
        # checking if the annotation file exists if exists read it
        image_name, image_extension = os.path.splitext(image_path)
        annotation_file_path = "{0}.txt".format(image_name)
        if os.path.exists(annotation_file_path):
            annotations = __read_from_file(annotation_file_path)
            annotations = annotations.split("\n")
            annotations = filter(None, annotations)  # delete empty lists 
            annotations = [annotation.split() for annotation in annotations]
            # convert annotations to float and label to int
            # yolo annotation structure: (0 0.8 0.8 0.5 0.5)
            for annotation in annotations:
                annotation[0] = int(annotation[0])
                annotation[1] = float(annotation[1])
                annotation[2] = float(annotation[2])
                annotation[3] = float(annotation[3])
                annotation[4] = float(annotation[4])
            return annotations
        else:
            return None

    def __draw_bounding_boxes_to_image(image_path, class_names):
        """
        draw annotations if file is exists
        """

        # loading annotation file if exists
        annotations = __load_annotations_from_file(image_path)

        if(not annotations):
            return None, 0

        # loading image 
        image = cv2.imread(image_path)
        
        # get dimensions of image
        image_height = np.size(image, 0)
        image_width = np.size(image, 1)

        # convert points
        opencv_points = __convert_annotations_yolo_to_opencv(image_width, image_height, annotations)

        # draw the rectangles using converted points
        for opencv_point in opencv_points:
            # give error if an annoted file has impossible class value
            if(opencv_point[0] > len(class_names)-1):
                raise ValueError("this txt file has an annotation that has bigger class number than current selected class file") 

            cv2.rectangle(image, (opencv_point[1], opencv_point[2]), (opencv_point[3], opencv_point[4]), (0,200,100), 2)
            cv2.line(image, (opencv_point[1], opencv_point[2]), (opencv_point[3], opencv_point[4]), (255, 0, 0), 1) 
            cv2.putText(image, "{0}".format(class_names[opencv_point[0]]), (opencv_point[1], opencv_point[2]), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color=(0, 0, 0), thickness=2)

        return image, len(annotations)

    def __refresh_image(image_index, label):
        """
        if annotation file exists draw the rectangles resize and return the image if not just return the resized image
        also draw information to the image
        """
        image, annoted_object_count = __draw_bounding_boxes_to_image(images[image_index], class_names)
        if(image is None):
            image = cv2.imread(images[image_index])
        # image = __resize_with_aspect_ratio(image, max_windows_size[0], max_windows_size[1])
        image = cv2.resize(image, max_windows_size)

        if(annoted_object_count == 0):
            __save_annotations_to_file(images[image_index], [], "w")
        
        # show some info with puttext
        cv2.putText(image, "{0}/{1} objects:{2} label: {3}".format(len(images), image_index+1, annoted_object_count, class_names[label]), (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color=(0, 200, 100), thickness=2)

        return image 


    

    points = []
    image_index = 0
    label_temp = 0
    global __drawing__
    __drawing__ = False
    window_name = "Yolo annotation tool"


    # create window and set it up
    cv2.namedWindow(window_name)
    cv2.moveWindow(window_name, 40,30)
    cv2.setMouseCallback(window_name, __draw_rectangle_on_mouse_drag,image)
    cv2.createTrackbar('label', window_name, 0, len(class_names)-1, __on__trackbar_change)
    image = __refresh_image(image_index, 0)

    # gui loop
    while(True):

        label = cv2.getTrackbarPos('label', window_name)
        
        # bu ne salak yontem lan kafan mi iyidi yaparken
        if(label != label_temp):
            image = __refresh_image(image_index, label)
            label_temp = label
            points = []

        # dont refresh the original frame while drawing
        if(not __drawing__):
            cv2.imshow(window_name, image)  
        
        key = cv2.waitKey(30)
        


        # save selected annotations to a file
        if(key == ord("s")):
            if(len(points) > 0):

                image_height = np.size(image, 0)
                image_width = np.size(image, 1)

                # convert and save annotations to file
                yolo_labels_lists = __convert_annotations_opencv_to_yolo(image_width,image_height,points)
                __save_annotations_to_file(images[image_index], yolo_labels_lists, "a")

                # reset points and refresh image
                image = __refresh_image(image_index, label)
                points = []

                print("annotation saved {0}".format(yolo_labels_lists))



        # move backward
        if(key == ord("a")):
            if(image_index > 0):
                image_index -= 1
                image = __refresh_image(image_index, label)
                points = []

        # move forward
        if(key == ord("d")):
            if(image_index < len(images)-1):
                image_index += 1
                image = __refresh_image(image_index, label)
                points = []

        # delete last annotation
        if(key == ord("z")):
            # load annotations
            yolo_labels_lists = __load_annotations_from_file(images[image_index])            
            if(yolo_labels_lists):
                # delete last one
                yolo_labels_lists.pop()
                # save new annotations (last one deleted)
                annotation_file_path = __save_annotations_to_file(images[image_index], yolo_labels_lists, "w")
                image =__refresh_image(image_index, label)
                points = []

                # # if file is empty delete it
                # if(len(yolo_labels_lists) == 0):
                #     os.remove(annotation_file_path)

        # refresh current image
        if(key == ord("r")):
            image =__refresh_image(image_index, label)
            points = []

        # clear annotations
        if(key == ord("c")):
            __save_annotations_to_file(images[image_index], [], "w")
            image = __refresh_image(image_index, label)        
            points = []


        # if window is closed break this has to be after waitkey
        if (cv2.getWindowProperty(window_name, 0) < 0):
            # cv2.destroyAllWindows()
            break

        # quit on esc
        if(key == 27):
            break


    cv2.destroyAllWindows()



def create_cfg_file_yolo(save_path, classes, batch=64, sub=16, width=416, height=416):
    """
    creates config file with default options for yolo3


    # config file structure
    # 0 batch 64
    # 1 sub 8
    # 2 width 416
    # 3 height 416
    # 4 max_batches classes*2000 but no less than 4000
    # 5 steps %80 max_batches
    # 6 steps %90 max_batches
    # 7 classes
    # 8 filters before yolo layers (classes+5)*3
    """
    
    if(classes < 1):
        raise ValueError("class count can't be smaller than 1") 

    if(width%32 != 0 or height%32 != 0):
        raise ValueError("height and width must be divisible by 32") 

    # get template
    yolo_cfg_template = __get_cfg_template("yolo_cfg_template")

    # set up parameters
    if(classes == 1):
        max_batches = 4000
    else:
        max_batches = classes * 2000

    steps1 = int((max_batches * 80) /100)
    steps2 = int((max_batches * 90) /100)

    filters = (classes+5)*3

    yolo_cfg_template = yolo_cfg_template.format(batch,sub,width,height,max_batches,steps1,steps2,classes,filters)

    # save cfg to save path
    __write_to_file([yolo_cfg_template], os.path.join(save_path, "yolo-obj.cfg"), write_mode="w")

    print("file saved -> {0}".format("yolo-obj.cfg"))


def make_prediction_from_directory_yolo(images_path, darknet_path, save_path = "detection_results", darknet_command = "./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights {0} -i 0 -thresh 0.2 -dont_show", files_to_exclude = [".DS_Store",""]):
    """
    makes prediction for multiple images from directory
    it uses shell command to execute darknet
    """

    save_path = os.path.join(darknet_path, save_path)

    # make the dir
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    images = os.listdir(images_path)
    images.sort()

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in images: 
            images.remove(exclude)

    image_count = len(images)
    for index, image in enumerate(images):
        abs_path = os.path.join(images_path, image)
        __run_shell_command("cd {0} && {1}".format(darknet_path,darknet_command.format(abs_path)))
        copyfile(os.path.join(darknet_path, "predictions.jpg"), os.path.join(save_path, "predictions{0}.jpg".format(index)))
        
        print("File name: {0} - {1}/{2}".format(image, index+1, image_count), end="\r")

    print("\nAll images saved to {0}".format(save_path))


def draw_bounding_boxes(images_path_file, class_names_file, save_path = "annoted_images"):
    """
    Draws bounding boxes of images

    # input
    images_path_file: a file that consists of image paths
    class_names_file: class names for bounding boxes
    save_path:("annoted_images") save path of the new images
    """
    import cv2
    import numpy as np

    image_paths = __read_from_file(images_path_file)
    image_paths = image_paths.split()
    
    class_names = __read_from_file(class_names_file)
    class_names = class_names.split()
    
    # make the dir
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for image_path in image_paths:

        image = cv2.imread(image_path)

        # set up save loaction and get annotation file
        image_name, image_extension = os.path.splitext(image_path)
        new_file_name = "{0}(objects){1}".format(image_name, image_extension)
        new_file_save_path = os.path.join(save_path, os.path.basename(new_file_name))
        annotation_file_path = "{0}.txt".format(image_name)

        # parse annotation file
        
        if os.path.exists(annotation_file_path):
            annotations = __read_from_file(annotation_file_path)
            annotations = annotations.split("\n")
            annotations = filter(None, annotations)  # delete empty lists 
            annotations = [annotation.split() for annotation in annotations]
            # convert annotations to float and label to int
            # yolo annotation structure: (0 0.8 0.8 0.5 0.5)
            for annotation in annotations:
                annotation[0] = int(annotation[0])
                annotation[1] = float(annotation[1])
                annotation[2] = float(annotation[2])
                annotation[3] = float(annotation[3])
                annotation[4] = float(annotation[4])
        else:
            continue
            
         # get dimensions of image
        image_height = np.size(image, 0)
        image_width = np.size(image, 1)

        # convert points
        opencv_points = __convert_annotations_yolo_to_opencv(image_width, image_height, annotations)

        # draw the rectangles using converted points
        for opencv_point in opencv_points:
            # give error if an annoted file has impossible class value
            if(opencv_point[0] > len(class_names)-1):
                raise ValueError("this image file has an annotation that has bigger class number than current selected class file") 

            cv2.rectangle(image, (opencv_point[1], opencv_point[2]), (opencv_point[3], opencv_point[4]), (0,200,100), 2)
            cv2.line(image, (opencv_point[1], opencv_point[2]), (opencv_point[3], opencv_point[4]), (255, 0, 0), 1) 
            cv2.putText(image, "{0}".format(class_names[opencv_point[0]]), (opencv_point[1], opencv_point[2]), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color=(0, 0, 0), thickness=2)
            
        
        cv2.imwrite(new_file_save_path, image)
        
        print("Image saved: {0}".format(new_file_save_path))


def auto_annotation_by_random_points(images_path, class_of_images, annotation_points=(0.4,0.6,0.8,0.9), files_to_exclude = [".DS_Store"]):
    """
    # auto creates random annotations for all images it needs 4 values (smallest_center, biggest_center, smallest_dimension, biggest_dimension) ex:(0.4,0.6,0.8,0.9)
    # values should be between 0 and 1 
    """

    images = os.listdir(images_path)

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in images: 
            images.remove(exclude)
    
    # exclude possible annotation files
    for image in images:
        if ".txt" in image: 
            images.remove(image)

    # loop inside each category folder   itertools for stoping on a percentage
    for image_index, img in enumerate(images):

        # percent info
        print("Image:{}/{}".format(image_index+1, len(images)), end="\r")

        # annote images
        if(len(annotation_points) != 4):
            raise ValueError("4 values needed for random annotations '{0}' is given".format(len(annotation_points)))
        for label in annotation_points:
            if(label < 0 or label > 1):
                raise ValueError("labels has to be between 0 and 1 '{0}' is given".format(label))

        c1 = random.uniform(annotation_points[0], annotation_points[1])
        c2 = random.uniform(annotation_points[0], annotation_points[1])
        
        w = random.uniform(annotation_points[2], annotation_points[3])
        h = random.uniform(annotation_points[2], annotation_points[3])
        
        yolo_labels = "{0} {1} {2} {3} {4}".format(class_of_images, c1,c2, w, h)
        
        basename, extension = os.path.splitext(img)
        txtname = basename + ".txt"
        abs_save_path = os.path.join(images_path, txtname)

        __write_to_file([yolo_labels], file_name = abs_save_path, write_mode="w")



# other utilities

def train_test_split(train_x, train_y, test_size=0.2, save_path=None):
    """
    Splits train and test sets from numpy array

    # Arguments:
        train_x: taining data
        train_y: labels of the training data
        test_size (0.2): size of the test set to split
        save_path (None): save path for for seperated data

    # Returns 
        splitted train and test data
        train_x, train_y, test_x, test_y
    """

    new_train_x = []
    new_train_y = []
    
    test_x = []
    test_y = []

    if(len(train_x) != len(train_y)):
        raise ValueError("x and y sizes does not match")
    
    data_count = len(train_x)
    train_percent = int((data_count * test_size))

    new_train_x = train_x[train_percent:]
    new_train_y = train_y[train_percent:]
    
    test_x = train_x[:train_percent]
    test_y = train_y[:train_percent]

    print("\ntest x: {0} test y: {1}".format(len(test_x),len(test_x)))
    print("train x: {0} train y: {1}".format(len(new_train_x),len(new_train_y)))

    # save
    if(save_path != None):
        with open(save_path + "_x_train.pkl", "wb") as file:
            pickle.dump(new_train_x, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("\nfile saved -> {0}{1}".format(save_path,"_x_train.pkl"))

        with open(save_path + "_y_train.pkl", "wb") as file:
            pickle.dump(new_train_y, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}".format(save_path,"_y_train.pkl"))
        
        with open(save_path + "_x_test.pkl", "wb") as file:
            pickle.dump(test_x, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}".format(save_path,"_x_test.pkl"))

        with open(save_path + "_y_test.pkl", "wb") as file:
            pickle.dump(test_y, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("file saved -> {0}{1}\n".format(save_path,"_y_test.pkl"))
        
    return new_train_x, new_train_y, test_x, test_y


def create_confusion_matrix(predictions, actual_values, class_names=None, one_hot=False, normalize=False):
    """ 
    Creates a confusion matrix

    # Arguments:
        predictions: list of predicted numerical class labels of each sample ex:[1,2,5,3,1]
        actual_values: list of actual numerical class labels of each sample ex:[1,2,5,3,1] or onehot encoded [[0,0,1],[1,0,0],[0,1,0]]
        class_names (None): names of classes that will be drawn, if you want only the array and not the plot pass None (matplotlib required)
        one_hot (False): if labels are one hot formatted use this
        normalize (False): normalizes the values of the matrix

    # Retruns:
        A numpy array of confusion matrix 
    """
    from sklearn.metrics import confusion_matrix
    import numpy as np

    # decode one hot
    if(one_hot):
        labels = []
        for one_hot_value in actual_values:
            for index,value in enumerate(one_hot_value):
                if(value == 1):
                    labels.append(index)
        actual_values = labels

    # create confusion matrix
    cnf_matrix = confusion_matrix(actual_values, predictions)

    if(normalize):
        cnf_matrix = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Not Normalized confusion matrix')
    
    print("xlabel: True label\nylabel: predicted label")
    print(cnf_matrix)

    # plot the matrix
    if(class_names):
        import matplotlib.pyplot as plt

        title='Confusion matrix'
        cmap=plt.cm.Blues

        plt.imshow(cnf_matrix, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(class_names))
        plt.xticks(tick_marks, class_names, rotation=45)
        plt.yticks(tick_marks, class_names)

        
        thresh = cnf_matrix.max() / 2.
        for i, j in itertools.product(range(cnf_matrix.shape[0]), range(cnf_matrix.shape[1])):
            plt.text(j, i, cnf_matrix[i, j],horizontalalignment="center",color="white" if cnf_matrix[i, j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()

    return cnf_matrix











# deprecated
def __create_training_data_yolo(source_path, save_path = "data/obj/", percent_to_use = 1, validation_split = 0.2, rename_duplicates = False, shuffle = True, files_to_exclude = [".DS_Store","data","train.txt","test.txt","obj.names","obj.data"]):
    """
    Creates train ready data for yolo, labels all the images by center automatically
    (This is not the optimal way of labeling but if you need a lot of data fast this is an option)

    # Arguments:
        source_path: source path of the images see input format
        save_path (data/obj/): this path will be added at the begining of every image name in the train.txt and test.txt files
        percent_to_use (1): percentage of data that will be used
        validation_split (0.2): splits validation data with given percentage give 0 if you don't want validation split
        rename_duplicates (False): renames duplicates while copying images but it slows down the process if you don't have any duplicates in your set don't use it
        shuffle (True): shuffle the paths
        files_to_exclude ([".DS_Store","data,"train.txt","test.txt","obj.names","obj.data"]): list of file names to exclude in the image directory (can be hidden files)

    # Save:
        Copies all images in to save_path directory and creates txt files for each image see output format

    # Input format:
        (if there are duplicates you can use rename duplicates)
        source_path = some_dir
        
        /some_dir
        ├──/class1
            ├──img1.jpg
            ├──img2.jpg
            ├──img3.jpg
        ├──/class2
            ├──img3.jpg

    # Output format:
        (if rename duplicates is on it renames images)
        source_path = some_dir
        save_path = "data/obj/"
        
        /some_dir
        train.txt
        test.txt
        ├──data/obj/
            ├──img1.jpg
            ├──img1.txt
            ├──img2.jpg
            ├──img2.txt
            ├──img3.jpg
            ├──img3.txt
            ├──img3(1).jpg
            ├──img3(1).txt                  
    """

    image_names = [] 
    
    CATEGORIES = os.listdir(source_path)  # get all file names from main dir
    CATEGORIES.sort()                     # sort the directories

    # remove excluded files
    for exclude in files_to_exclude:
        if exclude in CATEGORIES: 
            CATEGORIES.remove(exclude)
    
    # make the dir
    if not os.path.exists(os.path.join(source_path, save_path)):
        os.makedirs(os.path.join(source_path, save_path))
    
    total_image_count = 0

    # loop in the main directory
    for category_index, category in enumerate(CATEGORIES):


        path = os.path.join(source_path, category)
        number_of_categories = len(CATEGORIES)
        index_of_category = CATEGORIES.index(category)
        images = os.listdir(path)

        # fix possible percentage error
        if(percent_to_use <= 0 or percent_to_use > 1):
            print("Enter a possible percentage between 0 and 1")
            return
        elif(int(percent_to_use * len(images)) == 0):
            print("Percentage is too small for this set")
            return
        else:
            stop_index = int(len(images)*percent_to_use)

              

        # loop inside each category folder   itertools for stoping on a percentage
        for image_index, img in enumerate(itertools.islice(images , 0, stop_index)):

            # percent info
            print("File name: {} - {}/{}  Image:{}/{}".format(category, index_of_category+1, number_of_categories, image_index+1, stop_index), end="\r")

        
            # yolo label format
            # <object-class> <x_center> <y_center> <width> <height>
            # class 0.5 0.5 1 1 

            yolo_labels = "{0} {1} {2} {3} {4}".format(category_index, 0.5, 0.5, 1, 1)
            
            absolute_save_path = os.path.join(source_path, save_path)
            img_and_path = save_path + img

            # if rename duplicates enabled name can be changed but original name is needed to copy the file 
            img_new_name = img

            # rename duplicates if enabled
            if(rename_duplicates):
                duplicate_number = 1
                while(True):
                    if(img_and_path in image_names):

                        # reset the image name tor prevet something like this img(1)(2).jpg
                        img_and_path = save_path + img 

                        # change the image name in the train or test file
                        basename, extension = os.path.splitext(img_and_path)
                        img_and_path = "{0}{1}{2}{3}{4}".format(basename, "(", duplicate_number, ")", extension)
                        
                        # change real image name
                        basename, extension = os.path.splitext(img)
                        img_new_name = "{0}{1}{2}{3}{4}".format(basename, "(", duplicate_number, ")", extension)
                        duplicate_number += 1
                    else:
                        break
            

            basename, _ = os.path.splitext(img_new_name)
            text_name = basename + ".txt"
            path_for_txt_file = os.path.join(absolute_save_path, text_name)
 
            __write_to_file([yolo_labels], path_for_txt_file, write_mode="w")


            # copy_files_to_new_path
            new_path_img = os.path.join(absolute_save_path, img_new_name)            
            copyfile(os.path.join(path, img), new_path_img)

            image_names.append(img_and_path)

            # count images for dividing validation later
            total_image_count += 1
        
        print("")

    # shuffle and divide train and test sets
    if(shuffle):
        random.shuffle(image_names)
    image_names_train = []
    image_names_test = []

    train_percent = int((validation_split * total_image_count))
    image_names_train += image_names[train_percent:]
    image_names_test += image_names[:train_percent]

    # prepare obj.data
    objdata = []
    objdata.append("classes = {0}".format(len(CATEGORIES)))
    objdata.append("train  = data/train.txt")
    objdata.append("valid  = data/test.txt")
    objdata.append("names = data/obj.names")
    objdata.append("backup = backup")

    # save to file
    __write_to_file(image_names_train, file_name = os.path.join(source_path, "train.txt"), write_mode="w")
    __write_to_file(image_names_test, file_name = os.path.join(source_path, "test.txt"), write_mode="w")

    __write_to_file(CATEGORIES, file_name = os.path.join(source_path, "obj.names"), write_mode="w")
    __write_to_file(objdata, file_name = os.path.join(source_path, "obj.data"), write_mode="w")

    print("\nfile saved -> {0}\nfile saved -> {1}\nfile saved -> {2}\nfile saved -> {3}".format("train.txt", "test.txt","obj.names","obj.data"))






