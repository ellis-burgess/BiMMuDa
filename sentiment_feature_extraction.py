import miditoolkit
import os
import pickle
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'remi'))

import utils


def get_pitch_average(remi):
  # if event is note, get pitch
  pitches = []
  for ev in remi:
    if ev.name == 'Note On':
      pitches.append(ev.value)
  # average all pitches
  return sum(pitches) / len(pitches)

def main():
  # read file
  file = os.path.join(os.path.dirname(__file__), "bimmuda_remis/1950_01_full.mid.pkl")
  with open(file, 'rb') as pickle_file:
      remi = pickle.load(pickle_file)
  
  print(get_pitch_average(remi))

if __name__ == "__main__":
  main()