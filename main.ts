controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    fish.setImage(assets.image`clownFish0`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    scene.setBackgroundImage(assets.image`myImage1`)
    关卡1.destroy()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    fish.setImage(assets.image`clownFish2`)
})
sprites.onDestroyed(SpriteKind.Projectile, function (sprite) {
    弹幕1 = sprites.create(assets.image`弹幕1`, SpriteKind.Enemy)
    弹幕1.setPosition(0, 0)
    弹幕1.setVelocity(60, 40)
    弹幕1.setBounceOnWall(true)
})
let 弹幕1: Sprite = null
let fish: Sprite = null
let 关卡1: Sprite = null
scene.setBackgroundImage(assets.image`myImage`)
关卡1 = sprites.create(assets.image`关卡1`, SpriteKind.Projectile)
fish = sprites.create(assets.image`clownFish2`, SpriteKind.Player)
fish.setPosition(80, 70)
controller.moveSprite(fish)
fish.setStayInScreen(true)
fish.startEffect(effects.bubbles)
关卡1.startEffect(effects.bubbles)
关卡1.setPosition(10, 60)
