def on_right_pressed():
    fish.set_image(assets.image("""
        clownFish0
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    scene.set_background_image(assets.image("""
        myImage1
    """))
    关卡1.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_left_pressed():
    fish.set_image(assets.image("""
        clownFish2
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_destroyed(sprite):
    global 弹幕1
    弹幕1 = sprites.create(assets.image("""
        弹幕1
    """), SpriteKind.enemy)
    弹幕1.set_position(0, 0)
    弹幕1.set_velocity(60, 40)
    弹幕1.set_bounce_on_wall(True)
sprites.on_destroyed(SpriteKind.projectile, on_on_destroyed)

弹幕1: Sprite = None
fish: Sprite = None
关卡1: Sprite = None
scene.set_background_image(assets.image("""
    myImage
"""))
关卡1 = sprites.create(assets.image("""
    关卡1
"""), SpriteKind.projectile)
fish = sprites.create(assets.image("""
    clownFish2
"""), SpriteKind.player)
fish.set_position(80, 70)
controller.move_sprite(fish)
fish.set_stay_in_screen(True)
fish.start_effect(effects.bubbles)
关卡1.start_effect(effects.bubbles)
关卡1.set_position(10, 60)