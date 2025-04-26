import requests
from bs4 import BeautifulSoup

def decodeFromDoc(url):
    response = requests.get(url)
    bsoup = BeautifulSoup(response.text, 'html.parser')

    text_lines = bsoup.get_text(separator="\n").splitlines()
    clean_lines = [line.strip() for line in text_lines if line.strip()]
    data = [line for line in clean_lines if line.isdigit() or line in ['█', '░']]

    points = []
    for i in range(0, len(data) - 2, 3):
        try:
            x = int(data[i])
            char = data[i + 1]
            y = int(data[i + 2])
            points.append((x, y, char))
        except (ValueError, IndexError):
            continue

    if not points:
        print("No valid points found.")
        return

    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    for row in grid:
        print(''.join(row))

decodeFromDoc("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")