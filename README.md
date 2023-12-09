# finstem - simple tool for command-line Finnish stemming

Stems Finnish words. Takes any kinds of words you can throw at it. Even has its own tiny REPL!

![image](https://github.com/hiAndrewQuinn/finstem/assets/53230903/9d0eef09-6d25-4519-9dab-8773edc555a8)

## 📹 Video - silent install, 2023.12.07

[output-fast.webm](https://github.com/hiAndrewQuinn/finstem/assets/53230903/b9f5bb51-4a0d-4189-9876-14ca4b50da0e)

The above is 10x to give a feel for how the commands work. 

Normal-speed video: https://youtu.be/85qwsrGdwZs


Normal-speed video: 

## Quickstart

### On Ubuntu 22.04

_Tested on a **totally fresh** Vagrant install of Ubuntu 22.04. You probably already have some or all of these installed._

```bash
# Install the prerequisites
yes | sudo apt update
yes | sudo apt install pip python-is-python3
yes | sudo apt install voikko-fi python-libvoikko python3-click

# clone the repo and run the command!
git clone https://github.com/hiAndrewQuinn/finstem
cd finstem

python finstem.py --help
python finstem.py 'Näin' 'tervetuloa' 'kiltti' 'kissa' 'Nimeni' 'on' 'Jeff'
```

## For scripters

`finstem` supports (experimental) CSV, TSV and JSON formats. 

### CSV format example

```bash
python finstem.py 'Näin' 'tervetuloa' 'kiltti' 'kissa' '.' 'Nimeni' 'on' 'Jeff' --format CSV | csvlook
```

![image](https://github.com/hiAndrewQuinn/finstem/assets/53230903/95b28509-b134-4915-a781-5d9eb1365ea8)

### TSV format example

```bash
python finstem.py 'Näin' 'tervetuloa' 'kiltti' 'kissa' '.' 'Nimeni' 'on' 'Jeff' --format TSV | awk '{print $3 " <~> " $2 " <~> " $1}'
```

![image](https://github.com/hiAndrewQuinn/finstem/assets/53230903/4d2304a9-1848-4d85-af48-cdf2bc75c142)


### JSON format example

```bash
python finstem.py 'hyvää' 'huomenta' --format JSON | \
while IFS= read -r line; do
    echo "$line" | jq .
done
```

![image](https://github.com/hiAndrewQuinn/finstem/assets/53230903/2784dd38-af83-4c11-bc5c-5b12c9ba5580)


Use with caution. I haven't used proper libraries for these yet.

## Advanced

### Passing a list of words in a text file

```bash
echo 'sana' > words.txt
echo 'vaimonille' >> words.txt
echo 'kirjoja' >> words.txt

# Pass each line as an argument to finstem.py
cat words.txt | xargs -n 1 python finstem.py
```

![image](https://user-images.githubusercontent.com/53230903/230723659-e016d3be-77ed-4a2b-9ce0-a3fb16ef10a0.png)

### Interactive mode

_Requires [fzf](https://github.com/junegunn/fzf)._

```bash
echo '' | fzf --print-query \
	--preview-window='bottom:50%' \
	--preview "echo {q} | tr ' ' '\n' | xargs -I _ python finstem.py _" \
	--bind "enter:execute(echo {q} | tr ' ' '\n' | xargs -I _ python finstem.py _)+abort"
```

If you don't feel like typing out all that, just run `finstem-interactive.sh`.


#### For use with [`finfreq10k`](https://ankiweb.net/shared/info/1149950470) when reading a book

`finfreq10k` is an Anki deck containing the 10,0000 most common Anki words in
order, made by yours truly. Using it in combination with `finstem` creates a
powerful way to target your vocabulary practice to the words you have actually
read that day.

# Other screenshots


![image](https://github.com/hiAndrewQuinn/finstem/assets/53230903/004fbbc1-3088-4efd-a484-0b04f6db309b)

![image](https://github.com/hiAndrewQuinn/finstem/assets/53230903/093efe66-3688-4358-a5b1-6e022a5f79f1)

