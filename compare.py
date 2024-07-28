import csv

from libzim.reader import Archive

june = Archive("zims/wikipedia_ab_all_maxi_2024-06.zim")
july = Archive("zims/wikipedia_ab_all_maxi_2024-07.zim")

path_to_sizes = {}

for i in range(0, june.all_entry_count):
  entry = june._get_entry_by_id(i)
  path_to_sizes[entry.path] = [entry.get_item().size]

for i in range(0, july.all_entry_count):
  entry = july._get_entry_by_id(i)
  if entry.path in path_to_sizes:
    path_to_sizes[entry.path].append(entry.get_item().size)
  else:
    path_to_sizes[entry.path] = [None, entry.get_item().size]

for entry, sizes in path_to_sizes.items():
  if len(sizes) == 1:
    sizes.append(None)

with open('comparison.tsv', 'w', newline='') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter='\t')
  sorted_keys = sorted(path_to_sizes.keys())
  csvwriter.writerow(('path', 'june', 'july'))
  for key in sorted_keys:
    csvwriter.writerow((key, *path_to_sizes[key]))
