import unittest
import numpy as np
from src.meshing.mesh_generator import generate_uniform_mesh

class TestMesh(unittest.TestCase):
    """Test cases for mesh generation."""
    
    def test_uniform_mesh(self):
        """Test that uniform mesh is generated correctly."""
        S_min, S_max, N_elements = 0, 100, 10
        nodes = generate_uniform_mesh(S_min, S_max, N_elements)
        
        self.assertEqual(len(nodes), N_elements + 1)
        self.assertAlmostEqual(nodes[0], S_min)
        self.assertAlmostEqual(nodes[-1], S_max)
        self.assertTrue(np.all(np.diff(nodes) > 0))  # Check ascending order

if __name__ == '__main__':
    unittest.main()
