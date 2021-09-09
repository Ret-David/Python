# David Martinez
# Print the following patterns using loop.
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

# stars = int(input("How many stars to a side would you like? "))
stars = 5                               # Set number of stars, could use input method.
spaces = stars -1                       # Set number of spaces on each row.

for x in range(0, stars):               # Should loop through 5 times.

# Add spaces first, then stars, row by row
        for y in range(0, spaces):      # Should loop through 4 times.
                print(end=" ")          # Insert 4 spaces on 1st row, then 3 on 2nd, and so on...
        
        spaces = spaces -1              # Decrement the space count from top. 4, 3, 2, 1, None
                
        for y in range(0, x + 1):       # Must use x in range, not stars, or you get 5 rows of 5 stars
                                        #   Must have +1 or will only do 4 rows since 0 is first
                print("* ", end="")     # Keeps stars on one row, shows 1 row of 5 stars.

        print("\r")                     # Carriage return after each row
