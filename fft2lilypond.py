# import libraries
import math
import argparse
import os

print('''
take the FFT (.txt file) and from the result of the FFT Analysis do a lilypond score file
''')

parser = argparse.ArgumentParser()
parser.add_argument("listsfile", help="Name of the lists file with the extension")
args = parser.parse_args()

listsfile_no_ext = os.path.splitext(args.listsfile)[0]

with open(args.listsfile) as f:
    frequencies = []
    amplitudes = []
    bandwidths = []
    for line in f:
        if listsfile_no_ext+"_frequencies" in line:
            frequencies = [float(x) for x in f.readline().split(", ")]
        elif listsfile_no_ext+"_amplitudes" in line:
            amplitudes = [float(x) for x in f.readline().split(", ")]
        elif listsfile_no_ext+"_bandwidths" in line:
            bandwidths = float(line.split("=")[1])

def closest_note_name(freq, amp):
    C4_frequency = (261.63 / 2)
    note_names = ['c', 'cis', 'd', 'ees', 'e', 'f', 'fis', 'g', 'gis', 'a', 'bes', 'b']
    num_half_steps = round(12 * math.log2(freq / C4_frequency))
    note_name = note_names[num_half_steps % 12]
    octave = 4 + num_half_steps // 12
    if octave < 4:
        note_name += ("," * (4 - octave))
    else:
        note_name += ("'" * (octave - 4))
    # Set dynamic based on amplitude
    if amp >= 0.9:
        dynamic = "1"+"\\"+"ff"
    elif amp >= 0.7:
        dynamic = "1"+"\\"+"f"
    elif amp >= 0.5:
        dynamic = "1"+"\\"+"mf"
    elif amp >= 0.3:
        dynamic = "1"+"\\"+"mp"
    elif amp >= 0.1:
        dynamic = "1"+"\\"+"p"
    else:
        dynamic = "1"+"\\"+"pp"
    return note_name + dynamic

print('''
\score {  
\new Staff\with { instrumentName = "Strings A" \remove "Time_signature_engraver"} 
{ \cadenzaOn
''')
for i, frequency in enumerate(frequencies):
    closest_note = closest_note_name(frequency, amplitudes[i])
    print(f"{closest_note}")
print('''
}
}
''')
