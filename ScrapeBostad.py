import requests 
import ast

def unique_elem(list1,list2):
    s = set(list1)

    for id in list2:
        if id in s: return False
        s.add(id)
    return True

def word_match(string_list,char_list,full_list):
    for index,char in enumerate(string_list):
        if char in char_list:
            full_dict = full_list[char_list.index(char)]
            full_old = full_dict['Original']

            word_range = index + len(full_old)
            full_actual = "".join(string_list[index:word_range])

            if full_actual == full_old: 
                string_list[index:word_range] = list(full_dict['Replacement'])

    return string_list

search_list = [{'Original':'null','Replacement':'None'},{'Original':'false','Replacement':'False'},{'Original':'true','Replacement':'True'}]
search_keys = ['n','f','t']

#Convinience
def format_arr(arr):

    split_string = list(arr)
    split_string = word_match(split_string,search_keys,search_list)
    return "".join(split_string)

url = 'https://bostad.stockholm.se/Lista/AllaAnnonser'
dump_loc = 'C:\\Users\\Mbwenga\\Documents\\ML\\Python\\HTML.txt'

bostad = requests.get(url)
dump = open(dump_loc, 'r+')
#old_list = ast.literal_eval(dump)
new_list = None

text_out = bostad.text
#split = list(text_out)
#Debug: print(split)

form_new_list = format_arr(text_out)

with dump as file:

    file.write(form_new_list)
    new_list = ast.literal_eval(form_new_list)
    file.close()

print('Scrape Done!')
key = 'Ungdom'

elig = [apt['AnnonsId'] for apt in new_list if apt['Ungdom']]
print('Number of appartments:' + str(len(elig)))
#old_elig = [apt['AnnonsId'] for apt in old_list if apt['Ungdom']]

#if unique_elem(elig,old_elig):
#    print("New appartments in the list!")
#else:
#    print("Same old, same old.")

print(len(elig))
print(elig)
#structure: Run each 30 min, checking if annonsId array is similar. if not, send email about annons and possibly
#
#url(regular url for main site with annonsid as query in it)

#utility fnc:
#script = 'C:\\Users\\Mbwenga\\Documents\\ML\\Python\\ScrapeBostad.py'
#def runscrape:
#    exec(open(script).read())

#exec python C:\Users\Mbwenga\Documents\ML\Python\ScrapeBostad.py
#interactive: 'C:\\Users\\Mbwenga\\Documents\\ML\\Python\\ScrapeBostad.py'
#Some copy paste abstraction from python SMTP documentation page, outline for
#Possible implementation of email system for newly added appartments

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile) as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % 'textfile'
msg['From'] = 'me'
msg['To'] = 'mbwenga.maliti@edu.huddinge.se'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()