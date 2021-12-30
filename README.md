## Create Environment
```bash
conda create -n env_name python==3.7
```

## Create Templates.py File
The Given File Can Be Used To Create The Project Structure

## Create Requirements.txt File & Install All Dependency
```bash
pip install -r requirements.txt
```

## Steps For DVC & Git Utilization
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given\Database_Credit.csv
```
```bash
git add . && git commit -m "Frist Commit"
```
```bash
git remote add origin https://github.com/mayurborkar/Credit-Risk-MLOPS.git
```
```bash
git branch -M main && git push -u origin main
```
## After Creating Every Stage In DVC.yaml File Use below Command
```bash
dvc repro
```
## Checking Metrics In DVC
```bash
dvc metrics show
```
## Checking The Difference In Metrics
```bash
dvc metrics diff
```
## Tox
Tox Can Be Used For Creating The Virtual Env. In that We Can Test Our Test
Cases That Are We Mention in The **test** Folder.
```bash
tox
```
If You Had Done Some Changes In Requirements File. If You Want To Run Again 
Tox Command For That
```bash
tox -r
```
We Can Also Run Directly test Cases With The Help Of Below Command
```bash
pytest -v
```
To Create The Standard pypi package, there is command
```bash
python setup.py sdist bdist_wheel
```