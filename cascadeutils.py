import os
def generate_negative_description_file():
    #open the poutput file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        #loop over the filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')
            print('negative/' + filename + '\n')