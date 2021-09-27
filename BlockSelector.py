# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:17:24 2021

@author: maurop
"""


import PIL

import os
import pathlib

import matplotlib.pyplot as plt

texture_folder = pathlib.Path("./1.17.1/assets/minecraft/textures/block")

# read the good block file
        
good_block_file = pathlib.Path("./good_blocks.txt")
bad_block_file = pathlib.Path("./bad_blocks.txt")

good_blocks_filenames = []
bad_blocks_filenames = []

if good_block_file.is_file():
    
    with open(good_block_file, "r") as f:
        lines = f.readlines()
        
    for line in lines:
        good_blocks_filenames.append(line.strip())

if bad_block_file.is_file():
    
    with open(bad_block_file, "r") as f:
        lines = f.readlines()
        
    for line in lines:
        bad_blocks_filenames.append(line.strip())
        

# read all the images

files = os.listdir(texture_folder)


for file in files:
    
    path = texture_folder / pathlib.Path(file)
        
    if path.is_file() and path.suffix == ".png":
        
        im = PIL.Image.open(path)
        
        if im.size == (16, 16): 
            
            # chose if block is appropriate
            
            
            
            
            
            if file in good_blocks_filenames:
                print(file, "block already good")
                continue
                
            elif file in bad_blocks_filenames:
                print(file, "block already bad")
                continue
            else:

                plt.imshow(im)
                plt.show()
                print(file)            
                
                i = input("is block appropriate: ")
        
                if i == "":
                    
                    with open(good_block_file, "a") as f:
                        f.write(file + "\n")
                elif i != "q":
                    with open(bad_block_file, "a") as f:
                        f.write(file + "\n")
                else:
                    print("program quit")
                    break