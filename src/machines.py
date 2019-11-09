import json

class StateMachine(object):

    EMPTY_STATE = '_'

    """
    Implements a simple and generic state machine.

    Each state is represented by a single character.

    Args:
        alph (string): A string of symbols representing the alphabet.

        tf (json-string/dict): The transition function. 
            Each key is a state and each value is a string of states 
            with the same length as the alphabet. When a symbol is fed
            into the automaton, the index of that symbol in the alphabet
            is used to determin the next state by looking at the
            state with the same index in the currents state value.
            The state '_' signals, that there is no transition for the 
            repective symbol. 

        start (char): The starting state represented by a single character.

        end (string): The end state(s). Can be a single character.

    Example:

        The following automaton accepts the words 'ab', 'ac', and 'cb'.

        alph = "abc"
        tf = {
            '1':"2_3"
            '2':"_44"
            '3':"_4_"
        }
    """
    def __init__(self, alph, tf, start, end=""):
        self.alph = alph
        self.start = start
        self.end = end
        
        self.state = start
        try:
            tf_dict = json.loads(tf)
        except:
            tf_dict = tf

        self.tf = {k:{alph[i]:v[i] for i in range(len(alph))} for k,v in tf_dict.items()}
        
    def feed(self, word):
        for c in word:
            if self.state in self.tf:
                if c in self.tf[self.state]:
                    new_state = self.tf[self.state][c]
                    if not new_state == self.EMPTY_STATE:
                        self.state = new_state
        return self.state

    def check(self, word):
        self.feed(word)
        is_end = self.state in self.end
        self.reset()
        return is_end

    def reset(self):
        self.state = self.start


class TuringMachine(object):

    def __init__(self):
        pass

