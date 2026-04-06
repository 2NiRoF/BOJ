import sys

capacity = sys.stdin.readline()
request = sys.stdin.readline()

if len(capacity) < len(request):
    print("no")
else:
    print("go")