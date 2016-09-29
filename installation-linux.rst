================================
Installation auf Linux-Rechnern
================================

* Miniconda von der `Download-Seite`_ herunterladen.  Wählen Sie die
  Version mit Python 3.5 für Ihr Betriebssystem

* Die heruntergeladene Datei ausführbar machen:

.. code:: bash

	  chmod u+x Miniconda3-latest-Linux-x86*.sh

* Die heruntergeladene Datei ausführen.  Das
  Installationsprogramm wird ausgeführt.  Am besten beantwortet man
  alle Fragen mit "yes"

* Öffnen Sie eine neues Terminal  und installieren Sie die benötigten Bibliotheken mit dem Befehl 

.. code:: bash

  conda install jupyter scipy sympy matplotlib


===================
Start des Notebooks
===================

Die graphische Oberfläche wird vom "Jupyter Notebook" zur Verfügung
gestellt.   Zum Start gibt man ein

.. code:: bash

   jupyter notebook
   

Nach kurzer Wartezeit öffnet sich der Browser mit der lokalen jupyter-Seite.  



.. _Download-Seite: http://conda.pydata.org/miniconda.html




Fragen
======

* Wie findet man heraus, ob man 32-bit oder 64-bit Linux hat?

.. code:: bash

   uname -p

gibt den Prozessortyp an; wenn die letzten beiden Ziffern gleich 64 sind, hat man eine 64-bit Maschine, sonst nicht

