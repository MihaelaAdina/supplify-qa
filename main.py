import unittest
from HTMLTestRunner.runner import HTMLTestRunner
from forms import TestForms
from company_filters import TestFilters
from open_projects import TestProjects

# get all tests
test_forms = unittest.TestLoader().loadTestsFromTestCase(TestForms)
test_filters = unittest.TestLoader().loadTestsFromTestCase(TestFilters)
test_projects = unittest.TestLoader().loadTestsFromTestCase(TestProjects)
# create the test suite
test_suite = unittest.TestSuite([test_forms, test_filters, test_projects])

# configure HMTLTestRunner options
runner = HTMLTestRunner(title="Test Report", description="Acceptance Tests", open_in_browser=True)

# run the tests
runner.run(test_suite)