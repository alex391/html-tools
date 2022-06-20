#!/usr/bin/env python3
# This program converts newline-seperated (as coppied from google docs) tables
# into a plain, validating HTML table
# Written by Alex Leute - 6/20/2022
# Known issues: 
# - Unicode is broken on Windows (this is IMO a Windows "feature" but fix it if you want)
# - Newlines in cells will break it (no good way to tell) so merge (separate with <br>) beforehand

import sys

TAB = "  " # set tab to what you want your tab to be, eg "  " or "\t"

def main():
    columns = 0
    if sys.stdout.isatty(): # Don't print stuff unless we are outputting to a terminal
        columns = int(input("How many columns does your table have?\n"))
        print ("Input an end of file (ctrl + d on Unix, ctrl + z, <enter> on Windows) to quit and print table html")
    else:
        columns = columns = int(input())
    assert(columns > 0)
    i = 0
    buffer =                \
    "<table>\n" +           \
    TAB + "<thead>\n" +     \
    TAB + TAB + "<tr>\n"
    for line in sys.stdin:
        line = line.rstrip('\n')
        if i < columns: #if we are in the "header"
            buffer = buffer + 3 * TAB + "<th>" + line + "</th>\n"
        elif i == columns: # if we are just one after the header
            buffer = buffer +                                       \
                     TAB + TAB + "</tr>\n" +                        \
                     TAB + "</thead>\n" +                           \
                     TAB + "<tbody>\n" +                            \
                     TAB + TAB + "<tr>\n" +                         \
                     TAB + TAB + TAB + "<td>" + line + "</td>\n"
        elif i % columns == 0: #if it's the first one in it's row, end the previous row and start the new one
            buffer = buffer +                                       \
                     TAB + TAB + "</tr>\n" +                        \
                     TAB + TAB + "<tr>\n"  +                        \
                     TAB + TAB + TAB + "<td>" + line + "</td>\n"
        else:
            buffer = buffer +                                       \
                     TAB + TAB + TAB + "<td>" + line + "</td>\n"
        i = i + 1
    print(buffer, TAB, TAB, "</tr>\n", TAB, "</tbody>\n</table>\n", sep="", end="")
            

main()
