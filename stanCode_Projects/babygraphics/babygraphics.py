"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = 0
    long = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)    # Automatically calculate the x-axis distance between the point and the point
    time = 0
    for i in YEARS:
        if i == year_index:

            x_coordinate = GRAPH_MARGIN_SIZE+time*long
        time += 1


    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE,2,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,2)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)


    for i in YEARS:
        x = get_x_coordinate(CANVAS_WIDTH,i)
        canvas.create_line(x, 2, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT, text=str(i), anchor=tkinter.SW)



    # Write your code below this line
    #################################


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    for i in range(len(lookup_names)):

        old_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # Set the first Y axis position
        old_x = GRAPH_MARGIN_SIZE                     # Set the first X axis position

        color_time = i%4              # Use remainder to make the number between 0 and 3
        color= COLORS[color_time]
        time = 0
        for j in range(len(YEARS)):
            x=get_x_coordinate(CANVAS_WIDTH,YEARS[j])
            time += 1


            if str(YEARS[j]) in name_data[lookup_names[i]]:

                rank =int(name_data[lookup_names[i]][str(YEARS[j])])
                if time ==1:
                    old_rank = rank

                if rank < CANVAS_HEIGHT-GRAPH_MARGIN_SIZE:
                    text = lookup_names[i] + str(rank)
                    canvas.create_text(x + TEXT_DX, rank + 10, text=text, anchor=tkinter.SW)
                    canvas.create_line(old_x, old_rank, x, rank, width=LINE_WIDTH,fill=color)
                else:
                    rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x, rank, text='*')
                    canvas.create_line(old_x, old_rank, x, rank, width=LINE_WIDTH,fill=color)
            else:
                rank = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_text(x,rank,text='*')
                canvas.create_line(old_x, old_rank, x, rank,width=LINE_WIDTH,fill=color)

            old_rank= rank         # Record the y-axis position of the previous point
            old_x = x              # Record the x-axis position of the previous point





            # canvas.create_line(x, old_rank + GRAPH_MARGIN_SIZE, x, rank + GRAPH_MARGIN_SIZE)




            old_rank = rank






    # Write your code below this line
    #################################


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)


    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
