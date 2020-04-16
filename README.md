SublimeLinter-contrib-clj-kondo
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [clj-kondo](https://github.com/borkdude/clj-kondo). It will be used with files that have the `clojure` syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `clj-kondo` is installed on your system.

In order for `clj-kondo` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

There are currently no additional editor-wide settings for clj-kondo. You can [configure it per project](https://github.com/borkdude/clj-kondo/blob/master/doc/config.md) via the usual `config.edn` file.
