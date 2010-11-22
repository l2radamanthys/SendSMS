#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import urllib2 # import urlopen
import ClientForm


CLARO_CDMA = ["1"]
CLARO_GSM = ["2"]
PERSONAL = ["3"]
MOVISTAR_MOV = ["4"]
MOVISTAR_UNI = ["5"]
#NEXTEL = ["6"]
CLARO = CLARO_GSM


def main():
    request = urllib2.Request("http://www.argentour.com/es/sms/enviar_sms.php")
    response = urllib2.urlopen(request)
    forms = ClientForm.ParseResponse(response)#, backwards_compat=False)
    response.close()

    form = forms[0]

    form["empresa"] = CLARO_GSM
    form["codigo"] = "387" #codigo area
    form["telefono"] = "4494307" #numero
    form["email"] = "L2Radamanthys@gmail.com"
    form["nombre"] = "L2Radamanthys"
    form["mensaje"] = "prueba... test" #max 80 caracteres

    print form

    response = urllib2.urlopen(form.click())


if __name__ == '__main__':
    main()
