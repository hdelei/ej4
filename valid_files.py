class Validate:

    def __init__(self):
        self.text_file = ''
        self.name_list = []
    
    def generate_txt(self, name_list):
        self.text_file = open('filtered_list.txt', 'w')
        for name in name_list:
            self.text_file.write(name + '\n')
        self.text_file.close()