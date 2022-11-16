from skimage import measure as m
from skimage.io import imread,imshow
import pandas as pd
import numpy as np
from skimage import feature,color,morphology
from skimage.exposure import histogram





#Code requirements:
# Input - Picture of Workspace and relevant Workpace dimensions
# Output - Bounding boxes, centroids, orientation, loactions of all objects


class Workspace:
    def __init__(self, grid_coords, bin_coords, image):
        self.grid_coords = grid_coords
        self.bin_coords = bin_coords
        self.image = imread(image, as_gray=True)
        self.obj = None
        
    #def filter_img(self):
        ## Insert Filtering logic here
        ## It is not YET known how the image need to be filtered in a real world application
        
        
    def detect_objects(self):
        im = self.image
        imbw = morphology.remove_small_objects(im<.4, min_size = 2500)
        label_im = m.label(imbw)
        properties = m.regionprops_table(label_im, properties=('bbox','centroid','orientation','area'))
        self.obj = pd.DataFrame(properties)
        self.imbw = imbw
        
        
        

