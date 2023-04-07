# finstem - simple tool for command-line Finnish stemming

## Quickstart

### On Ubuntu 22.04

```bash
# install libvoikko
sudo apt -y install -y voikko-fi python-libvoikko

# install click
pip install click

# clone the repo and run the command!
git clone https://github.com/hiAndrewQuinn/finstem
cd finstem

python finstem.py --help
python finstem.py 'kissa' 'kissat' 'anteeksi' 'peter'
```
