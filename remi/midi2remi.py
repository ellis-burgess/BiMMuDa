import miditoolkit
import os
import pickle
import sys
import utils

def get_single_midi_file(filename):
  return filename

def get_many_midi_files(pathname):
  midis = []
  files = os.listdir(pathname)
  for f in files:
    if f.endswith('.mid'):
      midis.append(get_single_midi_file(f))
  if len(midis) == 0:
    raise Exception(f"No .mid files found.")
  return midis

def main():
  if len(sys.argv) != 2:
    raise Exception(f"Expected 1 argument, got {len(sys.argv) - 1}")
  path = sys.argv[1]
  working_dir = os.getcwd()
  print(working_dir)
  path = os.path.join(working_dir, path)
  print(path)

  midis = []

  if path.endswith('.mid'):
    midis.append(get_single_midi_file(path))
  else:
    midis.append(get_many_midi_files(path))
  
  for midi in midis:
    note_items, tempo_items = utils.read_items(midi)
    note_items = utils.quantize_items(note_items)

    items = tempo_items + note_items
    max_time = note_items[-1].end
    groups = utils.group_items(items, max_time)

    events = utils.item2event(groups)
    with open(path+".pkl", 'wb') as p:   
      pickle.dump(events, p)

if __name__ == "__main__":
  main()