#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
#import urllib2 # import urlopen
#import ClientForm

import urllib # import urlopen
import httplib


CLARO = ["1"]
PERSONAL = ["2"]
MOVISTAR = ["3"]
NEXTEL = ["4"]


NAV_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible) Cliente SMS (Alpha Version)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ar,es;q=0.8,en-us;q=0.5,en;q=0.3",
    "Accept-Charset": "utf-8,ISO-8859-1;q=0.7,*;q=0.7",
    "Keep-Alive": "300",
    "Proxy-Connection": "keep-alive",
}


def main():
    """
    request = urllib2.Request("http://www.altoque.com/sms/mensajes_al_celular.php")
    response = urllib2.urlopen(request)
    forms = ClientForm.ParseResponse(response)#, backwards_compat=False)
    response.close()

    form = forms[0]

    form["empre"] = CLARO #PERSONAL
    form["tel"] = "387" #codigo area
    form["tel1"] = "4494307" #numero
    form["mail"] = "L2Radamanthys@gmail.com"
    form["mensaje_tmp"] = "prueba... test" #max 110 caracteres
    form["totalcounter"] = str(len("prueba... test"))
    form["mensaje_hidden"] = "hola mundo"
    print form

    response = urllib2.urlopen(form.click())

    dict = {
        "empre": "1",
        "tel": "387",
        "tel1": "4494307",
        "mail": "hola@hl.com",
        "totalcounter": "10",
        "mensaje": "hola",
        "mensaje_tmp": "hola mundo",
        "mensaje_hidden": "hola mundo",
    }
    params = urllib.urlencode(dict)
    print params
    connection = httplib.HTTPConnection("http://www.altoque.com", 80)
    connection.request("POST", "/sms/atqs.php", params, NAV_HEADERS)
    connection.getresponse()
    """


if __name__ == '__main__':
    main()
