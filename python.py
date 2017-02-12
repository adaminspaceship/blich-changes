import requests

def email_alert(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/blich/with/key/pYTi1N5f7ucT6tqt0PZjDVfgTjg_0rz6wRlI5EorafI", data=report)  
