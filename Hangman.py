import random
import time
from words_key import vocable

def inputwords():
    key = random.choice(vocable)
    return key.upper()
    