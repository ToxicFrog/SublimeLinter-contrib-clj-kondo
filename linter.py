from SublimeLinter.lint import Linter
import re

class ClojureKondoLinter(Linter):
  name = "clj-kondo"
  regex = r'^(?P<path>\S+):(?P<line>\d+):(?P<col>\d+): (?:(?P<warning>warning)|(?P<error>error)): (?P<message>.*)'
  multiline = False
  defaults = {
    'selector': 'source.clojure - source.clojure.clojurescript',
  }
  cmd = ['clj-kondo', '--lang', 'clj', '--lint', '-']
  word_re = r'^([^][)(\s]+)'

class ClojureScriptKondoLinter(Linter):
  name = "cljs-kondo"
  regex = r'^(?P<path>\S+):(?P<line>\d+):(?P<col>\d+): (?:(?P<warning>warning)|(?P<error>error)): (?P<message>.*)'
  multiline = False
  defaults = {
    'selector': 'source.clojurescript, source.clojure.clojurescript',
  }
  cmd = ['clj-kondo', '--lang', 'cljs', '--lint', '-']
  word_re = r'^([^][)(\s]+)'
