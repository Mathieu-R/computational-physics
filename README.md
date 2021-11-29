# computational-physics

## Python
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mathieu-R/computational-physics/HEAD)
Jupyter Notebooks contenant différentes méthodes numériques utiles en physique.    
Les notebooks sont disponibles dans le dossier "python/notebooks".

### Installer jupyter 
Selon votre choix, vous pouvez installer jupyter lab ou jupyter notebook.
```bash
$ python3-m pip install notebook # jupyter notebook
```

### Installer un environnement virtuel
Créer un environnement virtuel.
```bash
$ python3-m venv env
$ source env/bin/activate
$ python3-m pip install --upgrade pip
```

Connecter Jupyter à l'environnement virtuel.
```bash
$ pip3 install ipykernel
$ python3 -m ipykernel install --name=env
```

Installer les packages utiles.
```bash
$ pip3 install numpy matplotlib scipy
```

### Lancer jupyter
```bash
$ jupyer notebook # ou notebook
```

### Supprimer l'environnement virtuel de Jupyter
```bash
$ jupyter kernelspec uninstall myenv
```

## C++
Basé sur le livre : "A practical introduction to computational physics and scientific computing (using C++)"