import urllib, urllib2, xml.etree.ElementTree as ET, \
        requests, logging 

from flask import Flask, request, Blueprint, current_app, \
                    redirect, url_for, render_template
from flask.json import jsonify


mod = Blueprint('METAR', __name__)

@mod.route('/')
def index():
    if request.args.get('code') != None:
        current_app.logger.DEBUG("Returned an error code")
        
    return make_response(open('flaskSandbox/static/base.html').read())


#This calls the function when the /METAR/(a variable) is called. 
#For Example, /METAR/KROC will pass stationInfo=KROC into the function
@mod.route('/search', methods=['GET', 'POST'])
def search():

    print("Getting Metar for: " + request.args.get('station'))
    
    x = 0
    while x < 100000000:
        x += 1

    if (request.method == 'GET'):
        stationInfo = request.args.get('station')
        data = "&stationString=" + stationInfo + "&hoursBeforeNow=2"
    
    elif request.method == 'POST':
        stationInfo = request.form['stationInfo']
        data = "&stationString=" + stationInfo + "&hoursBeforeNow=2"
    
    else:
        return redirect(url_for('.index', code=304))
    
    #Build the URL
    source = "https://aviationweather.gov/adds/dataserver_current/httpparam" \
             "?dataSource=metars&requestType=retrieve&format=xml"
    
    #Make the connection the the URL
    response = urllib.urlopen(source + data)
    
    #Parse the XML into an ElementTree object and retrieve the root
    tree = ET.parse(response)
    root = tree.getroot()
    
    #Find the data needed (In this case temperature) and return it as a string
    data = root.find('data/METAR')
    
    returnData = dict()
    for value in data.iter():
        if(value.tag != 'METAR'):
            returnData[value.tag] = value.text 
    
    return jsonify(data=returnData, stationInfo=stationInfo)
