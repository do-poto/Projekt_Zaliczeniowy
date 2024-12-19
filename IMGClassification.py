import mediapipe
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision.image_classifier import ImageClassifierResult

#initialized global variables
Classified_Image : mediapipe.Image
Results_Output_String = "Top 3 predictions are: "

#image input
def Get_User_Image():
    global Classified_Image
    try:
        #get image from the user
        User_Input_Image = str(input("Write image name or the localsation of the image with its type: "))
        #input image into appropriate mediapipe format
        Classified_Image = mediapipe.Image.create_from_file(User_Input_Image)
        return Classified_Image
    except Exception as e:
        #print exception in case of an error
        print("An error occured while creating an image: " + str(e))
        Get_User_Image()
    return Classified_Image

#image classifier set up
def Classification_Function(Classified_Image):
    #trained model file path
    Model_Asset_Path = "efficientnet_lite0.tflite"

    #imported computer vision settings objects
    Image_Classifier = mediapipe.tasks.vision.ImageClassifier
    Base_Options = mediapipe.tasks.BaseOptions
    Vision_Running_Mode = mediapipe.tasks.vision.RunningMode

    #image classifier options object
    Image_Classifier_Options = mediapipe.tasks.vision.ImageClassifierOptions

    #computer vision options set up
    Current_Options = Image_Classifier_Options(base_options=Base_Options(model_asset_path=Model_Asset_Path),
                                       max_results=5,
                                       running_mode=Vision_Running_Mode.IMAGE)

    #creation of image classifier object using chosen settings
    with Image_Classifier.create_from_options(Current_Options) as Classifier:
        Classification_Results = Classifier.classify(Classified_Image)
    return Classification_Results

#present results
def Results_Presenter(Classification_Results):
    global Results_Output_String
    Flag_One = 0
    #final output line
    while Flag_One < 3:
        #str output creator
        Results_Output_String = Results_Output_String + "\n" \
                                + "Object name: " + Classification_Results.classifications[0].categories[Flag_One].category_name + "\n"  \
                                + "Probability of being this object: " \
                                + str(round(Classification_Results.classifications[0].categories[Flag_One].score * 100, 2)) + "%" + "\n"
        Flag_One += 1

    return Results_Output_String

def Run_IMG_Classification():
    print(Results_Presenter(Classification_Function(Get_User_Image())))