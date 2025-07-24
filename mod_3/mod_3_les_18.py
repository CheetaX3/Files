from abc import ABC, abstractmethod

class ChessBoard:
    def __init__(self):
        # 8x8 доска, заполняем None
        self.size = 8
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
    
    def is_within_board(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def move_piece(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if not self.is_within_board(from_row, from_col):
            print('Исходная клетка за пределами доски.')
            return

        if not self.is_within_board(to_row, to_col):
            print('Клетка за пределами доски.')
            return

        piece = self.board[from_row][from_col]
        if piece is None:
            print('На исходной клетке нет фигуры.')
            return

        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None

    def display(self):
            columns = [' a', ' b', ' c', ' d', ' e', ' f', ' g', ' h']
            print()  # пустая строка сверху

            for row_idx, row in enumerate(self.board):
                # Номера рядов с 8 сверху до 1 снизу — если надо, можно сделать по-другому.
                # Сейчас подписываем слева номера с 8 (вверху) до 1 (внизу):
                print(f"{self.size - row_idx} ", end='')  # нумерация рядов слева

                print(' '.join(str(piece) if piece else '__' for piece in row))

            # Подпись колонок снизу
            print(' ' + ' '.join(columns))
            print('')  # пустая строка после доски

class ChessPiece(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __str__(self):
        return f'{self.color[0]}{self.name[0]}'

    @abstractmethod
    def get_possible_moves(self, position, board):
        pass

    def get_moves_in_directions(self, position, board, directions):
        row, col = position
        moves = []
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while board.is_within_board(new_row, new_col):
                target = board.board[new_row][new_col]
                if target is None:
                    moves.append((new_row, new_col))
                else:
                    if target.color != self.color:
                        moves.append((new_row, new_col))  # взять фигуру
                    break  # уперся в фигуру
                new_row += dr
                new_col += dc

        return moves

class Pawn(ChessPiece):
    def get_possible_moves(self, position, board):
        row, col = position
        moves = []
        direction = -1 if self.color == 'White' else 1

        # Прямой ход
        if 0 <= row + direction < board.size:
            if board.board[row + direction][col] is None:
                moves.append((row + direction, col))

        # Взятие по диагонали
        for dc in [-1, 1]:
            new_row = row + direction
            new_col = col + dc
            if board.is_within_board(new_row, new_col):
                target = board.board[new_row][new_col]
                if target is not None and target.color != self.color:
                    moves.append((new_row, new_col))

        return moves

class Bishop(ChessPiece):
    def get_possible_moves(self, position, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self.get_moves_in_directions(position, board, directions)
        
class Queen(ChessPiece):
    def get_possible_moves(self, position, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1,0), (1,0), (0,-1), (0,1)]
        return self.get_moves_in_directions(position, board, directions)

board = ChessBoard()

pawn1 = Pawn('pawn', 'White')
board.board[6][1] = pawn1
board.display()

print(pawn1.get_possible_moves((6, 1), board))

board.move_piece((6, 1), (4, 1))  # Белая пешка с b2 на b4
pawn2 = Pawn('pawn', 'Black')
board.board[3][0] = pawn2
board.display()

print(pawn1.get_possible_moves((4, 1), board))