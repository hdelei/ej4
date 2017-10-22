import txt
import valid_files
from datetime import datetime

start_time = datetime.now()

newtxt = txt.Txt()
filenames = newtxt.get_all_filenames()
for file in filenames:    
    print(newtxt.get_path() + '\\' + file)

stop_time = datetime.now()
elapsed_time = stop_time - start_time

print('\nElapsed time for {} files: {}'.format(newtxt.all_files_count, elapsed_time))
print('Files taken {} \nDiscarded files {}.'.format( len(filenames), newtxt.all_files_count - len(filenames) ))

text_file = valid_files.Validate()

text_file.generate_txt(filenames)