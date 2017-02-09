============================================================
Installation von Mayavi auf Linux-Systemen
============================================================

Voraussetzung ist, dass conda bereits installiert ist.  Die Anleitung
funktioniert nur für 64-Bit Systeme.  Andere müssen wahrscheinlich
aus den Quellen bauen.

* Mayavi und sympy in eine neue Umgebung installieren, und zwar unter
  Python3:

.. code:: bash
	  
	  conda create -n mayavi python=3 pyqt=4
	  source activate mayavi
	  conda install ipython sympy scipy
	  conda install -c menpo mayavi

* Mayavi arbeitet unter Python3 nicht mit Jupyter zusammen.  Daher
  startet man es unter ipython in einem Terminal:

.. code:: bash

	  source activate mayavi

Die Schwierigkeit liegt augenblicklich (Februar 2017) darin, dass
weder das Mayavi aus den offiziellen Conda-Quellen noch die notwendige
Notebook-Extension an Python3 und QT5 angepasst sind.  Meine Anleitung
fasst die Diskussion unter
https://github.com/enthought/mayavi/issues/84 zusammen.
	  ipython --gui=qt

