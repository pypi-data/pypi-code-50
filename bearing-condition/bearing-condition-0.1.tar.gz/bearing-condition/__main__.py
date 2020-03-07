from BearingClassifier import *

if __name__ == "__main__":
    bearing_classifier = BearingClassifier(ModelTraining.DE)
    bearing_classifier.load_wav()
    predominant_class, confidence_percentage = bearing_classifier.predict_wav()
    print(f"Predominant class: {predominant_class} \n"
          f"Confidence percentage: {confidence_percentage}")
