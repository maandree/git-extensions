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
from git import *


# TODO git-am
# TODO git-bisect
# TODO git-branch
# TODO git-bundle
# TODO git-checkout
# TODO git-cherry-pick
# TODO git-commit
# TODO git-describe
# TODO git-diff
# TODO git-fetch
# TODO git-format-patch
# TODO git-grep
# TODO git-log
# TODO git-merge
# TODO git-notes
# TODO git-pull
# TODO git-push
# TODO git-rebase
# TODO git-reset
# TODO git-revert
# TODO git-shortlog
# TODO git-show
# TODO git-stash
# TODO git-status
# TODO git-submodule
# TODO git-tag


def git_add(files,
            dry_run = False, verbose = False, force = False, interactive = False,
            patch = False, edit = False, update = False, no_ignore_removal = False,
            ignore_removal = False, intent_to_add = False, refresh = False,
            ignore_errors = False, ignore_missing = False,
            git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('add')
    if dry_run: args.append('--dry-run')
    if verbose: args.append('--verbose')
    if force: args.append('--force')
    if interactive: args.append('--interactive')
    if patch: args.append('--patch')
    if edit: args.append('--edit')
    if update: args.append('--update')
    if no_ignore_removal: args.append('--no-ignore-removal')
    if ignore_removal: args.append('--ignore-removal')
    if intent_to_add: args.append('--intent-to-add')
    if refresh_add: args.append('--refresh')
    if ignore_errors: args.append('--ignore-errors')
    if ignore_missing: args.append('--ignore-missing')
    args.append('--')
    args += files
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_archive(treeish, paths = [], extra = [],
                format = None, list = False, prefix = None, output = None,
                worktree_attributes = False, remote = None, exec = None,
                git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('archive')
    if format is not None: args.append('--format=%s' % format)
    if list: args.append('--list')
    if prefix is not None: args.append('--prefix=%s%s' % (prefix, '' if prefix.endswith('/') else '/'))
    args += extra
    if output is not None: args.append('--output=%s' % output)
    if worktree_attributes: args.append('--worktree-attributes')
    if remote is not None: args.append('--remote=%s' % remote)
    if exec is not None: args.append('--exec=%s' % exec)
    args.append(treeish)
    for path in paths:
        if path.startswith('-'):
            args.append('./%s' % path)
        else:
            args.append(path)
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_clean(path, exclude = [],
              directories = False, force = False, dry_run = False, quiet = False,
              level = 0, git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('clean')
    if directories: args.append('-d')
    if force: args.append('--force')
    if dry_run: args.append('--dry-run')
    if quite: args.append('--quite')
    for pattern in exclude:
        args.append('--pattern=%s' % pattern)
    if level == 1:
        args.append('-x')
    if level == 2:
        args.append('-X')
    args.append('--')
    args += paths
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_clone(repository, directory = None,
              template = None, local = False, shared = None, no_hardlinks = False,
              quite = False, verbose = False, progress = False, no_checkout = False,
              bare = False, mirror = False, reference = None, origin = None, branch = None,
              upload_pack = None, depth = None, single_branch = False, no_single_branch = False,
              recursive = False, separate_git_dir = None, git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('clone')
    if template is not None: args.append('--template=%s' % template)
    if local: args.append('--local')
    if shared: args.append('--shared')
    if no_hardlinks: args.append('--no-hardlinks')
    if quite: args.append('--quite')
    if verbose: args.append('--verbose')
    if progress: args.append('--progress')
    if no_checkout: args.append('--no-checkout')
    if bare: args.append('--bare')
    if mirror: args.append('--mirror')
    if reference is not None:
        args.append('--reference')
        args.append(reference)
    if separate_git_dir is not None:
        args.append('--separate-git-dir')
        args.append(separate_git_dir)
    if single_branch: args.append('--single-branch')
    if no_single_branch: args.append('--no-single-branch')
    if recursive: args.append('--recursive')
    args.append('--')
    args.append(repository)
    if directory is not None:
        args.append(directory)
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_gc(aggressive = False, auto = False, quite = False, no_prune = False, prune = None,
           git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('gc')
    if aggressive: args.append('--aggressive')
    if auto: args.append('--auto')
    if quite: args.append('--quite')
    if no_prune: args.append('--no-prune')
    if prune is not None: args.append('--prune=' % prune)
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_init(directory = None,
             quiet = False, bare = False, template = None, separate_git_dir = None,
             shared = None, git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('init')
    if quite: args.append('--quite')
    if bare: args.append('--bare')
    if template is not None: args.append('--template=%s' % template)
    if separate_git_dir is not None:
        args.append('--separate-git-dir')
        args.append(separate_git_dir)
    if shared is not None:
        if len(shared) == 0:
            args.append('--shared')
        else:
            args.append('--shared=%s' % shared)
    if directory is not None:
        if directory.startswith('-'):
            args.append('./%s' % directory)
        else:
            args.append(directory)
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_mv(files,
           verbose = False, force = False, dry_run = False, skip_error = False,
           git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('mv')
    if verbose: args.append('--verbose')
    if force: args.append('--force')
    if dry_run: args.append('--dry-run')
    if skip_move: args.append('-k')
    args.append('--')
    args += files
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_rm(files,
           force = False, dry_run = False, recursive = False,
           cached = False, ignore_unmatched = False, quiet = False,
           git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('rm')
    if force: args.append('--force')
    if dry_run: args.append('--dry-run')
    if recursive: args.append('-r')
    if cached: args.append('--cached')
    if ignore_unmatched: args.append('--ignore-unmatch')
    if quiet: args.append('--quiet')
    args.append('--')
    args += files
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None

