import sys


def solve(M, slices):
  # Maybe smarter
  slices = list(zip(slices, range(len(slices))))
  indices = []
  sizes = []
  k = 0
  for size, index in slices[::-1]:
    k += size
    sizes.append(size)
    indices.append(index)
    print(f"k={k} - added {size}, {index}")
    if k > M:
      d = k - M
      print(f"\t{k} > {M} (by {d})")
      for i,e in enumerate(sizes[::-1]):
        if e > d:
          i = len(sizes)-i-1
          break
      #i = sizes.index(max(sizes))
      S = sizes[i]
      I = indices[i]
      sizes.remove(S)
      indices.remove(I)
      k -= S
      print(f"\tRemoved {S}, {I} - new k = {k}")
  return len(sizes), sorted(indices)


if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename) as f:
    data = f.readlines()
  for i, line in enumerate(data):
    l = line.strip().split(' ')
    if i:
      ns = l
    else:
      M, N = l
  n_slices, _i = solve(int(M), list(map(int, ns)))
  score = 0
  ns = list(map(int, ns))
  for i in _i:
    score += ns[i]
  print(f"Final score of {score} with {n_slices} pizzas")
  out = filename.split('_')[0] + '.out'
  with open(out, 'w') as f:
    f.write(f'{n_slices}\n')
    for e in _i[:-1]:
      f.write(f'{e} ')
    f.write(str(_i[-1]))


