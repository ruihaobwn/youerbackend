from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

path = "E:\youershuo\AA音频连读-93"
files = os.listdir(path)

for file in files:
    (filename, extension) = os.path.splitext(file)
    song = AudioSegment.from_file("{}\{}".format(path, file), format="mp3")
    chunks = split_on_silence(
        song,
        min_silence_len=400,
        silence_thresh=-48,
        keep_silence=500
    )
    for i, chunk in enumerate(chunks):
        print("Exporting {0}{1}.mp3".format(filename, i+1
                                            ))
        chunk.export(
            "E:\youershuo\剪切音频\{0}{1}.mp3".format(filename, i+1),
            format="mp3"
        )
