
The test suite uses a mixture of [unittest](https://docs.python.org/3.8/library/unittest.html)
and [pytest](https://pytest-cov.readthedocs.io/en/latest/), depending on what is most
convenient for the actual test and the preference of the author. Pytest should be used
as the test runner.

Test are grouped into those which require a linked Dropbox account ("linked") and those
who can run by themselves ("offline"). The former tend to be integration test while the
latter are mostly unit tests. The current focus currently lies on integration tests,
especially for the sync engine, as they are easier to maintain when the implementation
and internal APIs change. Exceptions are made for performance tests, for instance for
indexing and cleaning up sync events, and for particularly complex functions that are
prone to regressions.

The current test suite uses a Dropbox access token provided by the environment variable
`DROPBOX_TOKEN` to connect to a real account.  The GitHub action which is running the
tests will set this environment variable for you with a temporary access token that
expires after 4 hours. Tests are run on `ubuntu- latest` and `macos- latest` in parallel
on different accounts and you should acquire a "lock" on the account before running
tests. Fixtures to create and clean up a test config and to acquire a lock are provided
in the `fixtures` module. If you run the tests locally, you will need to provide an
access token for your own Dropbox account.
