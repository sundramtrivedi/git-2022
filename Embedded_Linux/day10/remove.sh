#!/bin/bash
read -p "Name the package to install :" toInstall
echo "Removing the previously install package!"
sudo apt autoremove $toInstall
echo "No re-installing the entered file"
sudo apt-get install $toIntstall
