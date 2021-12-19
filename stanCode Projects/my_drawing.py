"""
File: my_drawing.py
Name: Elaine Chu
----------------------

"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    When you want some expensive things so badly, you'll need this meme.
    """
    window = GWindow(520, 582)
    window_bg = GRect(520, 582)
    window_bg.filled = True
    window_bg.fill_color = 'khaki'
    window.add(window_bg)
    body = GPolygon()
    body.add_vertex((120,349))
    body.add_vertex((300, 170))
    body.add_vertex((520,200))
    body.add_vertex((520, 582))
    body.add_vertex((70, 582))
    body.filled = True
    body.color = 'ivory'
    body.fill_color = 'ivory'
    window.add(body)
    back = GArc(310, 250, 0, 120)
    back.color = 'ivory'
    back.filled = True
    back.fill_color = 'ivory'
    window.add(back, 300, 170)
    tongue = GArc(80, 60, 10, -180)
    tongue.filled = True
    tongue.fill_color = 'coral'
    tongue.color = 'coral'
    window.add(tongue, 250, 392)
    face = GOval(350, 250)
    face.color = 'grey'
    face.filled = True
    face.fill_color = 'ivory'
    window.add(face, 100, 162)
    l_eye_upper = GArc(80, 40, -40, 180)
    l_eye_upper. color = 'black'
    l_eye_upper.filled = True
    window.add(l_eye_upper, 150, 300)
    l_eye_lower = GArc(80, 40, -40, -150)
    l_eye_lower.filled = True
    l_eye_lower.fill_color = 'black'
    window.add(l_eye_lower, 150, 300)
    r_eye = GOval(50, 40)
    r_eye.filled = True
    r_eyelid = GPolygon()
    r_eyelid.add_vertex((320, 300))
    r_eyelid.add_vertex((360, 305))
    r_eyelid.add_vertex((330, 340))
    r_eyelid.filled = True
    window.add(r_eye, 300, 300)
    window.add(r_eyelid)
    nose = GPolygon()
    nose.add_vertex((235, 380))
    nose.add_vertex((274, 380))
    nose.add_vertex((250, 410))
    nose.filled = True
    nose.color = 'coral'
    nose.fill_color = 'coral'
    window.add(nose)
    nose_l = GLine(225, 361, 250, 410)
    nose_l.color = 'coral'
    window.add(nose_l)
    nose_r = GLine(250, 410, 290, 360)
    nose_r.color = 'coral'
    window.add(nose_r)
    tear0 = GOval(5, 5)
    tear0.filled = True
    tear0.color = 'ivory'
    tear0.fill_color = 'ivory'
    window.add(tear0, 210, 310)
    tear1 = GOval(7, 7)
    tear1.filled = True
    tear1.color = 'ivory'
    tear1.fill_color = 'ivory'
    window.add(tear1, 200, 315)
    tear2 = GOval(7, 7)
    tear2.filled = True
    tear2.color = 'ivory'
    tear2.fill_color = 'ivory'
    window.add(tear2, 200, 305)
    tear3 = GOval(7, 7)
    tear3.filled = True
    tear3.color = 'ivory'
    tear3.fill_color = 'ivory'
    window.add(tear3, 320, 320)
    tear4 = GOval(6, 6)
    tear4.filled = True
    tear4.color = 'ivory'
    tear4.fill_color = 'ivory'
    window.add(tear4, 315, 330)
    tear5 = GOval(6, 6)
    tear5.filled = True
    tear5.color = 'ivory'
    tear5.fill_color = 'ivory'
    window.add(tear5, 310, 325)
    m0 = GArc(200, 50, 70, 130)
    m0.color = 'grey'
    window.add(m0, 100, 350)
    m1 = GArc(150, 70, 30, 160)
    m1.color = 'grey'
    window.add(m1, 90, 370)
    m2 = GArc(120, 80, 30, 160)
    m2.color = 'grey'
    window.add(m2, 120, 390)
    m4 = GArc(100, 100, 10, 150)
    m4.color = 'grey'
    window.add(m4, 350, 340)
    m5 = GArc(150, 70, 30, 160)
    m5.color = 'grey'
    window.add(m5, 340, 360)
    m6 = GArc(120, 80, 30, 160)
    m6.color = 'grey'
    window.add(m6, 330, 380)
    t0 = GLabel('抱歉了錢錢')
    t0.font = '-50'
    t0.color = 'black'
    window.add(t0, 120, 120)
    t1 = GLabel('但我真的需要那個酷東西')
    t1.font = '-40'
    t1.color = 'black'
    window.add(t1, 50, 500)


if __name__ == '__main__':
    main()
