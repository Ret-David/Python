# David Martinez

# 1) Extract all the links from this website https://news.ycombinator.com/news using what
#    you have learned earlier. Feel free to use whatever tools and techniques you prefer.

# 2) In the same file, after you successfully get titles and links, then save all those to
#    text file or Excel file (your choice). The file should contain the name of each link
#    and the link itself.

import requests
from bs4 import BeautifulSoup  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import openpyxl                # https://openpyxl.readthedocs.io/en/stable/
import csv

''' This site was a royal pain, thank you very much!'''
source = requests.get('https://news.ycombinator.com/news').text
soup = BeautifulSoup(source, 'lxml')

wb = openpyxl.Workbook()            # create the wb instance
sheet = wb.active                   # create a new wb with an active sheet
sheet['A1'] = 'Headline'            # set A1
sheet['B1'] = 'Link'                # set B1

''' CSV writing technique learned from Corey Schafer'''
csv_file = open('PE08_David_Martinez_scrape_data.csv', 'w') # open file in write mode
csv_writer = csv.writer(csv_file)                           # instance(object)
csv_writer.writerow(["Headline", "Link"])                   # write headers on first row

''' Between the video and bs4 doc, I made the below. '''
for link in soup.find_all('a', class_='storylink'):         # step through all found
    print(link.get_text(strip=True))                        # print stripped text
    print(link['href'])                                     # print only the link
    print()                                                 # print blank line
    sheet.append([link.get_text(strip=True), link['href']]) # append results to sheet
    # write each new title and link to a new csv row
    csv_writer.writerow([link.get_text(strip=True), link['href']])

wb.save('PE08_David_Martinez_scrape_data.xlsx')             # save Excel file
csv_file.close()                                            # close CSV file
