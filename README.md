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

## Advanced

### Passing a list of words

```bash
echo 'sana' > words.txt
echo 'vaimonille' >> words.txt
echo 'kirjoja' >> words.txt

# Pass each line as an argument to finstem.py
cat words.txt | xargs -n 1 python finstem.py
