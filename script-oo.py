import glob
import re
import os

"""


Script to Filter out junk data from
CSV google analytic files


"""

'''

TODO: Extract PDFS

'''


class GoogleAnalyticsParser:
    def __init__(self, outputfile, csvfiles):
        self.outputfile = outputfile
        self.csvfiles = csvfiles

    def parse(self):

        discard = []
        allow = []

        regexes = [

            re.compile("search:showresults&searchInput"),
            re.compile("previewid"),
            re.compile("/companyinformation/newsarchive/"),
            re.compile("/companyinformation/employeedirectory/"),
            re.compile("/eventsdevelopment/calendar/"),
            re.compile("/eventsdevelopment/reminders/"),
            re.compile("login&returnURL"),
            re.compile("/workplaceresources/conferences/"),
            re.compile("/workplaceresources/conferences/booking/admin/index.cfm?event=confroomsadmin:showrequestconfirmed&approved"),
            re.compile("/workplaceresources/printservices/"),
            re.compile("/mydepartment/applications/"),
            re.compile("/login/"),
            re.compile("searchInput")

        ]

        directory = glob.glob(self.csvfiles)

        for csvfile in directory:
            with open(csvfile) as inputcsv:
                for line in inputcsv:
                    commadelimited = line.split(',')

                    if any(regex.search(commadelimited[0]) for regex in regexes):
                        discard.append(line)
                    else:
                        allow.append(line)
        return allow

    def grabpdfs(self):

        """
        Get all instances of PDFS in the file
        :return: allow
        """

        discard = []
        allow = []

        regexes = [

            re.compile("/downloads/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.pdf")
        ]

        directory = glob.glob(self.csvfiles)

        for csvfile in directory:
            with open(csvfile) as inputcsv:
                for line in inputcsv:
                    commadelimited = line.split(',')

                    if any(regex.search(commadelimited[0]) for regex in regexes):
                        allow.append(line)
                    else:
                        discard.append(line)
        return allow

    def csvwriter(self):

        csvlist = parser.parse()

        file = open(self.outputfile, 'w')

        for entry in csvlist:
            file.write(entry)

        file.close()

parser = GoogleAnalyticsParser("C:/Users/jasingh/Documents/data ops/data-output.csv", "C:/Users/jasingh/Documents/CSVs/*.csv")
parser.csvwriter()

