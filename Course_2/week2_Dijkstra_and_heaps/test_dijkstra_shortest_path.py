import unittest

import dijkstra_shortest_path as d


class TestDijtstra(unittest.TestCase):

    def setUp(self):
        """
        Do the following after each test
        """
        # self.apoc_1 = Apocalypse(5,5, [(1,1)], [(2,2)], [(4,4)])


    def tearDown(self):
        """
        Do the following after each test
        """
        pass

    def test_dijkstra(self):
        graph1 = {1: {2:1, 3:4}, 2:{3:2, 4:6}, 3:{4:3}, 4:{}}

        expected = {1:0, 2:1, 3:3, 4:6}
        result = d.dijkstra(graph1, 1)
        self.assertEqual(result, expected)

        expected = {1:1000000, 2:0, 3:2, 4:5}
        result = d.dijkstra(graph1, 2)
        self.assertEqual(result, expected)

        expected = {1:1000000, 2:1000000, 3:0, 4:3}
        result = d.dijkstra(graph1, 3)
        self.assertEqual(result, expected)

        expected = {1:1000000, 2:1000000, 3:1000000, 4:0}
        result = d.dijkstra(graph1, 4)
        self.assertEqual(result, expected)

        graph2 = {1: {2:1, 3:4, 4:2}, 2:{3:2, 4:6}, 3:{4:3}, 4:{}}

        expected = {1:0, 2:1, 3:3, 4:2}
        result = d.dijkstra(graph2, 1)
        self.assertEqual(result, expected)


        graph3 = {1: {2:1, 3:4}, 2:{3:2, 4:6, 4:1}, 3:{4:3}, 4:{}}

        expected = {1:0, 2:1, 3:3, 4:2}
        result = d.dijkstra(graph3, 1)
        self.assertEqual(result, expected)

        graph4 = {1:{2:1,8:2},2:{1:1,3:1},3:{2:1,4:1}, 4:{3:1,5:1}, 5:{4:1,6:1}, 6:{5:1, 7:1}, 7:{6:1, 8:1}, 8: {7:1,1:2}}
        result = d.dijkstra(graph4,1)
        expected = {1:0, 2:1, 3:2, 4:3, 5:4, 6:4, 7:3, 8:2}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
