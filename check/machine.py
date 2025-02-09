from machine import freq
from config import alt_freq

f = freq()
print("Default frequency is {f}")
if alt_freq:
    freq(alt_freq)  # Set alternate frequency
    if new_freq := freq() != alt_freq:
        raise ValueError("Frequency didn't change as expected. freq()={new_freq}")
    print("Alternate frequency set to {alt_freq}")
    freq(f) # Re-set default frequecy