import sys

def get_occurrences(pattern, text):
    return [i for i in range(len(text) - len(pattern) + 1) if text[i:i + len(pattern)] == pattern]

if __name__ == '__main__':
    pattern = sys.stdin.readline().rstrip()
    text = sys.stdin.readline().rstrip()
    print(' '.join(map(str, get_occurrences(pattern, text))))