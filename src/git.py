#!/usr/bin/env python3
# -*- mode: python, coding: utf-8 -*-
'''
git-extensions — Simple handy extensions for git
Copyright © 2012, 2013  Mattias Andrée (maandree@member.fsf.org)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import sys
import os
from subprocess import Popen, PIPE


def git(*arguments):
    '''
    Execute a git command and return the result
    
    @param   arguments:*str|list<str>  Arguments for git to run with
    @return  :str                      Git's output to stdout, one trailing new line will be removed
    @throws  :Exception                On error, global variable errno will set the the return code
                                       iff git failed
    '''
    global errno
    if (len(arguments) == 1) and isinstance(arguments[0], list):
        arguments = arguments[0]
    else:
        arguments = list(arguments)
    proc = Popen(['git', '--no-pager'] + arguments,
          stdin = sys.stdin.buffer,
          stdout = PIPE,
          stderr = sys.stderr.buffer)
    out = proc.communicate()[0]
    out = out.decode('utf-8', 'error')
    if out.endswith('\n'):
        out = out[:-1]
    if proc.returncode != 0:
        errno = proc.returncode
        raise Exception('git exited with return value: %i' % proc.returncode)
    return out


def git_out(*arguments):
    '''
    Execute a git command and print the result
    
    @param   arguments:*str|list<str>  Arguments for git to run with
    @throws  :Exception                On error, global variable errno will set the the return code
                                       iff git failed
    '''
    global errno
    if (len(arguments) == 1) and isinstance(arguments[0], list):
        arguments = arguments[0]
    else:
        arguments = list(arguments)
    proc = Popen(['git'] + arguments,
          stdin = sys.stdin.buffer,
          stdout = sys.stdout.buffer,
          stderr = sys.stderr.buffer)
    proc.wait()
    if proc.returncode != 0:
        errno = proc.returncode
        raise Exception('git exited with return value: %i' % proc.returncode)


def export(variable, value):
    '''
    Export a environment variable
    
    @param  variable:str  The environment variable
    @param  value:str?    The variable's new value, `None` for unsetting it
    '''
    if value is None:
        os.unsetenv(var)
        if var in os.environ:
            del os.environ[var]
    else:
        os.putenv(var, value)
        if var not in os.environ or os.environ[var] != value:
            os.environ[var] = value


def env(variable):
    '''
    Read a environment variable
    
    @param   variable:str  The environment variable
    @return  :str?         The variable's value, `None` if it is not set
    '''
    return os.environ[variable] if variable in os.environ else None


def version():
    '''
    Get the installed version of git
    
    @return  :str  The version number
    '''
    return git('--version').split(' ')[-1]


def core_path():
    '''
    Get the path where core git programs are installed
    
    @return  :str  The path
    '''
    return git('--exec-path')


def html_path():
    '''
    Get the path where git HTML documentation is installed
    
    @return  :str  The path
    '''
    return git('--html-path')


def man_path():
    '''
    Get the path where git man page documentation is installed
    
    @return  :str  The path
    '''
    return git('--man-path')


def info_path():
    '''
    Get the path where git info documentation is installed
    
    @return  :str  The path
    '''
    return git('--info-path')


def argument_configure(name, value):
    '''
    Constructor arguments for override configurations
    
    @param   name:str    The name of the configuration
    @param   value:str   The value of the configuration
    @return  :list<str>  The arguments to pass
    '''
    return ['-c', '%s=%s' % (name, value)]


def argument_core_path(path):
    '''
    Constructor arguments for the path with core git programs are installed
    
    @param   path:str    The path
    @return  :list<str>  The arguments to pass
    '''
    return ['--exec-path=%s' % path]


def argument_paginate():
    '''
    Constructor arguments for using $PAGER (fall back to `less`)
    
    @return  :list<str>  The arguments to pass
    '''
    return ['--paginate']


def argument_no_pager():
    '''
    Constructor arguments for instructing git not to use a pager
    
    @return  :list<str>  The arguments to pass
    '''
    return ['--no-pager']


def argument_git_dir(path):
    '''
    Constructor arguments for instructing git use another root for the git repository
    
    @param   path:str    The path
    @return  :list<str>  The arguments to pass
    '''
    return ['--git-dir=%s' % path]


def argument_word_tree(path):
    '''
    Constructor arguments for instructing git use another path for the work tree
    
    @param   path:str    The path
    @return  :list<str>  The arguments to pass
    '''
    return ['--work-tree=%s' % path]


def argument_namespace(path):
    '''
    Constructor arguments for setting git namespace
    
    @param   path:str    The namespace
    @return  :list<str>  The arguments to pass
    '''
    return ['--namespace=%s' % path]


def argument_bare():
    '''
    Constructor arguments for instructing git to treat the repository as a bare repository
    
    @return  :list<str>  The arguments to pass
    '''
    return ['--bare']


def argument_no_replace_objects():
    '''
    Constructor arguments for instructing git not to use replacement refs
    
    @return  :list<str>  The arguments to pass
    '''
    return ['--no-replace-objects']


def argument_literal_pathspecs():
    '''
    Constructor arguments for instructing git to treat pathspecs literally, rather than as glob patterns
    
    @return  :list<str>  The arguments to pass
    '''
    return ['--literal-pathspecs']

