import csv
import sys

from libzim.reader import Archive


def output_tsv(left_path, right_path):
  left = Archive(left_path)
  right = Archive(right_path)

  path_to_sizes = {}

  for i in range(0, left.all_entry_count):
    entry = left._get_entry_by_id(i)
    path_to_sizes[entry.path] = [entry.get_item().size]

  for i in range(0, right.all_entry_count):
    entry = right._get_entry_by_id(i)
    if entry.path in path_to_sizes:
      path_to_sizes[entry.path].append(entry.get_item().size)
    else:
      path_to_sizes[entry.path] = [None, entry.get_item().size]

  for entry, sizes in path_to_sizes.items():
    if len(sizes) == 1:
      sizes.append(None)

  csvwriter = csv.writer(sys.stdout, delimiter='\t')
  sorted_keys = sorted(path_to_sizes.keys())
  csvwriter.writerow(('path', 'left', 'right'))
  for key in sorted_keys:
    csvwriter.writerow((key, *path_to_sizes[key]))


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('Usage: python compare.py left_zim right_zim')
    sys.exit(1)

  output_tsv(sys.argv[1], sys.argv[2])
