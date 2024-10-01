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
      midis.append(pathname+"\\"+get_single_midi_file(f))
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
  output_path = os.path.join(path, "outputs")
  if not os.path.exists(output_path):
    os.makedirs(output_path)

  midis = []

  if path.endswith('.mid'):
    midis.append(get_single_midi_file(path))
  else:
    midis= get_many_midi_files(path)
  
  for midi in midis:
    midi_name = midi.split("\\")[-1]
    note_items, tempo_items = utils.read_items(midi)
    note_items = utils.quantize_items(note_items)

    items = tempo_items + note_items
    max_time = note_items[-1].end
    groups = utils.group_items(items, max_time)

    events = utils.item2event(groups)
    with open(output_path+"\\"+midi_name+".pkl", 'wb') as p:   
      pickle.dump(events, p)

if __name__ == "__main__":
  main()