import unittest
import controller as cont
import time
__author__ = 'johnathan'


class ControllerTest(unittest.TestCase):

    def test_1_isConnected(self):
        cont.update()
        self.assertTrue(cont.isConnected(), "Controller was not found")
        print "controller was found"

    def test_2_buttonsWorking(self):
        notDone = True
        print "starting button test"
        buttons = [False, False, False, False, False, False, False, False, False, False]
        while notDone:
            cont.update()
            for x in range(0, 10):
                if cont.getButton(x) and buttons[x] == False:
                    print "button ", x
                    buttons[x] = True
            if all(buttons):
                notDone = False



    def test_3_Axis(self):
        print "starting Axis test, press a to pass, b to fail"
        while True:
            time.sleep(0.1)
            cont.update()
            if cont.getButton(cont.A):
                break
            if cont.getButton(cont.B):
                self.assertEqual(True, False, "Axis Test Failed")
            print "X: ", cont.getPrimaryX(), " Y: ", cont.getPrimaryY(), " X2: ", cont.getSecondaryX(), " Y2: ", cont.getSecondaryY()