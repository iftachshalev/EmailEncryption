import pickle
import os


class UpdateFile:

    def save_list(self, file):
        filename = 'pass_file.bin'
        outfile = open(filename, 'wb')
        pickle.dump(file, outfile)
        outfile.close()

    def open_list(self):
        filename = 'pass_file.bin'
        if os.path.isfile(filename):
            infile = open(filename, 'rb')
            all_pass = pickle.load(infile)
            infile.close()
            return all_pass
        all_pass = []
        return all_pass


