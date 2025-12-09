import sys

sys.path.append(r"C:\Users\kira_\OneDrive\Рабочий стол\python_labss\src")
from lib.io_txt_csv import read_text, write_csv

txt = read_text("data/lab04/input.txt")
write_csv([], "data/lab04/check.csv")
