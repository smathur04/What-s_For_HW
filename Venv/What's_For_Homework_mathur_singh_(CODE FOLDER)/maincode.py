import os
import requests
from flask import Flask, render_template
import urllib3.request
from bs4 import BeautifulSoup
import re

''' 
IMPORTANT!!! MUST READ!!! PLEASE VIEW THE INSTRUCTIONS FOR RUNNING TEXT FILE
IN ORDER TO PROPERLY EXECUTE ALL THE CODE. THANK YOU
'''

#disables useless warnings made by cloud9
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()


app = Flask(__name__)

#route for login page
@app.route("/")
@app.route("/login")
def login():
    '''
    takes no input
    returns the webpage with the rendertemplate
    links to a html render template and acesses html code to display on page
    '''
    return render_template('index.html')
    
#route for homepage
@app.route("/home")
def home():
    '''
    takes no input
    returns the webpage with the rendertemplate
    links to a html render template and acesses html code to display on page
    Goes to Shaan's math teacher's site and pulls the homework for Mon 2/11 and
    sends it to be used in the HTML template
    '''
    #goes to teacher site and gathers source code as unicode string
    source = requests.get("https://sites.google.com/dublinusd.org/mrleedhs/lesson-plans").text
    #parses the code with lxml parser
    soup = BeautifulSoup(source, 'lxml')
    #finds specific assignment
    mathHW = soup.find_all(string= re.compile("Mon 2/11"))
    #turns assignment into useable string
    mathHW = str(mathHW[1])
    return render_template('mathur_singh_home.html', mathHW = mathHW)

#route for grades page   
@app.route("/grades")
def grades():
    '''
    takes no input
    returns the webpage with the rendertemplate
    links to a html render template and acesses html code to display on page
    '''
    return render_template('mathur_singh_grades.html')

#runs the website on this link and port
app.run(host=os.getenv('IP','mathur_singh_project'), port=int(os.getenv('PORT', 8080)))


