from ZEROENGINE.Main import *


if __name__ == "__main__":
    game = GameHandle()
    game.start_game()


    hello_text = GameObject(type="text", X=50, Y=50, property="Hello ZeroEngine!", additionalColor=pr.GREEN)
    game.add_object(hello_text)


    def move_script(obj):
        obj.x += 1
        pr.draw_text("I’m moving!", obj.x, obj.y, 20, pr.RED)
        if obj.x > Wx:
            obj.destroy()

    moving_obj = GameObject(type="scriptable", X=100, Y=200, property=move_script)
    game.add_object(moving_obj)

    game.game_loop()