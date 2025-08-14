import unittest
from galaxy import Galaxy
from sorting import my_mutating_sort, my_immutable_sort, galaxy_sorting_method

class TestGalaxySorting(unittest.TestCase):

    def setUp(self):
        self.galaxy1 = Galaxy("Milky Way", 1e12)
        self.galaxy2 = Galaxy("Andromeda", 1.2e12)
        self.galaxy3 = Galaxy("Triangulum", 5e11)

    def test_sorting(self):
        galaxies = [self.galaxy2, self.galaxy1, self.galaxy3]
        sorted_galaxies = my_immutable_sort(galaxies)
        self.assertEqual(sorted_galaxies, [self.galaxy3, self.galaxy1, self.galaxy2])
        my_mutating_sort(galaxies)
        self.assertEqual(galaxies, [self.galaxy3, self.galaxy1, self.galaxy2])

    def test_galaxy_sorting_method(self):
        galaxies = [self.galaxy2, self.galaxy1, self.galaxy3]
        self.assertEqual(galaxy_sorting_method(galaxies), [self.galaxy3, self.galaxy1, self.galaxy2])


if __name__ == "__main__":
    unittest.main()