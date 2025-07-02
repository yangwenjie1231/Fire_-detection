from maix import camera, display, image, nn, app,time,touchscreen
detector = nn.YOLOv5(model="./model_119975.mud")
cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
dis = display.Display()
ts = touchscreen.TouchScreen()
stop_app_img = image.load("./ret.png")
while not app.need_exit():
    img = cam.read()
    img.draw_image(0, 0, stop_app_img)
    state = ts.read()
    if state[2]==1:
        if(state[0]>0 and state[0]<60)and(state[1]>0 and state[1]<60):
            print(123)
            app.set_exit_flag(True)
    objs = detector.detect(img, conf_th = 0.5, iou_th = 0.45)
    for obj in objs:
        img.draw_rect(obj.x, obj.y, obj.w, obj.h, color = image.COLOR_RED)
        msg = f'{detector.labels[obj.class_id]}: {obj.score:.2f}'
        img.draw_string(obj.x, obj.y, msg, color = image.COLOR_RED)
    dis.show(img)
