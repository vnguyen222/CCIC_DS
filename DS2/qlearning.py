import random


class QLearning:
    ###############
    ### Methods ###
    ###############
    __bellman_equation = lambda self, state, old_q, next_q, alpha=0.5, gamma=0.5 : (1 - alpha) * old_q + alpha * (self.REWARDS[state[0]][state[1]] + gamma * next_q)    

    def __get_possible_actions(self, row_index, column_index):    
        possible = {"up": False, "down": False, "right": False, "left": False}
        #possible = {"up": row_index != 0, "down": row_index != len(MAZE)-1, "right": column_index != 0, "left": column_index != len(MAZE[0])-1}    
        dir_functions = {"up": (lambda: True if self.MAZE[row_index-1][column_index] == 1 and not row_index == 0 else False),
                        "down": (lambda: True if self.MAZE[row_index+1][column_index] == 1 and not row_index == len(self.MAZE)-1 else False),
                        "right": (lambda: True if self.MAZE[row_index][column_index+1] == 1 and not column_index == len(self.MAZE[row_index])-1 else False),
                        "left": (lambda: True if self.MAZE[row_index][column_index-1] == 1 and not column_index == 0 else False)}
        for dir,funct in dir_functions.items():
            try:
                possible[dir] = funct()
            except: pass

        return possible
    

    def __get_next_move(self, dictionary):
        true_keys = [key for key, value in dictionary.items() if value]
        if not true_keys:
            return None
        return random.choice(true_keys)
    

    def __iterate_to_next_move(current_position, next_move):
        '''
        current_position: tuple (row_index, column_index)
        '''
        new_pos = [current_position[0], current_position[1]]
        match next_move:
            case "up":
                new_pos[0] -= 1
            case "down":
                new_pos[0] += 1
            case "right":
                new_pos[1] += 1
            case "left":
                new_pos[1] -= 1
            case _:
                raise Exception("No possible moves at ${current_position}")
        
        return tuple(new_pos)

    def __get_next_move_qtable(self, current_state, dir):
        '''
        current_state: A tuple containing the coordinates to the old state, (row_index, column_index)
        '''

        next_state = list(current_state)
        match dir:
            case "up":
                next_state[0] = current_state[0] - 1
                next_state[1] = current_state[1]
            case "down":
                next_state[0] = current_state[0] + 1
                next_state[1] = current_state[1]
            case "left":
                next_state[0] = current_state[0]
                next_state[1] = current_state[1] - 1
            case "right":
                next_state[0] = current_state[0]
                next_state[1] = current_state[1] + 1
            case _:
                raise Exception("Direction is invalid")
        next_state = tuple(next_state)
            
        # Find the entry in the q_table that contains the new state
        return self.q_table[next_state[0]][next_state[1]]
        
    # Create a state table
    def __init_state_table(self, maze):
        qtable = []
        for row in range(len(maze)):
            qtable_row = []
            for column in range(len(maze[row])):
                qtable_row.append(self.QEntry((row, column)))
            qtable.append(qtable_row)
        return qtable

    # QEntry: stores the data of every position in the maze
    # state (position), up, down, left, right
    class QEntry:
        def __init__(self, state):
            self.state = state
            self.up = 0
            self.down = 0
            self.left = 0
            self.right = 0
        
        def get_state(self):
            return self.state
        def get_positions(self):
            return {"up": self.up, "down": self.down, "left": self.left, "right": self.right}

        def add_to_positions(self, increment, position):
            match position:
                case "up":
                    self.up += increment
                case "down":
                    self.down += increment
                case "right":
                    self.right += increment
                case "left":
                    self.left += increment
                case _:
                    raise Exception("No possible moves at ${current_position}")
    

    # DEBUGGING PURPOSES #
    def get_state_table(self):
        return self.q_table



    ######################
    ### Public Methods ###
    ######################
    # Constructor
    def __init__(self, maze, rewards):
        """
        maze: the matrix (puzzle) for the Q-learning algorithm to solve
        """
        self.MAZE = maze
        self.REWARDS = rewards
        self.q_table = self.__init_state_table(self.MAZE)

    def predict(self, starting_pos, end_pos, alpha = 0.5, gamma = 0.5, episodes = 300):
        """
        starting_pos: the starting position within the matrix modeled as (row index, column index)
        end_pos: the ending position within the matrix modeled as (row index, column index)
        """
        self.STARTING_POS = starting_pos
        self.END_POS = end_pos

        # Start and end position indexes
        start_row_index, start_column_index = self.STARTING_POS[0],self.STARTING_POS[1]
        end_row_index, end_column_index = self.END_POS[0],self.END_POS[1]

        # Store where the current position is
        current_row_index, current_column_index = start_row_index, start_column_index

        # Iterations (episodes)
        for loop in range(0, episodes):
            # Loop and find the path to the end (an episode)
            while True:
                # Get current state
                entry = self.q_table[current_row_index][current_column_index]
                state = entry.get_state()
                state_q_positions = entry.get_positions()
                possible_movements = self.__get_possible_actions(state[0], state[1])

                # Get next move
                next_move = self.__get_next_move(possible_movements)
                # display(str(state) + str(state_q_positions) + str(possible_movements) + " " + str(next_move))

                # display(state_q_positions)
                # Using Bellman equation to find the Q-values
                old = state_q_positions[next_move]
                next_q_obj = self.__get_next_move_qtable(state, next_move)
                next_q = max(list(next_q_obj.get_positions().values()))
                # print(str(next_q_obj.get_state()) + " old: {} next_q: {}".format(old, next_q))
                # display(bellman_equation(state, old, next_q))
                # Update the Q-value in the Q-table
                self.q_table[state[0]][state[1]].add_to_positions(self.__bellman_equation(state, old, next_q), next_move)

                # Update for the next iteration
                next_state = next_q_obj.get_state()
                current_row_index, current_column_index = next_state[0], next_state[1]

                if current_row_index == end_row_index and current_column_index == end_column_index:
                    break;

        return self.q_table



class Visualize:
    def visualize_maze(maze, starting_pos, end_pos):
        # Print visualization
        for row in range(0, len(maze)):
            print("| ", end="")
            for col in range(0, len(maze[row])):
                if row == starting_pos[0] and col == starting_pos[1]:
                    print("•", end=" | ")
                elif row == end_pos[0] and col == end_pos[1]:
                    print("★", end=" | ")
                elif maze[row][col] == 0:
                    print("█", end=" | ")
                else:
                    print(" ", end=" | ")
            print()


    def visualize_q_states(q_table):
        # Visualize Q-Table
        q_table_optimal = []
        for row in q_table:
            q_table_optimal_row = []
            for column in row:
                pos = column.get_positions()
                q_table_optimal_row.append(" " if max(pos.values()) == 0 else max(pos, key=pos.get))
            q_table_optimal.append(q_table_optimal_row)

        # Print visualization
        for row in q_table_optimal:
            print("| ", end="")
            for pos in row:
                if pos == " ":
                    print("█".ljust(5, "█"), end=" | ")
                else:
                    print(pos.ljust(5, " "), end=" | ")
            print()