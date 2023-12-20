import random 
import pygame #imports pygame module 
pygame.font.init() #initiates pygame fonts 

card_dict = {0: 54, 1: 92, 2: 130, 3: 168, 4: 206, 5: 244, 6: 282, 7: 320, 8: 358,
                    9: 396, 10: 434} #key = "card number", value = x-coordinate of respective card sprite on sprite sheet

FONT = pygame.font.SysFont("Verdana", 30) #sets default text font and size for text in game

class CardPile:
    def __init__(self):
        self.items = []
           
    def add_top(self, item):
        return self.items.insert(0, item)
        
    
    def add_bottom(self, item):
        return self.items.insert(self.size(), item)

    def remove_top(self):
        return self.items.pop(0)
    
    def remove_bottom(self):
        return self.items.pop(self.size()-1)
 
    def size(self):
        return len(self.items)
    
    def peek_top(self):
        if self.items != []:
            return self.items[0]
    
    def peek_bottom(self):
        if self.items != []:
            return self.items[self.size()-1]
        return 0
   
    def print_all(self, index):
        card_x = 50 #x position of first card in pile on window
        card_y = 10 #y position of pile 0 on window
        pile_num = FONT.render("{}".format(index), True, "white") #creates text surface to be displayed
        if self.size() > 0:
            if index > 0:
                card_y = index * 80 #sets pile y position on window 
                window.blit(pile_num, (10,card_y)) #displays pile number in front of cards
                for card in self.items: #iterates through each card within the pile 
                    window.blit(SpriteSheet("cards.png").card_sprite(card_dict[card]), (card_x,card_y)) #displays current card from list
                    card_x += 60 #increments x coordinate for spacing between every card
                 

            else:
                top_card = self.items[0] 
                window.blit(pile_num, (10,10)) #displays pile number in front of each card pile
                window.blit(SpriteSheet("cards.png").card_sprite(card_dict[top_card]), (card_x, card_y)) #displays first flipped card on window
                card_x = 90 #sets x coordinate for successive card relative to top card in pile
                for card in range(len(self.items)-1):
                    window.blit(SpriteSheet("cards.png").card_sprite(card_dict[0]), (card_x, card_y))
                    card_x += 40 #increments x coordinate for spacing between every card

        pygame.display.update() #updates window with new card display every time function is called
        


class Solitaire:
    #chooses the card pile sequence in random 
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(cards)
    def __init__(self, cards = cards ):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])
        self.move_number = 1
            

    def get_pile(self, i):
        return self.piles[i]
    
    def display(self):
        for i in range(self.num_piles):
            current_pile = self.get_pile(i)
            current_pile.print_all(i)



    def move(self, p1, p2):
        draw_backgorund() #updates background display with every move  
        p1_size = self.get_pile(p1).size()
        p2_size = self.get_pile(p2).size()
        if p1 >= 0 and p2 >= 0 and p1 < self.num_piles and p2 < self.num_piles:
            if p1_size != 0:
                if p1 == 0 and p2 == 0:
                    top_card = self.get_pile(0).peek_top()
                    self.get_pile(0).remove_top()
                    self.get_pile(0).add_bottom(top_card)
                    self.display() 
            
                elif p1 == 0 and p2 > 0:
                    top_card = self.get_pile(0).peek_top()
                    if p2_size > 0:
                        bottom_card = self.get_pile(p2).peek_bottom()
                        if top_card == bottom_card-1:
                            self.get_pile(0).remove_top()
                            self.get_pile(p2).add_bottom(top_card)
                    elif p2_size == 0:
                        self.get_pile(0).remove_top()
                        self.get_pile(p2).add_bottom(top_card)
                    self.display()
            
                elif p1 > 0 and p2 > 0:
                    if p2_size > 0:
                        if self.get_pile(p1).peek_top() == self.get_pile(p2).peek_bottom()-1:
                            for card in self.piles[p1].items:
                                self.get_pile(p2).add_bottom(card)
                            self.piles[p1].items = []
                        self.display()

    def play(self):
        print("********************** NEW GAME *****************************")
        while self.move_number <= self.max_num_moves and not self.is_complete() and not self.no_more_moves():
            self.display()
            print("Round", self.move_number, "out of", self.max_num_moves, end = ": ")
            pile1 = int(input("Move from pile no.: "))
            print("Round", self.move_number, "out of", self.max_num_moves, end = ": ")
            pile2 = int(input("Move to pile no.: "))
            if pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles and pile2 < self.num_piles:
                self.move(pile1, pile2)
            self.move_number += 1

        

    def is_complete(self):
        cardpiles = 0
        if self.get_pile(0).items == []:
            for i in range(self.num_piles):
                if self.get_pile(i).items != []:
                    cardpiles += 1
                    index = i
            if cardpiles == 1:
                return self.get_pile(index).items == sorted(self.get_pile(index).items, reverse=True)    
        return False
    
    def no_more_moves(self):
        #iterates through all of the card piles to check if there are any more valid moves
        for curr_pile in range(1, self.num_piles): #iterates through each piles except for first pile
            current_pile = self.get_pile(curr_pile)
            for comp_pile in range(1, self.num_piles):
                compare_pile = self.get_pile(comp_pile)
            if current_pile != compare_pile:
                if self.get_pile(0).peek_top() == current_pile.peek_bottom()-1 or compare_pile.items == [] or current_pile.items == []:
                    return False
                elif current_pile.peek_top() == compare_pile.peek_bottom()-1 or compare_pile.peek_top() == current_pile.peek_bottom()-1:
                    return False
        pygame.time.delay(1000) #delays card window - game do not close straight away if no more moves 
        return True 
    

#sets window display - background image, size 
window_height, window_width = 300, 650
window = pygame.display.set_mode((window_width, window_height))
background = pygame.transform.scale(pygame.image.load("background .png"), (window_width, window_height)) #imports background image


    
def draw_backgorund():
    pygame.display.set_caption("CS130 Solitaire") #set up display window
    window.blit(background, (0,0)) #sets window background as imported background image
    pygame.display.update()


    
#imports spritesheet and defines spritesheet class to access spritesheet throughout
class SpriteSheet:
    def __init__(self, filename):
        self.filename = filename 
        self.spritesheet = pygame.image.load(filename).convert()

    def card_sprite(self, x, y = 221, w = 31, h = 44): 
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0)) #sets card sprite backgound as transparent
        sprite.blit(self.spritesheet, (0,0), (x, y, w, h)) #crops card sprite and displays card sprite on screen
        return sprite
    




def main():
    pygame.init() #initiates pygame module 
    game = Solitaire() 
    draw_backgorund()
    #keeps game window open until user quits window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            break
    game.play()
    if game.is_complete():
        win_surface = FONT.render(f"You Win in {game.move_number-1} steps!", False, "white")
        window.blit(win_surface, (150, 10)) #displays "You win" text on screen
    else:
        if game.no_more_moves():
            no_more_moves_surface = FONT.render("No More Moves!", False, "white")
            window.blit(no_more_moves_surface, (350, 100))
        lost_surface = FONT.render("You Lose!", False, "white")
        window.blit(lost_surface, (350, 150))  #displays "you lost" text on screen
    pygame.display.update() #updates window displya with text 
    pygame.time.delay(1500) #delays windown closing - for player to read text 
    pygame.quit() #close window 




        
main() 
