from SublimeLinter.lint import Linter
import re

class ClojureKondoLinter(Linter):
  name = "clj-kondo"
  regex = r'^(?P<path>\S+):(?P<line>\d+):(?P<col>\d+): (?:(?P<warning>warning)|(?P<error>error)): (?P<message>.*)'
  multiline = False
  defaults = {
    # TODO: support clojurescript as well.
    # It has scope 'source.clojurescript', but we also need to replace
    # --lang clj with --lang cljs
    'selector': 'source.clojure',
  }
  cmd = ['clj-kondo', '--lang', 'clj', '--lint', '-']
  word_re = r'^([^][)(\s]+)'
