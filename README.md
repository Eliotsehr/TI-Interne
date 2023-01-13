# TI-Interne

## Introduction

Ce script permet de découvrir les subnets hébergeant des machines enregistrées dans un domaine active directory. L'idée est d'utiliser l'ensemble des noms des machines récupérées avec l'outil ldapdomaindump puis effectuer une résolution DNS sur ces noms afin de déduire les sous-réseaux.

## Utilisation
```shell
#Avec domain_computers.grep le résultat de ldapdomaindump
./subnetfinder.py domain_computers.grep -o subnets.txt
```
