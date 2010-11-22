#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import urllib2 # import urlopen
import ClientForm




def main():
    request = urllib2.Request("http://www.altoque.com/sms/mensajes_al_celular.php")
    response = urllib2.urlopen(request)
    forms = ClientForm.ParseResponse(response)#, backwards_compat=False)
    response.close()

    form = forms[0]
    print form





if __name__ == '__main__':
    main()
