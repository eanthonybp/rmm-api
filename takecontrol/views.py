from flask_init import app
from flask import render_template, redirect, url_for, session, request
from takecontrol.form import TakeControlForm
import requests
import xml.etree.ElementTree as ET



@app.route('/takecontrol',methods=('GET','POST'))
def takecontrol():
    form = TakeControlForm()
    if request.method=='GET':
        return render_template("/takecontrol.html", form=form)
        
    if request.method=='POST':
        apicall = "https://www.systemmonitor.us/api/?apikey=%s&service=get_take_control_connection_url&deviceid=%s" % (form.apikey.data,form.deviceid.data)
        xmlresponse = requests.get(apicall)
        root = ET.fromstring(xmlresponse.content)
        connecturl = root[0].text
        
        return redirect(connecturl)
        
@app.route('/tc/<apikey>/<deviceid>/')
def tc(apikey,deviceid):
    apicall = "https://www.systemmonitor.us/api/?apikey=%s&service=get_take_control_connection_url&deviceid=%s" % (str(apikey),str(deviceid))
    xmlresponse = requests.get(apicall)
    root = ET.fromstring(xmlresponse.content)
    connecturl = root[0].text
    return redirect(connecturl)
    
    
