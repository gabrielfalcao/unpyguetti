from unpyguetti.refactoring import Strategy, matchers
from unpyguetti.refactoring.matchers import Class, Function
from unpyguetti.refactoring.matchers import Glob
from unpyguetti.refactoring.matchers import anything


matcher = Strategy('rename `mock_*_patch` parameters of test methods')

test_method_depending_on_mock_patch = (
    Function(named=anything)
    .with_param(named=Glob('mock_*_patch'))
    .within_class(named=anything, extends='unittest.TestCase')
)


@matcher.on(test_method_depending_on_mock_patch)
def rewrite_dependency(method):
    print(method)
