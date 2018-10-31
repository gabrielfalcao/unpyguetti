import unittest
import unittest.mock



class SomeTestDependingOnMock(unittest.TestCase):

    @unittest.mock.patch('sys.stdout')
    def test_method_depending_on_mock_patch(self, mock_stdout_patch):
        """
        tests how to write to stdout
        """

        print('hello world')

        mock_stdout_patch.write.assert_called_once_with('hello\n')
