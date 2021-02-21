# computational-physics
Jupyter Notebooks contenant différentes méthodes numériques utiles en physique.    
Les notebooks sont disponibles dans le dossier "notebooks".

### Installer un environnement virtuel
Créer un environnement virtuel
```bash
$ python3-m venv env
$ source env/bin/activate
$ python3-m pip install --upgrade pip
```

Connecter Jupyter à l'environnement virtuel
```bash
$ pip3 install ipykernel
$ python3 -m ipykernel install --name=env
```

Installer les packages utiles
```bash
$ pip3 install numpy matplotlib scipy
```

### Supprimer l'environnement virtuel de Jupyter
```bash
$ jupyter kernelspec uninstall myenv
```


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mathieu-R/computational-physics/HEAD)