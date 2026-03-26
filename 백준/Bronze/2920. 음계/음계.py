notes = input().split()

if notes == sorted(notes):
    print('ascending')
elif notes == list(reversed(sorted(notes))):
    print('descending')
else:
    print('mixed')