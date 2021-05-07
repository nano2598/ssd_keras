## AE4317 Individual Assignment - Mariano Ramirez

This repository is a fork of the repository at https://github.com/pierluigiferrari/ssd_keras "SSD: Single-Shot MultiBox Detector implementation in Keras" by Pierluigi Ferrari, since the project was heavily based on that code. Note that his repository also includes a very extensive README which might help to clarify some parts about the code and implementation. 

## Dependencies
The most important dependencies are Keras (only version 2.2.3 tested, known that others might have issues) and tensorflow (only version 1.15.5 tested, known that others might have issues.) For the rest of the dependencies such as numpy, openCV, scipy, matplotlib, and others in general the version is not important. 

## Training

To replicate the training, the ssd7_training.ipynb jupyter notebook can be used. If you prefer not to use a jupyter notebook, the essentially equivalent code is also included in main.py. Both of these files already have all the parameters and setting to replicate the training of my final chosen model. At the end of the code some example detections are also shown.  

## Loading the saved model

Note that training can take a relatively long time, thus it might be more convenient to simply load the saved ssd7_final.h5 model that is also in this repository. This can again be done with the same jupyter notebook mentioned above, but it can also be done with testing.py. 

## Evaluating

Similarly, to get some quick evaluation results, the ssd300_evaluation.ipynb file can be used. Again there is an alternative python file, evaluation.py. Both these files again have all the needed parameters set. 
