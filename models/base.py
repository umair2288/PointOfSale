

class BaseModel():

    def save_to_file(self, file_path):
        f = open(file_path, "a")
        txt = self.format_to_save(sep=",")
        f.write(txt)
        f.close()
