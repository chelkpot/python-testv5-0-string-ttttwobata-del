# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    chars = input().split()
    for char in chars:
    print(f"Код символа {char} равен {ord(char)}")
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
