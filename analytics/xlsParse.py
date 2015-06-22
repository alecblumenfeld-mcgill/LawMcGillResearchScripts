
import itertools
import operator
import collections
import sys
from metrics import *
__author__ = 'Alec'
from xlrd import open_workbook


class author:
    def __init__(self, name):
        self.name = name;
        self.entries = []
class year:
    def __init__(self, year):
        self.year = year;
        self.entries = []
class lang:
    def __init__(self, lang):
        self.lang = lang;
        self.entries = []
class region:
    def __init__(self, region):
        self.lang = region;
        self.entries = []
class journalType:
    def __init__(self, type):
        self.lang = type;
        self.entries = []
class outletLang:
    def __init__(self, outletLang):
        self.lang = outletLang;
        self.entries = []

class topic:
    def __init__(self, topic):
        self.topic = topic;
        self.entries = []
class entry:
    def __init__(self, publication, author, year, lang, publicationType, coAuthor, coAuthorRelation, outlet, outletType,
                 outletReg, outletLang, journalType, lawType, publicationField, keyword, citations,row):

        self.publication = str(publication).replace('“', '').replace('”', '').strip()
        self.author = str(author)
        self.year = str(year).split(".")[0]
        self.lang = lang
        self.publicationType = publicationType
        if(coAuthor=="Y"):
            self.coAuthor = True
        else:
            self.coAuthor= False
        self.coAuthorRelation = coAuthorRelation
        self.outlet = outlet
        self.outletType = outletType
        self.outletReg = outletReg
        self.outletLang = outletLang
        self.journalType = journalType
        self.lawType = lawType
        self.topic = "{"+publicationField+"}"
        self.keyword = keyword.split(',')
        try:
            self.citations = int(citations)
        except:
            self.citations = 0
        self.row=row


def getEntries():
    entries = []
    workbook = open_workbook('RO Analytics data FINAL without citations.xlsx')
    for s in workbook.sheets():
        for row in range(1, s.nrows):

            try:
                if(s.cell(row, 0)!=''):
                    entries.append(entry(s.cell(row, 0).value, s.cell(row, 1).value, s.cell(row, 2).value, s.cell(row, 3).value,
                                     s.cell(row, 4).value, s.cell(row, 5).value, s.cell(row, 6).value, s.cell(row, 7).value,
                                     s.cell(row, 8).value, s.cell(row, 9).value, s.cell(row, 10).value,
                                     s.cell(row, 11).value, s.cell(row, 12).value, s.cell(row, 13).value,
                                     s.cell(row, 14).value, s.cell(row, 15).value,row))
            except IndexError:
                return entries
    return entries

#returns the authors in entries as a dictonary with authors as keys
def getAuthors(entries):
    authors = {}
    for x in entries:

        try:
            authors[x.author].entries.append(x)

            pass
        except :
            authors[x.author] = author(x.author)
            authors[x.author].entries.append(x)

            pass
    return authors

#returns the years in entries as a dictonary with years as keys
def getYears(entries):

    years = {}
    for x in entries:

        try:
            years[x.year].entries.append(x)

            pass
        except :
            years[x.year] = year(x.year)
            years[x.year].entries.append(x)
            pass
    return collections.OrderedDict(sorted(years.items()))

#returns langs
def getLangs(entries):

    langs = {}
    for x in entries:

        try:
            langs[x.lang].entries.append(x)

            pass
        except :
            langs[x.lang] = lang(x.lang)
            langs[x.lang].entries.append(x)
            pass
    return collections.OrderedDict(sorted(langs.items()))
def getRegions(entries):

    regions = {}
    for x in entries:

        try:
            regions[x.outletReg].entries.append(x)

            pass
        except :
            regions[x.outletReg] = region(x.outletReg)
            regions[x.outletReg].entries.append(x)
            pass
    return collections.OrderedDict(sorted(regions.items()))

def getJournalTypes(entries):

    journalTypes = {}
    for x in entries:
        if(x.outletType=="Journal"):
            try:
                journalTypes[x.journalType].entries.append(x)

                pass
            except :
                journalTypes[x.journalType] = journalType(x.journalType)
                journalTypes[x.journalType].entries.append(x)
                pass
        pass
    return collections.OrderedDict(sorted(journalTypes.items()))

