#! python3
# mouseNow.py - Displays the mouse cursor's current position.
print(positionStr, end='')
print('\b' * len(positionStr), end='', flush=True)
