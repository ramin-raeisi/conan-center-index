```
cd  to/the/project where conanfile.py has been located
conan create . j1939/v1 # this will create a package in your local

# repeat the above for each one(j1939/plantuml/graphviz)
```

go to the cpp project(digitalDash)

change the cononfile.txt

```
[requires]
openjdk/16.0.1
doxygen/1.9.4
graphviz/2.38.0@demo/v1
PlantUML/1.2020.0@demo/v3
J1939/1.1.0@j1939/v1
jsoncpp/1.9.5

[generators]
virtualenv
```

cd into build

```
cd /home/s/Codes/main_app/digitalDashProject
mkdir build
cd build
conan install ..
source activate.sh
cmake .. -DCMAKE_PREFIX_PATH=/home/saeed/Qt/6.3.2/gcc_64
```