def getPublishers(entries):

    journalTypes = {}
    for x in entries:
        if(x.outletType=="Journal"):
            try:
                journalTypes[x.outlet].entries.append(x)

                pass
            except :
                journalTypes[x.outlet] = journalType(x.outlet)
                journalTypes[x.outlet].entries.append(x)
                pass
        pass
    return collections.OrderedDict(sorted(journalTypes.items()))

def getJournalLangs(entries):

    outletLangs = {}
    for x in entries:

        try:
            outletLangs[x.outletLang].entries.append(x)

            pass
        except :
            outletLangs[x.outletLang] = outletLang(x.outletLang)
            outletLangs[x.outletLang].entries.append(x)
            pass
    return collections.OrderedDict(sorted(outletLangs.items()))

def getTopics(entries):

    topics = {}
    for x in entries:

        try:
            topics[x.topic].entries.append(x)

            pass
        except :
            topics[x.topic] = topic(x.topic)
            topics[x.topic].entries.append(x)
            pass
    return collections.OrderedDict(sorted(topics.items()))

def getOutletType(entries):

    topics = {}
    for x in entries:

        try:
            topics[x.outletType].entries.append(x)

            pass
        except :
            topics[x.outletType] = topic(x.outletType)
            topics[x.outletType].entries.append(x)
            pass
    return collections.OrderedDict(sorted(topics.items()))


def getTopicsSum(topics):
    sum =0
    for x,y in topics.items():
        sum+=len(y.entries)
        pass

    return sum

def getJournalSum(topics):
    sum =0
    for x,y in topics.items():
        sum+=len(y.entries)
        pass

    return sum

if __name__ == '__main__':
    entries = getEntries()
    authors = getAuthors(entries)
    years = getYears(entries)

    def getProductivityPerYear():
        productivityPerYear(years)

    def getProductivityPerYearProRated():
        productivityPerYearProRated(years)

    def getpercentLangPerYear():
        percentLangPerYear(years)

    def getPercentCoAuthoredperYear():
        percentCoAuthoredperYear(years)

    def getCoAuthoredTypePerYear():
        CoAuthoredTypePerYear(years)

    def getCollectiveHIndexByYear():
        collectiveHIndexByYear(years)

    def getMostUsedPublishers():
        mostUsedPublishers(entries)

    def getPercentRegionPerYear():
        percentRegionPerYear(years)

    def getPercentPerOutlettypePertime():
        percentPerOutlettypePertime(years)

    def getPercentPerOutletLangPertime():
        PercentPerOutletLangPertime(years)

    def getpercentTopicPerYear():
        percentTopicPerYear(years)

    def getCitationsperTopicperYear():
        citationsperTopicperYear(years)
    def quit():
         sys.exit(0)

    citationsperLaunguage(entries)

    options = {0 : getProductivityPerYear,
           1 : getProductivityPerYearProRated,
           2 : getpercentLangPerYear,
           3 : getPercentCoAuthoredperYear,
           4 : getCoAuthoredTypePerYear,
           5 : getCollectiveHIndexByYear,
           6 : getMostUsedPublishers,
           7 : getPercentRegionPerYear,
           8 : getPercentPerOutlettypePertime,
           9 : getPercentPerOutletLangPertime,
           10: getpercentTopicPerYear,
           11: getCitationsperTopicperYear,
           12 : quit
        }

    while True:
        print("""
0 : Productivity Per Year
1 : Productivity Per Year (Pro-Rated)
2 : Percent Language Per Year
3 : Percent CoAuthored Per Year
4 : Percent CoAuthored Type Per Year
5 : Collective H-Index By Year
6 : Most Used Publishers
7 : Percent for each Region Per Year,
8 : Percent Per Outlet Type Per Year
9 : Percent Per Outlet Language Per Year
10: Percent Per Outlet Language Per Year
11: citation per topic per year
12: Quit\n""")
        num = int(input("Please Enter A Selection:"))
        options[num]()
        temp = input("Press Enter to Select Another Option")

    #print(mostUsedPublishers(entries))

    print(percentPerOutlettypePertime(years))
