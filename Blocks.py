# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:35:32 2021

@author: maurop
"""


import PIL

import os
import pathlib

import matplotlib.pyplot as plt

texture_folder = pathlib.Path("./1.17.1/assets/minecraft/textures/block")

good_block_file = pathlib.Path("./good_blocks.txt")

def average_color(image):
    
    px_matrix = image.load()
    
    col_avg = [0, 0, 0]
    
    for i in range(16):
        for j in range(16):
            px = px_matrix[i, j]

            
            if isinstance(px, int) or len(px) != 4 or px[3] == 0:
            
                continue
            
            for c in range(3):
                
                col_avg[c] += px[c]

    
    for i in range(3):
        col_avg[i] = col_avg[i] / (16*16) / 256

    
    return col_avg


class Block:
    
    def __init__(self, name, image):
        
        self.name = name
        self.image = image
        
    def correct_pixel(self, px):
        
        if isinstance(px, int):
            px_int = px
            px = []
            for i in range(3):
                px.append(px_int * 16)
            
        # if the image has a alpha channel that is 0 skip the pixels
        if len(px) == 4 and px[3] == 0:
            #print("skipped px", px, "because alpha is 0")
            px = None      
        
        return px
        
    
        
    def average_color(self):
        
        px_matrix = self.image.load()
        
        col_avg = [0, 0, 0]
        
        for i in range(16):
            for j in range(16):
                px = px_matrix[i, j]
                
                # if the image is  in 8 bit grayscale
                if isinstance(px, int):
                    px_int = px
                    px = []
                    for i in range(3):
                        px.append(px_int * 16)
                    
                # if the image has a alpha channel that is 0 skip the pixels
                if len(px) == 4 and px[3] == 0:
                    #print("skipped px", px, "because alpha is 0")
                    continue

                
                for c in range(3):
                    col_avg[c] += px[c]
    
        
        for i in range(3):
            col_avg[i] = col_avg[i] / (16*16) / 256
        
        
        return col_avg
    
    def top_color(self):
        
        px_matrix = self.image.load()
        
        hist = {}
        
        for i in range(16):
            for j in range(16):
                
                px = px_matrix[i, j]
                
                # if the image is  in 8 bit grayscale
                if isinstance(px, int):
                    px_int = px
                    px = []
                    for i in range(3):
                        px.append(px_int * 16)
                    
                # if the image has a alpha channel that is 0 skip the pixels
                if len(px) == 4 and px[3] == 0:
                    #print("skipped px", px, "because alpha is 0")
                    continue
                
                px = tuple(px)
                
                try:
                    hist[px] += 1
                    
                except KeyError:
                    hist[px] = 1
                    
        
        max_v = max(hist.values())
        
        for k, v in hist.items():
            
            if v == max_v:
                
                if isinstance(k, int):
                    k = [1, 1, 1]
                
                color = [x / 256 for x in k[:3]]
                return color
        
                
        
        
                
    
    

def load_blocks():
    good_blocks_filenames = []
    
    if good_block_file.is_file():
        
        with open(good_block_file, "r") as f:
            lines = f.readlines()
            
        for line in lines:
            good_blocks_filenames.append(line.strip())
            
    else:
        print("Good blocks file not found")
        
        
    blocks = []
        
    
    for block_filename in good_blocks_filenames:
        
       
        
        path = texture_folder / pathlib.Path(block_filename)
        
        
        im = PIL.Image.open(path)
        
        name = block_filename.replace(".png", "")
        
        b = Block(name, im)
        
        blocks.append(b)
        
    print("load_blocks: loaded blocks")
    
    return blocks

    
        
if __name__ == "__main__":
    blocks = load_blocks()
    
    for block in blocks:
        
        if block.name == "dispenser_front":
            print(block.top_color())

            
            
    
    
        
    
    
