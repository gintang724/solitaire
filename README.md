Given this was based on an in-course assignment, the Solitaire class was given. And the GUI was produced as a creative extension to the program.
In terms of adjustments to the code itself, the card order is to be randomly generated for every game, so no predetermined list of cards is needed to play the game. 
Because of the randomly generated card orders, an implication rised such that there become instances where players will run out of moves because there are no more valid moves; 
thus, an additional method within the Solitaire class was added - no_more_moves() .

No_more_move() method:
The method is a conditional function that iterates through each pile except for pile 0 and checks to see if there are any valid moves left 
by comparing the top cards of the pile to the bottom card to the other piles other than itself as well as checking to see whether any piles that are empty.
In the case that there are valid moves such that the top card is one less than the bottom card of the existing piles or there is an empty pile, 
the method will return False, and the player can continue to play else, the method returns True, and the while loop within the play() method breaks. 

Randomly generated starting card pile:
Using the Random module, the list of numbers from 1-10 could be rearranged randomly. Which produces a random sequence of cards for the initial pile for every game.

GUI implementation:
The graphics were implemented using the PyGame module.
Firstly,required variables of window height, width, background file and window name to generate the PyGame window itself that opens which code is run were set. 
Then the function called draw_background() was added to use the window variables to generate a window by establishing window size and drawing the background image to the window by using blit().
Then a spritesheet class was defined which imported and loaded an image with card sprites. 

Within the SpriteSheet class there are the initialisers, filename - name of spritesheet file and spritesheet which loads the file into the class.
And the method card_sprite() has 4 parameters, x-coordinate, y coordinate, width and height. Then the size of the cards were established to be 31 x 44 px. 
That was set as the default parameter for width and height. As only the last row of spade cards were to be cropped, the y-coordinate was defaulted to 221.
- the measurements were taken using an online pixel ruler. The card_sprite() method crops the card based on x-coordinate and converts it into a drawable surface to the window. 

In order to display the cards with every move, 
the CardPile.print_all() method was modified such that each number within the pile list would produce a corresponding card sprite using the SpriteSheet.card_sprite() method 
by using an dictionary where the keys are the numbers (1-10) and value being the x-coordinates of the card corresponding to the numbers on the spritesheet. 
Thus instead of printing the cards as numbers when print_all() is called, the method draws the cards on the screen. 
To ensure that the display changes with every move - so the display is accurate with where the cards are moved to the background is updated every time print_all() is called.

To run the game on the window, a main() function is created which keeps the window open unless the player finishes the game or quits the window. 
And Solitaire.game() method is called to play the game. 
Once the game finishes, the ending text drawn on the screen is based on the conditions of is_complete(), no_more_moves() and move_number. 
(move_number was changed to an instance variable within the Solitaire() class so that it could be called in both the game() method and in the main() (not within the Solitaire class where play() is) for ending message). 

It was found that upon the game ending, the program would close the window abruptly as the method quit() was run at the end of the game 
Thus time delays were added at the end of the no_more_moves() method and after the ending texts were drawn so the game does not quit abruptly 
and the player gets to read the text drawn. 

The game is played the same way within the terminal but displayed within the Pygame window. 
