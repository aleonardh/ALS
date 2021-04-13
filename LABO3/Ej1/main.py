import dateutil.parser as parser
import datetime
class Ej01:
    def __init__(self, date):
        self.date = date

    def convert_to_ISO8301(self):
        try:
            date_text = str(self.date)
            date = (parser.parse(date_text))
            date_iso_format = date.isoformat()
            if date_iso_format.find("+", 10) == -1 and date_iso_format.find("-", 10) == -1:
                date_iso_format += "+00:00"
            return date_iso_format
        except:
            print("Error")

f = Ej01("2016-05-22")
f2 = Ej01("12 Feb 2014")
print(f.convert_to_ISO8301())
print(f2.convert_to_ISO8301())
