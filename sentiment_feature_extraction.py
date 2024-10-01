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
  if len(sys.argv) != 2:
    raise Exception(f"Expected 1 argument, got {len(sys.argv) - 1}")
  
  path = sys.argv[1]
  path = os.path.join(os.getcwd(), path)
  print(path)
  
  pickles = []
  files = os.listdir(path)
  for f in files:
    if f.endswith('.mid.pkl'):
      pickles.append(f)

  print(os.path.join(path, pickles[0]))


  # read file
  for pkl in pickles:
    with open(os.path.join(path, pkl), 'rb') as pickle_file:
      remi = pickle.load(pickle_file)
    
    pitches = get_pitches(remi)
    pitch_ave = get_pitch_average(pitches)
    pitch_var = get_pitch_variation(pitches)
    pitch_range = get_pitch_range(pitches)

    print(round(pitch_ave, 4), pitch_var, pitch_range)

if __name__ == "__main__":
  main()