import numpy as np
import gymnasium as gym
from gymnasium import spaces
import random
import chess

# Define the order of the pieces in the observation array
PIECES = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]

puzzles = [("3r4/4kppp/8/8/1P2P3/2R5/5PPP/6K1 b - - 1 1", -1), # 192
           ("2krr3/B1pb2pp/1p6/3p4/3Np1P1/7P/PK2B3/4R3 w - - 1 1", 1), # 249
           ("4r1k1/pp5p/6p1/3b1p2/3R4/BPp3P1/P1P2P1P/6K1 b - - 1 1", -1), # 281
           ("2brr1k1/2p1qp1p/p2p1bpB/1p6/1Q6/PBNP4/1PP2PPP/R3R1K1 b - - 1 1", -1), # 325
           ("r1b1r1k1/p4ppp/1p6/2pP4/5b2/P4N2/1P3PPP/R3R1K1", 1), # 365
           ("2B2k2/R1P2pp1/2R1p2p/3p4/1p1P4/1P2P3/5PPP/6K1 b - - 1 1", -1), # 404
           ("r2q2r1/pp1bkppQ/4p3/2bpP3/3n4/2N5/PP3PPP/R1B1K1NR w - - 1 1", 0.75), # 440
           ("2k2r2/p1p5/1pp1P2Q/2q5/8/8/1PP2PPP/3R2K1 b - - 1 1", -1), # 465
           ("1r2k1nr/pqpb1pp1/2pBp2p/3p4/3P4/2N3P1/PPPQPP1P/2KR1B1R b - - 1 1", -1), # 508
           ("5r2/8/2r2b1k/p7/8/2P5/PP3R2/6RK w - - 1 1", 1), # 589
           ("6k1/2b2p1p/p2q2pB/1p6/3R4/5Q1P/PPP2PP1/5RK1 b - - 1 1", -1), # 616
           ("qR1r4/P4k1p/6p1/8/8/6P1/5P1P/R5K1 b - - 1 1", -1), # idk
           ("2R5/1r4p1/n3pk1p/3pNp2/3p1P2/6P1/P6P/6K1 w - - 1 1", 0.75) # 780
           ]

mates = [("8/8/8/4k3/8/8/8/3QK3 w - - 1 1", 1),
         ("3qk3/8/8/8/8/2K5/8/8 b - - 1 1", -1),
         ("4k3/4r3/8/8/8/2K5/8/8 b - - 1 1", -1),
         ("8/8/7K/3k4/8/8/8/4R3 w - - 1 1", 1),
         ("8/8/8/7k/8/2K5/5r2/4r3 b - - 1 1", -1),
         ("1K6/3b4/k7/2b5/8/8/8/8 b - - 1 1", -1),
         ("1k6/3B4/K7/2B5/8/8/8/8 w - - 1 1", 1)
         ]

class ChessEnv(gym.Env):
    def __init__(self, render_mode="print"):
        self.metadata = {"render_modes": ["print","human", "rgb_array"], "fps": 1}
        self.model = None

        # The action will be a single continuous value representing the evaluation of the board
        self.action_space = spaces.Box(low=-1, high=1, shape=(1,))

        high = np.ones((8*8*12 + 1+4+16+2))
        high[-1] = 150
        # 12 pieces, turn, castles, en passant, 50 move, trefold
        self.observation_space = spaces.Box(low=np.zeros((8*8*12 + 1+4+16+2)), high=high, dtype=np.uint8)

        self.reset()

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def _get_obs(self):
        # Initialize the board representation # 8*8*12 + 1 + 4 + 16 + 2
        board_representation = np.zeros(791, dtype=np.uint8)

        # Get the bitboard representation of each piece type for each color
        for color in [chess.WHITE, chess.BLACK]:
            for piece in PIECES:
                # Get the bitboard for the current piece type and color
                bitboard = self.board.pieces(piece, color)

                # Add the bitstring to the board representation
                board_representation[color*6*64 + (piece-1)*64:color*6*64 + piece*64] = np.array(bitboard.tolist(), dtype=np.uint8)

        # Set the turn, castling rights, and en passant square
        board_representation[8*8*12] = 1 if self.board.turn == chess.WHITE else 0
        board_representation[8*8*12 + 1:8*8*12 + 5] = [
            int(self.board.has_kingside_castling_rights(chess.WHITE)),
            int(self.board.has_queenside_castling_rights(chess.WHITE)),
            int(self.board.has_kingside_castling_rights(chess.BLACK)),
            int(self.board.has_queenside_castling_rights(chess.BLACK))
        ]
        if self.board.ep_square is not None:
            board_representation[8*8*12 + 5 + self.board.ep_square - (16 if self.board.ep_square < 30 else 48)] = 1

        # Set the 50-move rule and threefold repetition counters
        board_representation[-2] = self.board.is_repetition()
        board_representation[-1] = self.board.halfmove_clock

        return board_representation
    
    def reset(self, seed=None, options=None):
        if random.randint(1,5) == 1:
            a = random.choice(puzzles+mates)
            self.board = chess.Board(a[0])
            self.last_eval = np.array([a[1]])
        else:
            self.board = chess.Board()
            self.last_eval = np.array([0])

        obs = self._get_obs()
        return obs, {}

    def step(self, action=None):
        moves = list(self.board.legal_moves)
        evalualuations = []

        for move in moves:
            self.board.push(move)
            obs = self._get_obs()
            evalualuation, _ = self.model.predict(obs)
            evalualuations.append((move, evalualuation))
            self.board.pop()

        bestmove = max(evalualuations, key=lambda x: x[1])
        self.board.push(bestmove[0])
        obs = self._get_obs()

        done = self.board.is_game_over()
        if done:
            result = self.board.result()
            # Assign reward based on the result
            if result == "1-0":
                self.last_reward = bestmove[1] - 1
            elif result == "0-1":
                self.last_reward = -1 - bestmove[1]
            else:  # The game is a draw
                self.last_reward = -abs(bestmove[1])
        else:
            self.last_reward = min(self.last_eval, bestmove[1]) - max(self.last_eval, bestmove[1])

        self.last_eval = bestmove[1]

        return obs, self.last_reward[0], done, False, {}
    
    def render(self):
        if self.render_mode == "print":# or self.render_mode == "rgb_array":
            return self._render_frame()

    def _render_frame(self):
        print(f"\n{self.last_eval}\n{self.board}")