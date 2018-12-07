import utils
import random
import numpy as np

class Agent:
    def learning_rate(self, state):
        C = 10
        return C/(C+self.N[state[0],state[1],state[2],state[3],state[4],state[5]])


    def __init__(self, actions, two_sided=False):
        self._actions = actions
        self._train = True
        self._x_bins = utils.X_BINS
        self._y_bins = utils.Y_BINS
        self._v_x = utils.V_X
        self._v_y = utils.V_Y
        self._paddle_locations = utils.PADDLE_LOCATIONS
        self._num_actions = utils.NUM_ACTIONS
        # Create the Q Table to work with
        self.Q = utils.create_q_table()
        self.N = utils.create_q_table()
        self.last_state = None
        self.games = 0

    def act(self, state, bounces, done, won):
        gamma = 0.6
        action = self._actions[0]
        disc_state = self.discretize(state)
        if self.train:
            if self.last_state:
                self.N[self.last_state[0],self.last_state[1],self.last_state[2],self.last_state[3],self.last_state[4],self.last_state[5]] += 1
                reward = bounces
                if done and bounces < 9:
                    reward = -1
                # if done:
                #
                # reward = -1
                # if bounces > 9:
                #     reward = 1
                alpha = self.learning_rate(self.last_state)
                best_next_action = self.best_next(disc_state)
                best_next_value = self.Q[disc_state[0],disc_state[1],disc_state[2],disc_state[3],disc_state[4],best_next_action]
                curr = self.Q[self.last_state[0],self.last_state[1],self.last_state[2],self.last_state[3],self.last_state[4],self.last_state[5]]
                self.Q[self.last_state[0],self.last_state[1],self.last_state[2],self.last_state[3],self.last_state[4],self.last_state[5]] += alpha * (reward + gamma*(best_next_value-curr))

            action = self.chose_next(disc_state)
            disc_state.append(action)
            self.last_state = disc_state
        else:
            action = self.best_next(state)
        return action
        # if done:
        #     self.games += 1
        # action = self._actions[0]
        # disc_state = self.discretize(state)
        # if self._train:
        #     self.N[self.last_state[0],self.last_state[1],self.last_state[2],self.last_state[3],self.last_state[4],self.last_state[5]] += 1
        #     alpha = learning_rate(self.last_state)
        #     if done:
        #         reward = -1
        #         if bounces > 9:
        #             reward = 1
        #         self.Q[self.last_state[0],self.last_state[1],self.last_state[2],self.last_state[3],self.last_state[4],self.last_state[5]] += reward + gamma*()
        #     action = random.choice(self._actions)
        #     disc_state.append(action)
        #     self.last_state = disc_state
        # else:
        #     options = self.Q[disc_state[0],disc_state[1],disc_state[2],disc_state[3],disc_state[4]]
        #     max_id = 0
        #     max_val = options[0]
        #     for i in range(1):
        #         if options[i+1]> max_val:
        #             max_val = options[i+1]
        #             max_id = i+1
        #     if max_id == 2:
        #         action = -1
        #     else:
        #         action = max_id
        # return action

    def chose_next(self, state):
        tuning = 250
        options = self.N[
        state[0],
        state[1],
        state[2],
        state[3],
        state[4]]
        if options.min() < tuning:
            return random.choice(self._actions)
        else:
            return self.best_next(state)

    def best_next(self, disc_state):
        options = self.Q[disc_state[0],disc_state[1],disc_state[2],disc_state[3],disc_state[4]]
        max_id = 0
        max_val = options[0]
        for i in range(1):
            if options[i+1]> max_val:
                max_val = options[i+1]
                max_id = i+1
        if max_id == 2:
            action = -1
        else:
            action = max_id
        return action

    def discretize(self, state):
        ball_x, ball_y, velocity_x, velocity_y, paddle_y = state;
        x_bin = y_bin = disc_v_x = disc_v_y = disc_pad = None
        x_bin = int(ball_x*self._x_bins) - 1
        y_bin = int(ball_y*self._y_bins) - 1
        if velocity_x > 0:
            disc_v_x = 1
        else:
            disc_v_x = 0
        if velocity_y >= 0.015:
            disc_v_y = 2
        elif velocity_y <= 0.015:
            disc_v_y = 1
        else:
            disc_v_y = 0
        disc_pad = int(paddle_y*self._paddle_locations) - 1
        # disc_pad = floor(self._paddle_locations * paddle_y / (1 - paddle_height))
        return [
            x_bin,
            y_bin,
            disc_v_x,
            disc_v_x,
            disc_pad
        ]


    def train(self):
        self._train = True

    def eval(self):
        self._train = False

    def save_model(self,model_path):
        # At the end of training save the trained model
        utils.save(model_path,self.Q)

    def load_model(self,model_path):
        # Load the trained model for evaluation
        self.Q = utils.load(model_path)
