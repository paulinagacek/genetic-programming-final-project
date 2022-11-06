## Configuration
### How to configure - on linux
1. Install jdk
   ```
   sudo apt-get install default-jdk
   ```
2. Install antrl
```
   cd /usr/local/lib
   sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
   export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
```
3.  git clone

4. Create virtual environment & install packages
   ```bash
    cd ${project folder}
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade setuptools
    sudo apt-get install python3-tk
    sudo apt install python3-wxgtk4.0
    pip install wheel
    pip install antlr4-python3-runtime==4.9.2
    pip install pygame
    pip install libgtk-3-dev
   ```
5. Add to your .bashrc:
```
   alias grun='java org.antlr.v4.gui.TestRig'
   alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
```
6. Source bashrc:
```
   source ./.bashrc
```

## (optional) Creating lexer and parser - this command will automatically generate whole dist folder
*Do not do  it if dist folder is up to date with the grammar*
```
antlr4 -Dlanguage=Python3 ./antlr4/App.g4  -visitor -o dist3
```

### How to configure - on windows
1. Make sure you have jdk installed and path to \bin\javac is in yout PATH, [nice jdk](https://learn.microsoft.com/pl-pl/java/openjdk/download)
2. git clone
3. Create virtual environment & install packages
   ```bash
    cd ${project folder}
    python -m venv venv
    venv\Scripts\activate
    pip install --upgrade setuptools
    pip install wheel
    pip install antlr4-python3-runtime==4.9.2
   ```


## Run
### How to run main.py - linux
1. Go into project folder
2. Activate virtual env `source venv/bin/activate`
3. Run programm: 
      - with realtime interpreter - `python3 main.py`
      - from file in `\examples` - `python3 main.py <filename>`