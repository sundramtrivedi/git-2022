#!/bin/bash
#take only package name from user
read -p "enter package name :" package_name
sudo apt install $package_name

#cmd and packge name variable
install_pkg="sudo apt install"
read -p "enter pkg name : " package_name
$install_pkg $package_name

remove_pk="sudo apt autoremove"
read -p "enter pkg name to remove:" pkg_name
$remove_pk $pkg_name