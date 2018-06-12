import cv2
from PIL import Image
import matplotlib.pyplot as plt

_inp_file = 'mod_output_info.txt'
_max_runs = 10


def get_seans_data():
    
    print 'Reading ' + _inp_file
    data = []
    with open( _inp_file, 'r' ) as f:
        for row in f:
            data.append( row.split(',') )
            
    print 'Done'
    return data


def read_pass_data( inp_data ):

    ret_list = []
    
    tup_list = []

    print len(inp_data)
    
    for i in range( 0, _max_runs ):#len(inp_data) ):
    
        # Get the image
        img = Image.open( inp_data[i][0] )

        # Get the tuple
        tup = inp_data[i][1][1:].strip('(').strip(')')
        tup = tup.split(' ')
        tup_list.append( ( int(tup[0]), int(tup[1]), int(tup[2]), int(tup[3]) ) )
    
        ret_list.append( (img.copy(),tup_list[-1],'lego') )

    return ret_list