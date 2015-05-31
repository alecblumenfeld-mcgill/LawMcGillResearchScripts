import codecs
from scholar import *
from bs4 import BeautifulSoup
from xlrd import open_workbook
import xlwt


output = xlwt.Workbook()
sh = output.add_sheet("output",cell_overwrite_ok=True)


querier = ScholarQuerier()

workbook = open_workbook('testforscraper.xlsx')

for s in workbook.sheets():
    print 'Sheet:',s.name
    print s.nrows
    for row in range( s.nrows):
        for col in range(s.ncols):
            sh.write(row, col, s.cell(row,col).value)
        citationValue= s.cell(row,15).value
        if citationValue == "":
            query = SearchScholarQuery()
            query.set_author(s.cell(row,1).value)
            query.set_words(s.cell(row,0).value)
            query.set_num_page_results(1)
            querier.send_query(query)
            try:
                print querier.articles[0].attrs.get("num_citations")[0]
                sh.write(row, 15, querier.articles[0].attrs.get("num_citations")[0])
            except:
                sh.write(row, 15, "None in google")

                print "None in google"
                pass

        else:
            print citationValue


output.save("testforscraper_citations_updated.xls")









