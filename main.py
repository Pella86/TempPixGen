# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:22:30 2021

@author: maurop
"""


import PIL

import os
import pathlib

import matplotlib.pyplot as plt
import matplotlib.patches as patches

import math

import Blocks


texture_folder = pathlib.Path("./1.17.1/assets/minecraft/textures/block")



def draw_rectangle(color, ax = None):
    if ax == None:
        fig, ax = plt.subplots()

    ax.add_patch(patches.Rectangle((0,0), 1, 1, facecolor=color))
    
    plt.show()



def distance(p1, p2):
    
    sq = 0
    
    for i in range(3):
        sq += (p2[i] - p1[i])**2
    
    return math.sqrt(sq)

def wdistance(c1, c2):
    
    c1 = [x * 256 for x in c1]
    c2 = [x * 256 for x in c2]
    
    R1 = c1[0]
    G1 = c1[1]
    B1 = c1[2]
    
    R2 = c2[0]
    G2 = c2[1]
    B2 = c2[2]
    
    
    r = (R1 + R2) / 2
    
    DR = R1 - R2
    DG = G1 - G2
    DB = B1 - B2
    

    dc = math.sqrt((2 + r /256) * DR ** 2 + 4 * DG ** 2 + (2 + (255 - r)/256) * DB ** 2)
    
    return dc
    
blocks = Blocks.load_blocks()


# load the model image
model_image = PIL.Image.open(pathlib.Path("./creeper_head.png"))

plt.imshow(model_image)
plt.show()


px_matrix = model_image.load()



def best_block(color):
    
    mind = None
    best_block = None
    
    for block in blocks:
        
        dblock = wdistance(color, block.average_color())
        
        if mind == None:
            mind = dblock
            best_block = block
            
            
        elif dblock < mind:
        
            mind = dblock
            best_block = block
    
    return best_block


# best 10 blocks
    
    

class Stack:
    
    def __init__(self):
        
        self.stack_size = 25
        
        self.stack = []
        
        self.refused_blocks = []
    
    
    def add(self, block, distance):
        
        for b, _ in self.stack:
            if block == b:
                print("block already in stack")
                return
        
        for b, _ in self.refused_blocks:
            if block == b:
                print("block lready refused")
        
        
        
        
        if len(self.stack) < self.stack_size:
            self.stack.append((block, distance))
        
        else:
            # append
            
            self.stack.append((block, distance))
            
            # sort
            
            self.stack.sort(key=lambda i : i[1])
            
            # pop
            
            refused = self.stack.pop()
            
            self.refused_blocks.append(refused)
            
    def print_block_names(self):
        for block, distance in self.stack:
            print(block.name, f"{distance:.2f}", [f"{x:.2f}" for x in block.average_color()])
    
    def show_images(self):
        
        for block, _ in self.stack:
        
            fig, axs = plt.subplots(nrows=1, ncols=2)
        
            axs[0].imshow(block.image)
            
            draw_rectangle(block.average_color(), axs[1])
            
            
    





# first_px = [x / 256 for x in px_matrix[0, 0]]


# if first_px[3] == 0:
#     first_px = (1.0, 1.0, 1.0)
# else:
#     first_px = first_px[:3]

# print(first_px)


# draw_rectangle(first_px)


# stack = Stack()


# for block in blocks:
    
#     dblock = wdistance(first_px, block.average_color())
    
#     stack.add(block, dblock)
    
    
    
# stack.print_block_names()

# stack.show_images()









# best_blocks = []


# for block in blocks:
    
#     dblock = wdistance(first_px, block.top_color())
    
#     if len(best_blocks) < 10:
#         best_blocks.append(block)
        
#     else:
#         for i in range(len(best_blocks)):
            
#             if dblock  < wdistance(first_px, best_blocks[i].top_color()):
#                 best_blocks[i] = block
#                 break
        
        
# for bblock in best_blocks:
    
#     print(bblock.name)
    
#     plt.imshow(bblock.image)
#     plt.show()
    
#     draw_rectangle(bblock.top_color())
    



new_im = PIL.Image.new("RGB", size=(9 * 16, 9 * 16))
new_px_matrix = new_im.load()

for i in range(9):
    for j in range(9):
        
        print(i, j)
        
        color = px_matrix[i, j]
        
        color = [x / 256 for x in color]
        
        bblock = best_block(color)
        
        print(bblock.name)
        
        # new_color = bblock.average_color()
        
        # new_color = [int(x * 256) for x in new_color]
        
        # print(new_color)
        
        # new_px_matrix[i, j] = tuple(new_color)
        
        new_im.paste(bblock.image, (i * 16, j * 16))

plt.imshow(new_im)
plt.show()
        
        
    

    


