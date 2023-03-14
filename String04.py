def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    a = 'False'
    if s == s.lower():
        a = 'True'
    return a
print(main('dfg fsdf'))