# tic_tac_toe_AI_game
Franklin Neves
Kevin Tran
Valerie Benedit

This code uses a typical 3 by 3 tic-tac-toe board game. Each square is represented by a number in between 1-9. The first row are the numbers 1-3, the second row are 4-6, lastly 7-9.  We used a winner board that illustrates the different combinations that determine a win. This winner board is used to check. 

Next, we created a minimax function which attempts to choose the best option for player “O” to win the game. The algorithm has two parts. The first part is when it’s max turn; max’s turn looks for the maximum score available to make it next, efficient move. The second part is min’s turn; min looks for the minimum score available to make it next, efficient move. This minimax algorithm is incorporated to the AI function for the AI to play against a person. 

Third, we created a play_game( ) function which allows the user to interact with the playing board and to play against the AI. This function also defines a move in the game and keeps track of the moves made. 

