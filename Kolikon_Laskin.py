import pandas as pd
from pathlib import Path
import glob
import os
downloads_path = str(Path.home() / "Downloads")
list_of_files = glob.glob(downloads_path + "\\*") # * means all if need specific format then *.csv
file = max(list_of_files, key=os.path.getmtime)
print("Käytetään uusinta csv tiedostoa Downloads kansiossa.")
print("Tiedosto jota käytetään:", file)
print("---------------------")
df = pd.read_csv(file) 
sheetTotal = df['Words'].sum()
translatorOne = df.loc[df['Translator'] == 297410829589020673, 'Words'].sum()
translatorTwo = df.loc[df['Translator'] == 696421760890962061, 'Words'].sum()
translatorThree = df.loc[df['Translator'] == 404554986396319744, 'Words'].sum()
translatorFour = df.loc[df['Translator'] == 541652140687360010, 'Words'].sum()
proofreaderOn = df.loc[df['Proofreader(s)'] == 404554986396319744, 'Words'].sum()
proofreaderTw = df.loc[df['Proofreader(s)'] == 541652140687360010, 'Words'].sum()
print(f"Sheetin sanamäärä: {sheetTotal}")
print("Kuinka monta sanaa jokainen käänsi:")
print("Masterjoona:",translatorOne, "\nSiri:",translatorTwo, "\nSusmot:", translatorThree, "\nNuclide:",translatorFour)
print("---------------------")
print("Kuinka montaa sanaa proofreadtiin:")
print("Susmot:", proofreaderOn, "\nNuclide:", proofreaderTw)

totalWords = int(sheetTotal) + (int(sheetTotal) * 0.85)
proofreaderOne = proofreaderOn * 0.85
proofreaderTwo = proofreaderTw * 0.85
TranslatorOne = int(translatorOne) / int(totalWords)
TranslatorTwo = int(translatorTwo) / int(totalWords)
TranslatorThreee = int(translatorThree) / int(totalWords)
TranslatorFourr = int(translatorFour) / int(totalWords)
ProofreaderOnee = int(proofreaderOne) / int(totalWords) 
ProofreaderTwoo = int(proofreaderTwo) / int(totalWords) 
print("---------------------")
print('TR Masterjoona', TranslatorOne * 7.5 )
print('TR Siri', TranslatorTwo * 7.5)
print('TR Susmot ', TranslatorThreee * 7.5)
print('TR Nuclide',TranslatorFourr * 7.5)
print('PR Susmot ', ProofreaderOnee * 7.5)
print('PR Nuclide',ProofreaderTwoo * 7.5)
print("---------------------")
input("Paina enteriä sulkeaksesi")
