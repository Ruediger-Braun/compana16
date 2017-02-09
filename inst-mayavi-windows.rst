============================================================
Installation von Mayavi auf Windows-Systemen
============================================================

Voraussetzung ist, dass conda bereits installiert ist.  

* Um Mayavi und sympy in eine neue Umgebung zu installieren öffnet man
  eine Eingabeaufforderung und gibt ein

.. code:: bash
	  
	  conda create -n mayavi python=3 pyqt=4
	  activate mayavi
	  conda install ipython sympy scipy
	  conda install -c menpo mayavi

* Mayavi arbeitet unter Python3 nicht mit Jupyter zusammen.  Daher
  startet man es unter ipython in einer Eingabeaufforderung

.. code:: bash

	  activate mayavi
	  ipython --gui=qt

Die Schwierigkeit liegt augenblicklich (Februar 2017) darin, dass
weder das Mayavi aus den offiziellen Conda-Quellen noch die notwendige
Notebook-Extension an Python3 und QT5 angepasst sind.  Meine Anleitung
fasst die Diskussion unter
https://github.com/enthought/mayavi/issues/84 zusammen.
