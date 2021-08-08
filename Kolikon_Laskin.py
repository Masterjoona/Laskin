import pandas as pd
from pathlib import Path
import glob
import os

################# CONFIG #####################
#
#
rounding = True
#
#
##############################################
# Finding the newest file
valinta = input("Paina 1, jos haluat automaattisen tiedoston etsinnän. Paina 2 jos haluat syöttää itse tiedoston sijainin.\n")

def laskin():
    # Gathering the necessary information
    df = pd.read_csv(file) # Reads the csv file
    sheetTotal = df['Words'].sum() # Counts the words in the csv file
    translator_joona = df.loc[df['Translator'] == 297410829589020673, 'Words'].sum()
    translator_siri = df.loc[df['Translator'] == 696421760890962061, 'Words'].sum()
    translator_susmot = df.loc[df['Translator'] == 404554986396319744, 'Words'].sum()
    translator_nuclide = df.loc[df['Translator'] == 541652140687360010, 'Words'].sum()
    proofreader_susmot = df.loc[df['Proofreader(s)'] == 404554986396319744, 'Words'].sum()
    proofreader_nuclide = df.loc[df['Proofreader(s)'] == 541652140687360010, 'Words'].sum()

    # Presenting user with information
    print(f"Sheetin sanamäärä: {sheetTotal}")
    print("Käännetyt sanat")
    print("Masterjoona:",translator_joona, "\nSiri:",translator_siri, "\nSusmot:", translator_susmot, "\nNuclide:",translator_nuclide)
    print("---------------------")
    print("Proofreadatut sanat:")
    print("Susmot:", proofreader_susmot, "\nNuclide:", proofreader_nuclide)
    print("---------------------")

    # Taking proofreaders into the calculation
    totalWords = int(sheetTotal) + (int(sheetTotal) * 0.85)
    proofreader_susmot = proofreader_susmot * 0.85
    proofreader_nuclide = proofreader_nuclide * 0.85

    # Combining proofread and Translated
    reward_susmot = int(proofreader_susmot) + int(translator_susmot)
    reward_nuclide = int(proofreader_nuclide) + int(translator_nuclide)

    # Calculating rewards
    reward_joona = translator_joona * 7.5 / int(totalWords)
    reward_siri = int(translator_siri) * 7.5 / int(totalWords) 
    reward_nuclide = reward_nuclide * 7.5 / int(totalWords) 
    reward_susmot = reward_susmot * 7.5 / int(totalWords) 

    if rounding:# If rounding is turned ON in the config, rounds the answers to 2 decimals.

        # Rounding up to 2 decimals
        reward_joona = str(round(reward_joona, 2))
        reward_siri = str(round(reward_siri, 2))
        reward_nuclide = str(round(reward_nuclide, 2))
        reward_susmot = str(round(reward_susmot, 2))


    # Showing rewards to the user

    print("     Palkinnot")
    print("---------------------")
    print('Masterjoona', reward_joona)
    print('Siri', reward_siri)
    print('Susmot ', reward_susmot)
    print('Nuclide', reward_nuclide)
    print("---------------------")

    input("Paina mitä tahansa sulkeaksesi laskimen")

def autoFindCsv():
    print("Etsitään uusinta sheettiä")
    downloads_path = str(Path.home() / "Downloads") # Goes to %userprofile%\Downloads
    list_of_files = glob.glob(downloads_path + "\\*.csv") # Finds all .csv files
    global file
    file = max(list_of_files, key=os.path.getmtime) # Finds the newest one
    # Telling the user whats happening
    print("Uusin sheetti löytynyt:", file)
    print("---------------------")
    laskin()
if valinta == "1":
    autoFindCsv()
if valinta == "2":
    global file
    file = input("Anna tiedoston sijainti\n")
    laskin()
