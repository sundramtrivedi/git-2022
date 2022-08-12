#!/bin/bash
read -p "Enter your country name :" country_name
case $country_name in
	India)
		echo "India is country that produces brilliant minds of the world"
	;;
	Ireland)
		echo "A small country with rich culture"
	;;
	*)
		echo "You doesn't belong to this planet"
	;;
	esac
