#!/bin/bash


echo "** Python virtual environment setup **"

echo -e "\n[1] Activate" 
echo -e "[2] Deactivate\n" 

echo -n "Enter the option: "
read opt

if [ $opt -lt 1 ] || [ $opt -gt 2 ]; then
    echo "Invalid option"
    exit
fi

env_path=~/extras/Python/venv

if [ ! -d "$env_path" ]; then
    echo -n "Provide virtual environment path[Y/N]: "
    read path_opt

    if [ "$path_opt" != "Y" ]; then
        exit
    fi
    echo -n "Enter path: "
    read env_path
    if [ ! -d "$env_path" ]; then
        echo "Invalid path"
    fi
fi

echo "Virtual environment found at $env_path"

if [ $opt -eq 1 ]; then
    source "$env_path/bin/activate"
    echo "Virtual environment activated!!!"
else
    source "$env_path/bin/activate"
    deactivate
    echo "Virtual environment deactivated!!!"
fi
