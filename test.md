#burnPoint

*******************************************************************

##¿Que es burnPoint?

**burnPoint** es una herramienta que genera **toda la documentación** necesaria para una presentación a partir del mismo **archivo markdown**.

-------------------------------------------------------------------

El objetivo es generar las **diapositivas**, las **notas** para el orador y la **información complementaria** a partir de un mismo archivo de texto.

*******************************************************************

##¿Como funciona?
###burnPoint utiliza pandoc

burnPoint utiliza pandoc para generar los archivos. Y por lo tanto usa las mismas reglas que pandoc para generar las diapositivas.

-------------------------------------------------------------------

Para mas información sobre las reglas que utiliza pandc para generar las diapositivas ver la guía de usuario de pandoc.

*******************************************************************

##¿Como funciona?
###Reglas adicionales
####Transiciones

Para generar una transición:

    ********************************

-------------------------------------------------------------------

Para generar una transición: en burnPoint hay que añadir una fila de asteriscos:

*******************************************************************

Aqui va el texto

* Un punteo
* ldsjbbhfs
* ksd fdsjb fksd bf

Esta es una demostración de las notas: __este texto _debería_ ir en las notas__

-----------------------------------------

Entonces aqui va a ir mi texto informativo.
Esta parte __también podrá tener _notas_ __.

*******************************************

esta deberia ser ya otra diapo