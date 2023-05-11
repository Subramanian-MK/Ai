def search(pat, txt):
    m = len(pat)
    n = len(txt)
    indices = []
    for i in range(n - m + 1):
        for j in range(m):
            if txt[i + j] != pat[j]:
                break
            if j == m - 1:
                indices.append(i)
    return indices

txt = input("Enter the text: ")
pat = input("Enter the pattern to search: ")
indices = search(pat, txt)
print("Pattern found at indices:", indices)
