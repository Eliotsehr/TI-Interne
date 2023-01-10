#!/usr/bin/env python3

import argparse
import socket

# Créer un parseur d'arguments
parser = argparse.ArgumentParser()

# Ajouter un argument pour le fichier en entrée et l'option d'output
parser.add_argument("input_file", help="nom du fichier en entrée")
parser.add_argument("-o", "--output", help="nom du fichier de sortie")

# Analyser les arguments
args = parser.parse_args()

# Ouvrir le fichier en entrée en lecture
with open(args.input_file, "r") as input_file:
  # Initialiser un tableau pour stocker les résultats
  results = []

  # Pour chaque ligne dans le fichier
  for line in input_file:
    # Sélectionner la troisième colonne
    column3 = line.split()[2]

    # Résoudre l'adresse IP du domaine
    try:
      ip = socket.gethostbyname(column3)
    except:
      # Si l'adresse IP ne peut pas être résolue, passer à la ligne suivante
      continue

    # Déduire le subnet en /24
    subnet = ".".join(ip.split(".")[:3]) + ".0/24"

    # Ajouter le subnet au tableau de résultats
    results.append(subnet)

# Supprimer les doublons du tableau de résultats
unique_results = list(set(results))

# Si l'option d'output est présente
if args.output:
  # Écrire les résultats dans le fichier spécifié par l'option
  with open(args.output, "w") as output_file:
    for item in unique_results:
      output_file.write("%s\n" % item)
else:
  # Afficher les résultats
  for item in unique_results:
    print(item)