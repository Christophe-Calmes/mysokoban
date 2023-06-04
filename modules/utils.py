import pygame


class Utils:
    @staticmethod
    def detectCollideBoxes(boxes, player, event, walls):
        collision_index = player.rect.collidelist(boxes)
        if collision_index != -1:
            boxes[collision_index].move(event)
        
        if player.rect.collidelist(walls) != -1:
            player.moveBack()

            
                    
                        
                    
