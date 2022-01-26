
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def resolucion(x):
    x=str(x).lower()
    if "no injury" in x:
        x= "no injury"
        return x
    elif "fatal" in x:
        x= "death"
        return x
    elif x == "nan":
        return np.nan
    else:
        x= "bite"
        return x


def sexo(x):
    x=str(x).lower()
    if "f" in x:
        x= "f"
        return x
    elif "m" in x:
        x= "m"
        return x
    elif x == "nan":
        return np.nan
    else:
        x= "otro"
        return np.nan

def deaths(x):
    if x!=x:
        return np.nan
    x=str(x).lower()
    if "n" in x:
        x= 0
        return x
    elif "m" in x:
        x= 0
        return x
    elif "unkn" in x:
        return np.nan        
    elif  "y" in x:
        x=1
        return x        
    else:
        x = 1
        return x


def sharks(x):
    x=str(x).lower()
    if "white shark" in x:
        x= "whiteshark"
        return x
    elif "bull" in x:
        x= "bullshark"
        return x
    elif x == "nan":
        return np.nan
    elif "tiger" in x:
        x= "tigershark"
        return x        
    elif  "whitetip" in x:
        x="whitetip"
        return x
    elif  "hammer" in x:
        x="hammer"
        return x 
    else:
        x = "other"
        return x

