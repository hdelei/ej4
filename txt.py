import os
import re
from langdetect import detect

class Txt:   
    
    def __init__(self):
        #self.path = os.getcwd() + '\\amostra'
        self.path = os.getcwd() + '\\sentencas'
        self.filename = ''
        self.all_filenames = []
        self.all_files_count = 0
    
    def get_path(self):
        return self.path

    def is_valid(self, file):
        text_sample = ''
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        #file_full_path = os.path.join(file_dir, 'amostra/' + file)   
        file_full_path = os.path.join(file_dir, 'sentencas/' + file)   
       
        for i, line in enumerate(open(file_full_path)):            
            if i < 20 and i > 4:
                text_sample += line.strip()
        try:
            #print(detect(text_sample), file)      
            if detect(text_sample) == 'pt':
                return True
        except:
            pass    
        return False

    def get_all_filenames(self):                 
        for file in os.listdir(self.path):
            #print(os.path.getsize(self.path +'\\' + file))
            if self.discard_by_size(file) and self.is_valid(file):
                self.all_filenames.append(file)
            self.all_files_count += 1         
        return self.all_filenames

    def discard_by_size(self, file):
        size = os.path.getsize(self.path +'\\' + file)
        if size > 1500 or size < 500000:
            return True
        else:
            return False



    

        



