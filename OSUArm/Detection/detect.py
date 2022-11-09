from skimage import measure as m
from skimage.io import imread
import pandas as pd
import numpy as np





#Code requirements:
# Input - Picture of Workspace and relevant Workpace dimensions
# Output - Bounding boxes, centroids loactions of all objects


class Workspace:
    def __init__(self, grid_coords, bin_coords, image):
        self.grid_coords = grid_coords
        self.bin_coords = bin_coords
        self.image = imread(image)
        self.obj = pd.DataFrame()
        
    def filter_img(self):
        ## Insert Filtering logic here
        ## It is not YET known how the image need to be filtered in a real world application
        
        
        
    def detect_objects(self):
        im = self.image
        label_im = m.label(im)
        properties = m.regionprops(label_im)
        self.obj.insert(0, 'bbox', properties['bbox'])
        self.obj.insert(1, 'centroid', properties['centroid'])
        self.obj.insert(2, 'orientation', properties['orientation'])
        
        
        
        
        
        
if __name__ == '__main__':
    current = Workspace([1,2],[3,4],r'')
    current.obj
        
