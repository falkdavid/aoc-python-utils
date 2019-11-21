import pytest

from src.machines import StateMachine

def test_fsm_example_automaton1():

    alph = "abc"
    tf = """1:2_3; 
            2:_44; 
            3:_4_"""
    start = "1"
    end = "4"

    fsm = StateMachine(alph, tf, start, end)
    assert fsm.check("ab")
    assert fsm.check("ac")
    assert fsm.check("cb")
    assert not fsm.check("bc")
    assert not fsm.check("aaaaa")

    assert fsm.check("abd")