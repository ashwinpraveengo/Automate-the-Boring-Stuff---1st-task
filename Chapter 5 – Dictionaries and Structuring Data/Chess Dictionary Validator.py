def isValidChessBoard(bd):
    spaces=[f'{r}{c}' for r in range(1, 9) for c in 'abcdefgh']
    valid_pcs={'king', 'queen', 'rook', 'bishop', 'knight', 'pawn'}
    count={'wk': 0, 'bk': 0, 'wp': 0, 'bp': 0, 'wt': 0, 'bt': 0}
    
    for pos, piece in bd.items():
        if pos not in spaces or len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pcs:
            return False
        clr, name= piece[0], piece[1:]
        count[f'{clr}t'] += 1
        if name=='king':
            count[f'{clr}k'] += 1
        elif name=='pawn':
            count[f'{clr}p'] += 1
    
    if count['wk'] != 1 or count['bk'] != 1 or count['wp'] > 8 or count['bp'] > 8 or count['wt'] > 16 or count['bt'] > 16:
        return False
    
    return True

board={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(board))  
