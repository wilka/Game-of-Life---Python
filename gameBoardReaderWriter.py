from gameBoard import GameBoard
from point import Point
from tkinter import filedialog
import os
import tkinter
    
root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def write_board(board):
    file_name = filedialog.asksaveasfilename()
    if not file_name:
        return

    with open(file_name, "w") as file:
        file.write(f"{board.grid_size[0]}, {board.grid_size[1]}\n" )
        for cell in board.cells():
            file.writelines(f"{cell.position.x}, {cell.position.y}, {cell.is_alive}\n")



def read_board():
    file_name = filedialog.askopenfilename()
    if not file_name:
        return
    
    with open(file_name, "r") as file:
        line = file.readline()
        split_line = line.split(",")
        width = int(split_line[0].strip())
        height = int(split_line[1].strip())
        board = GameBoard((width, height))

        for line in file:
            split_line = line.split(",")
            x = int(split_line[0].strip())
            y = int(split_line[1].strip())
            is_alive = split_line[2].strip() == "True"

            board.set_cell(Point(x, y), is_alive)

    return board
