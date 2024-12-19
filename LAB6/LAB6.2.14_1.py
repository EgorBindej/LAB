
for hours in range(3, 25, 3):
    
    divisions = hours // 3
    # Количество клеток после делений
    cells = initial_cells * (2 ** divisions)
    print(f"Через {hours} часа(ов) будет {cells} клетки(ок)")
