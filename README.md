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