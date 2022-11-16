from skimage import measure as m
from skimage.io import imread,imshow
import pandas as pd
import numpy as np
from skimage import feature,color,morphology
from skimage.exposure import histogram
import greedypacker


class bin:
    
    def __init__(self, workspace, packer):
        self.workspace = workspace
        self.packer = packer
        self.workspace.detect_objects()
    
    def pack(self):
        
        dim = np.zeros(len(self.workspace.obj['area']))
        for x in self.workspace.obj.iterrows():
            if x[1]['area'] < 4000:
                dim[x[0]] = 1.5
            elif 6500 > x[1]['area'] > 4000:
                dim[x[0]] = 2.0
            elif x[1]['area'] > 6500:
                dim[x[0]] = 2.5
        self.workspace.obj['dim'] = dim
        
        for x in self.workspace.obj['dim']:
            self.packer.add_items(greedypacker.Item(x,x))
        
        self.packer.execute()
            
        
        