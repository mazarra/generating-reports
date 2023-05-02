import os
import datetime


class Generating_reports:
    def __init__(self, path:str):
        self.ph = path
        self.current_date = datetime.date.today()
        self.current_time = datetime.datetime.now()

    def gen_report(self, text_to_write):
        if not os.path.exists(self.ph+str(self.current_date)):
            file_reports = open(self.ph + str(self.current_date), "w+")
            file_reports.write(str(self.current_time) + ": " + text_to_write)
        else:
            file_reports = open(self.ph + str(self.current_date), "a+")
            file_reports.write("\n"+ str(self.current_time) + ": " + text_to_write)
        file_reports.close()