@echo off

echo Setting command to always overwrite

SET COPYCMD=/Y

echo Copying current layout to site themes...

copy "_global\theme\layout.html" "cubes\theme\templates\layout.html"
copy "_global\theme\layout.html" "brewery\theme\templates\layout.html"
copy "_global\theme\layout.html" "blog\theme\templates\layout.html"

echo Generating sites...

cd cubes

pelican content -s pelicanconf.py

cd ../brewery

pelican content -s pelicanconf.py

cd ../blog

pelican content -s pelicanconf.py

cd ../