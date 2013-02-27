basePath = '../../';

files = [
  ANGULAR_SCENARIO,
  ANGULAR_SCENARIO_ADAPTER,
  'test/e2e/**/*.js'
];

autoWatch = false;

browsers = ['Chrome'];

singleRun = true;

proxies = {
  '/': 'http://localhost:8008/'
};

junitReporter = {
  outputFile: 'test/test_out/e2e.xml',
  suite: 'e2e'
};
