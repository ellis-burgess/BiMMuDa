# The Billboard Melodic Music Dataset (BiMMuDa)

This repository is a fork of [The Billboard Melodic Music Dataset](https://github.com/madelinehamilton/), a MIDI dataset of the main melodies of the top five singles from the Billboard Year-End Singles Charts for each year from 1950 to 2022. More information about the project can be found in the Github repository, or in the [associated paper](https://www.nature.com/articles/s41598-024-64571-x).

All files in this repository's "bimmuda" folder are from the original repository. The "bimmuda_remis" folder contains every full MIDI file from the original dataset, converted into a REMI pkl file."

# REvamped MIDI-derived events (REMI)

REMI is a method for encoding symbolic music into text-based musical events for data analysis and use in machine learning. The "utils.py" file in this project's "remi" subfolder is taken from [YatinMusic's REMI repository](https://github.com/YatingMusic/remi). The "midi2remi.py" file in the same folder is an adaptation of the "midi2remi.ipynb" file from [the same source](https://github.com/YatingMusic/remi). More information about the project can be found in its Github repository, or in its [associatd paper](https://arxiv.org/abs/2002.00212).

# Extracting Sentiment Features from BiMMuda

Based on the research of [research of Panda et al](https://www.researchgate.net/publication/346359767_Audio_Features_for_Music_Emotion_Recognition_a_Survey), the following features have been identified as suitable for extraction from the melodic files in the BiMMuDa dataset. Features which depend on harmonic complexity or textural information, as well as features which do not have a clear consensus on impact on sentiment, have been omitted. Melodic contour has been omitted in this early stage of the research, as extracting melodic contour is more complex than extracting the remaining sentiment features.

| Attribute                     | Associated Quadrant(s) | Extraction Method |
| ----------------------------- | ---------------------- | ----------------- |
| High pitch                    | Q1, Q4                 | Y                 |
| Low pitch                     | Q2, Q3                 | Y                 |
| Large pitch variation         | Q1                     | Y                 |
| Small pitch variation         | Q3, Q4                 | Y                 |
| Wide pitch range              | Q1, Q4                 | Y                 |
| Narrow pitch range            | Q2                     | Y                 |
| Major mode                    | Q1, Q4                 | N/A               |
| Minor mode                    | Q2, Q3                 | N/A               |
| Fast tempo, high note density | Q1, Q2                 | N/A               |
| Slow tempo, low note density  | Q3, Q4                 | N/A               |

## High Pitch and Low Pitch
Determined as an average pitch from all note events in the file. For the purposes of this project, 60 (middle C) shall be determined as a threshold. Notes higher than 60 will be considered high pitch, and notes lower than or equal to 60 will be considered low pitch. An average pitch will be taken for all pieces of music.

## Wide and Narrow Pitch Variation
Pitch variation refers to the number of unique pitches within a piece. For the purposes of this project, pitches (as opposed to pitch classes) shall be used. Seven or more pitches in a melody (seven being the number of notes in a major or minor scale) shall be considered indication of wide pitch variation.

## Small and Large Pitch Range
For the purposes of this project, a large pitch range shall be any piece where the lowest note is greater than a scale lower than the highest note (lowest note < highest note - 12).

## Major or Minor mode
Modal data is provided in the original BiMMuDa dataset. Since modality is provided per melody in a piece, the modality of a piece shall be expressed as being in the range of -1 to 1, where -1 indicates that all melodies are minor, and 1 indicates that all melodies are major.

## Tempo
Tempo data is provided in the original BiMMuDa dataset. A BPM of 90 or greater shall be considered "fast".

## Note Density
Note onset density is provided in the original BiMMuDa dataset. A note onset density of 2.5 or greater shall be considered high density. The mean of note density in all melodies of a full piece shall be taken.