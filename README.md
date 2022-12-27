## Requirements
- python >= 3.8

### How to generate grammar - on linux
1. Install jdk
```bash
   sudo apt-get install default-jdk
```
2. Install antrl
```bash
   cd /usr/local/lib
   sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
   export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
```

3. Create virtual environment & install packages
```bash
    cd ${project folder}
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade setuptools
    pip install wheel
    pip install antlr4-python3-runtime==4.9.2
    pip install graphviz
```
4. Add to your .bashrc:
```
   alias grun='java org.antlr.v4.gui.TestRig'
   alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
```
5. Source bashrc:
```
   source ~/.bashrc
```
6. Genrate grammar:
```
antlr4 -Dlanguage=Python3 ./antlr/PP.g4 -visitor -o dist
```

## Running interpreter
- command prompt will appear and user can enter commands
- after command submission by `ENTER` command will be interpreted

1. Go into project folder
2. Activate virtual env:
   - linux:  `source venv/bin/activate`
   - windows: `.\venv\Scripts\activate`
3. Run programm: 
   - with realtime interpreter - `python runInterpreter.py`

## Generating programs
1. Go into project folder
2. Activate virtual env:
   - linux:  `source venv/bin/activate`
   - windows: `.\venv\Scripts\activate`
3. Run programm: 
   - with realtime interpreter - `python runGP.py`

### Fix bug in antlr code
Go to src/antlr4/tree/Tree.py and change:
```python
def aggregateResult(self, aggregate, nextResult):
      return nextResult
```
to
```python
def aggregateResult(self, aggregate, nextResult):
   if aggregate is None:
      return nextResult
   elif nextResult is None:
      return aggregate
   return aggregate + nextResult
```