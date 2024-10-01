import miditoolkit
import os
import pickle
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'remi'))

import utils

def get_pitches(remi):
  # if event is note on, get pitch
  pitches = []
  for ev in remi:
    if ev.name == "Note On":
      pitches.append(ev.value)
  return pitches

def get_pitch_average(pitches):
  return sum(pitches) / len(pitches)

def get_pitch_variation(pitches):
  return len(set(pitches))

def get_pitch_range(pitches):
  return max(pitches) - min(pitches)

def main():
  # read file
  file = os.path.join(os.path.dirname(__file__), "bimmuda_remis/1950_01_full.mid.pkl")
  with open(file, 'rb') as pickle_file:
      remi = pickle.load(pickle_file)
  
  pitches = get_pitches(remi)
  print(get_pitch_average(pitches))
  print(get_pitch_variation(pitches))
  print(get_pitch_range(pitches))

if __name__ == "__main__":
  main()