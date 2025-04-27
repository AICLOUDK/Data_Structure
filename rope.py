class Rope:
    def __init__(self, string):
        self.string = string

    def cut_and_insert(self, i, j, k):
        cut_substring = self.string[i:j + 1]
        remaining_string = self.string[:i] + self.string[j + 1:]
        if k == 0:
            self.string = cut_substring + remaining_string
        else:
            self.string = remaining_string[:k] + cut_substring + remaining_string[k:]

def main():
    S = input().strip()
    rope = Rope(S)
    q = int(input().strip())
    for _ in range(q):
        i, j, k = map(int, input().strip().split())
        rope.cut_and_insert(i, j, k)
    print(rope.string)

if __name__ == "__main__":
    main()