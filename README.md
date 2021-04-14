# Python App

## Create Virtual Environment

```bash
python -m venv .venv
```

```.venv``` is the name of the virtual environment.
You will see a folder created with the name .venv

## checking the python interpreter source

For unix based systems

```bash
which python
/Users/sravan/miniconda3/bin/python
```

For windows

```bash
where python
/Users/sravan/miniconda3/bin/python
```

## Activate the virtual environment

### For Unix based systems

```bash
source .venv/bin/activate
```

### For windows

```bat
.venv\Scripts\activate
```

## checking the python interpreter source after activating the virtual environment

```bash
which python
/Users/sravan/workapce/akademize/akademize-grofers-python-app/.venv/bin/python
```

For windows

```bash
where python
/Users/sravan/workapce/akademize/akademize-grofers-python-app/.venv/bin/python
```

## Deactivate virtual environment

```bash
deactivate
```

## Installing numpy

```bash
source .venv/bin/activate
```

```bash
pip install numpy
```

## Installing Jupyter and Ipykernel

```bash
pip install ipykernel jupyter
```

## Open Jupyter Notebook

```bash
jupyter notebook
```
