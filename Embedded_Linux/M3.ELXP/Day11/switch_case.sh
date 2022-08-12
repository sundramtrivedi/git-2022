#!/bin/bash
<<notes
case expression in
    pattern1)
    statements
    ;;
    pattern2)
    statements
    ;;
    pattern3)
    statements
    ;;
    *)
        statements
        ;;
    esac
notes
#ex for switch case
read -p "Enter country name: " country_name
case $country_name in 
    India)
        echo "India is world pharmacy"
        ;;
    Ireland)
        echo "One of the old civilizations"
        ;;
    *)
        echo "You dont belong to this planet"
        ;;
    esac

