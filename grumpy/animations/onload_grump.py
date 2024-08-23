import os
import sys
import time

frames = [
# Initial frame
"""
 /\_/\  
(  -_-)
 (   ) 
  | |  
""",
# Blink
"""
 /\_/\  
(  o_o)
 (   ) 
  | |  
""",
# Back to normal
"""
 /\_/\  
(  -_-)
 (   ) 
  | |  
""",
# Blink again
"""
 /\_/\  
(  o_o)
 (   ) 
  | |  
""",
    # Back to normal
"""
 /\_/\  
(  -_-)
 (   ) 
  | |  
""",
# Eyes before yawn
"""
 /\_/\  
(  O_O)
 (   ) 
  | |  
""",
# Back to normal
"""
 /\_/\  
(  -_-)
 (   ) 
  | |  
""",
# Yawn
"""
 /\_/\  
(  -.-)
 (   ) 
  | |  
""",
# Yawn bigger
"""
 /\_/\  
(  -o-)
 (   ) 
  | |  
""",
# Reset to original
"""
 /\_/\  
(  -_-)
 (   ) 
  | |  
"""
]


def clear_lines(frame: str):
    """Move the cursor up and clear the specified number of lines."""
    # Count the number of lines in the frame
    num_lines = frame.count("\n")
    # Move cursor up num_lines
    sys.stdout.write("\033[F" * num_lines)
    # Clear each line
    sys.stdout.write("\033[K" * num_lines)
    # Ensure the output is flushed to the terminal
    sys.stdout.flush()
    # Move cursor back to the start
    sys.stdout.write("\033[F")

def play_onload_animation(length: int | None = None) -> None:
    """Play the grumpy cat animation."""

    length = length if length else 2.6 / len(frames)

    for frame in frames:
        print(frame)
        time.sleep(length)
        clear_lines(frame)

    print(frames[0])


if __name__ == "__main__":
    play_onload_animation()