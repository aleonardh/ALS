import dateutil.parser as parser
import datetime
class Ej02:

    def __init__(self, text):
        self.text = text

    def parse_text(self):
        toret = ""
        lines_separated_in_lists = str(self.text).split('\n')
        companies = str(lines_separated_in_lists[0])
        lines = lines_separated_in_lists[1:]
        companies_list = companies.split(',')
        for x in range(len(companies_list)):
            if x % 2 == 0:
                line = lines[int(companies_list[x+1].lstrip())-1].split(',')
                toret += "%d. %s, in the week starting at: %s sold on monday: %s, tuesday: %s, wednesday %s, thursday %s, friday %s, saturday %s, sunday %s. \n" %(int(companies_list[x+1].lstrip()),companies_list[x].lstrip(), line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
        return toret



t = Ej02("Microsoft, 1, Apple, 2, Google, 3, Yahoo, 4 \n1, 2015-01-09, 120, 34, 256, 78, 93, 222, 5 \n 2, 2015-01-09, 900, 346, 730, 456, 33, 345, 234 \n3, 2015-01-09, 934, 922, 866, 444, 235, 999, 789 \n4, 2015-01-09, 45, 56, 78, 23, 44, 90, 9")
print(t.parse_text())




