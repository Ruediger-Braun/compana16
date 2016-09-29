=================================
Installation auf Windows-Rechnern
=================================

* Miniconda von der `Download-Seite`_ herunterladen.  Wählen Sie die Version für mit Python 3.5 für Ihr Betriebbsystem

* Die heruntergeladene Datei ausführen.  Dadurch startet das Installationsprogramm wird ausgeführt.  Am besten akzeptiert man alle Voreinstellungen.

* Öffnen Sie eine "Eingabeaufforderung" (finden Sie über die Suchfunktion) und installieren Sie die benötigten Bibliotheken mit dem Befehl 

.. code:: PowerShell

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

   gibt den Prozessortyp an; die letzten beiden Ziffern gleich 64
   sind, hat man eine 64-Bit Maschine, sonst nicht
