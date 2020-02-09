"""The template of the main script of the machine learning process
"""

import games.arkanoid.communication as comm
from games.arkanoid.communication import ( \
    SceneInfo, GameStatus, PlatformAction
)

def ml_loop():
    """The main loop of the machine learning process

    This loop is run in a separate process, and communicates with the game process.

    Note that the game process won't wait for the ml process to generate the
    GameInstruction. It is possible that the frame of the GameInstruction
    is behind of the current frame in the game process. Try to decrease the fps
    to avoid this situation.
    """

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here.

    # 2. Inform the game process that ml process is ready before start the loop.
    comm.ml_ready()

    # 3. Start an endless loop.
    while True:
        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()

        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.
        if scene_info.status == GameStatus.GAME_OVER or \
            scene_info.status == GameStatus.GAME_PASS:
            # Do some stuff if needed

            # 3.2.1. Inform the game process that ml process is ready
            comm.ml_ready()
            continue

        # 3.3. Put the code here to handle the scene information
        ball_x = scene_info.ball[0]
        ball_y = scene_info.ball[1]
        platform = scene_info.platform[0]+20
        
        #print(ball_y)
        #print(platform_C)
        #print(i)
        if ball_y <= 260 or ball_ey > ball_y:
            u = 0
            if platform > 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            if platform < 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
        else:
            if u !=1:
                if ball_ex > ball_x:
                    if ball_x -140 >0:
                        i = ball_x -140
                    else:
                        i = -(ball_x - 140)
                else:
                    if ball_x +140 <200:
                        i = i = ball_x +140
                    else:
                        i = 400-(ball_x + 140)
                u = 1
 
            
            if platform > i:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            elif platform < i:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            else :
                comm.send_instruction(scene_info.frame, PlatformAction.NONE)
        
        ball_ey = ball_y        
        ball_ex = ball_x
        
        
