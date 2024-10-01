import sentiment_feature_extraction
import os
import numpy
import pandas as pd
import pickle

root = os.getcwd()

per_melody_df = pd.read_csv(os.path.join(root, 'bimmuda/metadata/bimmuda_per_melody_metadata.csv'))
per_song_df = pd.read_csv(os.path.join(root, 'bimmuda/metadata/bimmuda_per_song_metadata.csv'))

per_song_df[['Year']] = per_song_df[['Year']].apply(pd.to_numeric)
per_song_df[['Position']] = per_song_df[['Position']].astype(str)

per_melody_df[['Year']] = per_melody_df[['Year']].apply(pd.to_numeric)
per_melody_df[['Position']] = per_melody_df[['Position']].astype(str)

remis_source = os.path.join(root, 'bimmuda_remis')
remis = os.listdir(remis_source)
fnames = [r.split('.')[0][:-5] for r in remis]

rows_list = []

for remi, fn in zip(remis, fnames):
  # load file
  src = os.path.join(remis_source, remi)
  with open(src, 'rb') as pickle_file:
    src = pickle.load(pickle_file)
  
  # get year & position
  year, pos = fn.split('_')
  pos = pos[1:] # remove leading 0

  # get title, artist, pitch STD
  song_row = per_song_df[(per_song_df['Year'] == int(year)) & (per_song_df['Position'] == pos)].iloc[0]
  melody_rows = per_melody_df[(per_melody_df['ID'].str.startswith(fn))]
  title = song_row['Title']
  artist = song_row['Artist']

  # get pitch STD, pitch average, pitch variation, and pitch range
  pitch_std = melody_rows['Pitch STD'].mean()

  pitches = sentiment_feature_extraction.get_pitches(src)
  pitch_ave = sentiment_feature_extraction.get_pitch_average(pitches)
  pitch_var = sentiment_feature_extraction.get_pitch_variation(pitches)
  pitch_range = sentiment_feature_extraction.get_pitch_range(pitches)

  # get mode polarity
  modes = melody_rows['Mode'].to_list()
  mode = 0
  for m in modes:
    if type(m) != str:
      continue
    if m.lower() == 'major':
      mode += 1
    elif m.lower() == 'minor':
      mode -= 1
    else:
      raise Exception('unexpected mode')
  
  # Normalize mode to between -1 and 1
  mode /= len(modes)

  # average BPM, note onset density
  bpms = melody_rows['BPM'].mean()
  onset_density = melody_rows['Onset Density'].mean()

  # store song data
  row = {'Title': title,
        'Artist': artist,
        'Year': year,
        'Position': pos,
        'Ave BPM': bpms,
        'Ave Pitch STD': pitch_std,
        'Ave Pitch Value': pitch_ave,
        'Pitch Variation': pitch_var,
        'Pitch Range': pitch_range,
        'Mode Polarity': mode,
        'Note Onset Density': onset_density,
        }
  rows_list.append(row)

df = pd.DataFrame(rows_list)
df.to_csv('sentiment_data.csv', index=False)