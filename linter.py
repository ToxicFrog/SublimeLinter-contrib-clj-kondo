from SublimeLinter.lint import Linter
import re

class ClojureKondoLinter(Linter):
  name = "clj-kondo"
  tempfile_suffix = "-"
  regex = r'^(?P<path>\S+):(?P<line>\d+):(?P<col>\d+): (?:(?P<warning>warning)|(?P<error>error)): (?P<message>.*)'
  multiline = False
  defaults = {
    'selector': 'source.clojure',
  }
  cmd = ['clj-kondo', '--lint', '${file}']
  word_re = re.compile(r'^([^][)(\s]+)')
