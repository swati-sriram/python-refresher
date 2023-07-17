import unittest
import physics
import numpy as np

class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_bouyancy(10, 1000), 98100.0)
        self.assertNotEqual(physics.calculate_bouyancy(15, 56), 100)
        self.assertRaises(ValueError, physics.calculate_bouyancy,-2, 3)
        self.assertRaises(ValueError, physics.calculate_bouyancy,2, -3)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(100,10), True)
        self.assertEqual(physics.will_it_float(5,5000), None)
        self.assertRaises(ValueError, physics.will_it_float,2, -3)
        self.assertRaises(ValueError, physics.will_it_float,-2, 3)
        self.assertRaises(ValueError, physics.will_it_float,-2, -3)
        self.assertRaises(ValueError, physics.will_it_float,0, 3)
        self.assertRaises(ValueError, physics.will_it_float,-2, 0)
        self.assertRaises(ValueError, physics.will_it_float,0, 0)
        

    def test_calculate_pressure(self):
        self.assertAlmostEqual(physics.calculate_pressure(10), 98100+101325)
        self.assertAlmostEqual(physics.calculate_pressure(-10), 98100+101325)
        self.assertNotEqual(physics.calculate_pressure(200), 98100 + 101325)
    
    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(10, 20), 0.5)
        self.assertRaises(ValueError, physics.calculate_acceleration, 10, -2)
        self.assertRaises(ValueError, physics.calculate_acceleration, -10, -2)
        self.assertRaises(ValueError, physics.calculate_acceleration, -10, 2)
        self.assertNotEqual(physics.calculate_acceleration(10, 30), 0.5)
    
    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(-10, 2), -5)
        self.assertEqual(physics.calculate_angular_acceleration(10, 2), 5)
        self.assertRaises(ValueError, physics.calculate_angular_acceleration, 10, -2)
        self.assertNotEqual(physics.calculate_angular_acceleration(10, 23), 5)
    
    def test_calculate_torque(self):
        self.assertAlmostEqual(physics.calculate_torque(10,180,10), 0)
        self.assertAlmostEqual(physics.calculate_torque(10,-180,10), 0)
        self.assertRaises(ValueError, physics.calculate_torque,-10,275, -3)
        self.assertRaises(ValueError, physics.calculate_torque,10,275, -3)
        self.assertRaises(ValueError, physics.calculate_torque,-10,275, 3)
    
    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(5,2),20)
        self.assertNotEqual(physics.calculate_moment_of_inertia(5,20),20)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia,-10,275)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia,10,-275)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia,-10,-275)

    def test_calculate_auv_acceleration(self):
        self.assertNotEqual(np.allclose(physics.calculate_auv_acceleration(10, np.pi), np.array([10,10])), True)
        self.assertEqual(np.allclose(physics.calculate_auv_acceleration(50, np.pi/2, 25), np.array([2*np.cos(np.pi/2),2*np.sin(np.pi/2)])), True)
        self.assertRaises(ValueError, physics.calculate_auv_acceleration, -10,3)





if __name__ == "__main__":
    unittest.main()

