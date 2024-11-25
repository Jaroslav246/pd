import pandas as pd # type: ignore

songs = []

with open("./spotify.csv", "r", encoding='utf8') as csv_file:
    reader = csv_file.DictReader(csv_file)
    for line in reader:
        songs.append(line)


df = pd.DataFrame(songs)

df.to_json