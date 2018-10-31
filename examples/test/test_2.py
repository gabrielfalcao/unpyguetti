import unittest
import unittest.mock



class AnotherTestDependingOnMock(unittest.TestCase):

    @unittest.mock.patch('io.open')
    def test_blabla(self, mock_open_patch):
        """
        tests how to write to stdout
        """

        print('hello world')

        mock_stdout_patch.write.assert_called_once_with('hello\n')


    @unittest.mock.patch('io.open')
    def test_blabla(self, io_open):
        import io

        io.open('foo')

        io_open.assert_called_once_with('foo')


    @unittest.mock.patch('io.open')
    def test_blabla(self, mock_io_open_patch):
        import io

        io.open('foo')

        mock_io_open_patch.assert_called_once_with('foo')
