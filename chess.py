from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        o
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        if not self.is_position_on_board(position): #kontrola platnosti aktuální pozice
            raise ValueError(f"Position {position} is out of bounds.")
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        if self.color == 'white':
            moves = [(row + 1, col)] #tah dopředu pro bílého pěšce
        elif self.color == 'black':
            moves = [(row - 1, col)] #tah dopředu pro černého pěšce
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
        
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        final_moves = []
        
        for i in range(1, 8):
            
            moves = [
                (row + i, col + i),   #vpravo nahoru
                (row + i, col - i),   #vlevo nahoru
                (row - i, col + i),   #vpravo dolů
                (row - i, col - i)    #vlevo dolů
            ]
            
            for move in moves:
                if self.is_position_on_board(move):
                    final_moves.append(move)
        
        return final_moves
    
    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        final_moves = []
        
        for i in range(1, 8):
            moves = [
                (row + i, col), #nahoru
                (row - i, col), #dolů
                (row, col + i), #vpravo
                (row, col - i)  #vlevo
            ]
            for move in moves:
                if self.is_position_on_board(move):
                    final_moves.append(move)
        return final_moves
    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'

class Queen(Bishop, Rook): #kombinace střelce a věže
    def possible_moves(self):
        bishop_moves = Bishop.possible_moves(self)
        rook_moves = Rook.possible_moves(self)
        return bishop_moves + rook_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'



class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Pawn("white", (8, 1))
    print(piece)
    print(piece.possible_moves())