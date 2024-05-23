# CSC126_FINALS_GROUPTEMP

#CSC 126 Graphics and Visual Computing Final Project  
Group name: TEMPNAME  
Grop members:  
  - Veverly Ewan  
  - Jelyn Gamboa  
  - Lendel Cosep  


# Requirements:  
  - Python 3+
  - OpenCV
  - Numpy
  - Haar Cascade Frontal face classifiers

# Approach:
 1. Using LBPH (Local Binary Patterns Histograms)Algorithm in detecting daces. Labeling the pixels of an image by thresholding the neighborhood of each pixel treating the resutl as a binary number.
 2. LBPH uses 4 parameters:
    - Radius: used to build the circular local binary pattern and represents the radius around the central pixel.
    - Neighbors: number of sample points in order to build the circular local binary pattern.
    - Grid X and Y: Grid X are the number of cells in the horizontal direction, while Grid Y are the number of cells in the vertical direction.
  3. Training process:
     - The model requires a sufficient number of labeld images for training. The images are converted to grayscale to simplify proccessing while reducing computational overhead.
     - The region of interset (ROI), the face, is extracted from each images. The process involes detecting the face in the image and cropping them to focus only on the relevant area. This serves as the input data for training the model.
    
Overall, LBPH offers flexibility and effective approach for face detection, with the parameters allowing fine-tuning to balance computational efficiency and accuracy.
