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


def git_am(mailboxes = [],
           signoff = False, keep = False, keep_non_patch = False, no_keep_cr = False,
           keep_cr = False, scissors = False, no_scissors = False, quiet = False,
           utf8 = False, no_utf8 = False, threeway = False, interactive = False,
           committer_date_is_author_date = False, ignore_date = False, resolvemsg = None,
           ignore_space_change = False, ignore_whitesspace = False, whitespace = None,
           remote_leading_slashes = None, ensure_surrounding = None, directory = None,
           exclude = [], include = [], reject = False, git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('am')
    if signoff: args.append('--signoff')
    if keep: args.append('--keep')
    if keep_non_patch: args.append('--keep-non-patch')
    if no_keep_cr: args.append('--no-keep-cr')
    if keep_cr: args.append('--keep-cr')
    if scissors: args.append('--scissors')
    if no_scissors: args.append('--no-scissors')
    if quiet: args.append('--quiet')
    if utf8: args.append('--utf8')
    if no_utf8: args.append('--no-utf8')
    if threeway: args.append('--3way')
    if interactive: args.append('--interactive')
    if committer_date_is_author_date: args.append('--committer-date-is-author-date')
    if ignore_date: args.append('--ignore-date')
    if resolvemsg is not None: args.append('--resolvemsg=%s' % resolvemsg)
    if ignore_space_change: args.append('--ignore-space-change')
    if ignore_whitesspace: args.append('--ignore-whitesspace')
    if whitespace is not None: args.append('--whitespace=%s' % whitespace)
    if remote_leading_slashes is not None: args.append('-p%i' % remote_leading_slashes)
    if ensure_surrounding is not None: args.append('-C%i' % ensure_surrounding)
    if directory is not None: args.append('--directory=%s' % directory)
    for path in exclude:
        args.append('--exclude=%s' % path)
    for path in include:
        args.append('--include=%s' % path)
    if reject: args.append('--reject')
    args.append('--')
    args += [mailboxes] if isinstance(mailboxes, str) else mailboxes
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_am_continue(resolvemsg = None, git_extra = [], read_output = False):
    args = git_extra + ['am', '--continue']
    if resolvemsg is not None: args.append('--resolvemsg=%s' % resolvemsg)
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_am_skip(resolvemsg = None, git_extra = [], read_output = False):
    args = git_extra + ['am', '--skip']
    if resolvemsg is not None: args.append('--resolvemsg=%s' % resolvemsg)
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_am_abort(resolvemsg = None, git_extra = [], read_output = False):
    args = git_extra + ['am', '--abort']
    if resolvemsg is not None: args.append('--resolvemsg=%s' % resolvemsg)
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


# TODO git-bisect
# TODO git-branch
# TODO git-bundle
# TODO git-checkout


def git_cherry_pick(commits
                    edit = False, extend_message = False, mainline = None, no_commit = False,
                    signoff = False, fast_forward = False, allow_empty = False,
                    allow_empty_message = False, keep_redundant_commits = False,
                    strategy = None, strategy_option = None,
                    git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('cherry-pick')
    if edit: args.append('--edit')
    if extend_message: args.append('-x')
    if mainline is not None:
        args.append('--mainline')
        args.append(mainline)
    if no_commit: args.append('--no-commit')
    if signoff: args.append('--signoff')
    if fast_forward: args.append('--ff')
    if allow_empty: args.append('--allow-empty')
    if allow_empty_message: args.append('--allow-empty-message')
    if keep_redundant_commits: args.append('--keep-redundant-commits')
    if strategy is not None: args.append('--strategy=%s' % strategy)
    if strategy_option is not None: args.append('--strategy-option=%s' % strategy_option)
    args += [commits] if isinstance(commits, str) else commits
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_cherry_pick_continue(git_extra = [], read_output = False):
    if read_output:
        return git(git_extra + ['cherry-pick', '--continue'])
    else:
        git_out(git_extra + ['cherry-pick', '--continue'])
        return None


def git_cherry_pick_quit(git_extra = [], read_output = False):
    if read_output:
        return git(git_extra + ['cherry-pick', '--quit'])
    else:
        git_out(git_extra + ['cherry-pick', '--quit'])
        return None


def git_cherry_pick_abort(git_extra = [], read_output = False):
    if read_output:
        return git(git_extra + ['cherry-pick', '--abort'])
    else:
        git_out(git_extra + ['cherry-pick', '--abort'])
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


# TODO git-commit
# TODO git-describe
# TODO git-diff
# TODO git-fetch
# TODO git-format-patch


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


# TODO git-grep


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


# TODO git-log
# TODO git-merge


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


# TODO git-notes
# TODO git-pull
# TODO git-push
# TODO git-rebase
# TODO git-reset


def git_revert(commits,
               edit = False, no_edit = False, no_commit = False, signoff = False,
               mainline = None, strategy = None, strategy_option = None,
               git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('revert')
    if edit: args.append('--edit')
    if no_edit: args.append('--no-edit')
    if no_commit: args.append('--no-commit')
    if signoff: args.append('--signoff')
    if strategy is not None: args.append('--strategy=%s' % strategy)
    if strategy_option is not None: args.append('--strategy_option=%s' % strategy_option)
    if mainline is not None:
        args.append('--mainline')
        args.append(mainline)
    args += [commits] if isinstance(commits, str) else commits
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_revert_continue(git_extra = [], read_output = False):
    if read_output:
        return git(git_extra + ['revert', '--continue'])
    else:
        git_out(git_extra + ['revert', '--continue'])
        return None


def git_revert_quit(git_extra = [], read_output = False):
    if read_output:
        return git(git_extra + ['revert', '--quit'])
    else:
        git_out(git_extra + ['revert', '--quit'])
        return None


def git_revert_abort(git_extra = [], read_output = False):
    if read_output:
        return git(git_extra + ['revert', '--abort'])
    else:
        git_out(git_extra + ['revert', '--abort'])
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


def git_shortlog(revision_range = None, paths = [],
                 numbered = False, summary = False, email = False,
                 format = None, width = None, indent1 = None, indent2 = None,
                 git_extra = [], read_output = False):
    args = []
    args += git_extra
    args.append('shortlog')
    if numbered: args.append('--numbered')
    if summary: args.append('--summary')
    if email: args.append('--email')
    if format is not None:
        if len(format) == 0:
            args.append('--format')
        else:
            args.append('--format=%s' % format)
    if (width is not None) or (indent1 is not None) or (indent2 is not None):
        arg = '-w'
        if width is not None:
            arg += '%i' % width
        else:
            arg += ','
        if indent1 is not None:
            arg += '%i' % indent1
        elif indent2 is not None:
            arg += ','
        if indent2 is not None:
            arg += '%i' % indent2
        args.append(arg)
    if revision_range is not None:
        args.append(revision_range)
    args.append('--')
    args += paths
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


def git_show(objects,
             pretty = None, abbrev_commit = False, no_abbrev_commit = False, oneline = False,
             encoding = None, notes = None, no_notes = False, show_signatures = False, verify = False,
             it_extra = [], read_output = False):
    if isinstance(objects, str):
        objects = [objects]
        args = []
    args += git_extra
    args.append('show')
    if pretty is not None: args.append('--pretty' if len(pretty) == 0 else ('--pretty=' % pretty))
    if abbrev_commit: args.append('--abbrev-commit')
    if no_abbrev_commit: args.append('--no-abbrev-commit')
    if oneline: args.append('--oneline')
    if encoding is not None: args.append('--encoding' if len(encoding) == 0 else ('--encoding=' % encoding))
    if notes is not None: args.append('--notes' if len(notes) == 0 else ('--notes=' % notes))
    if no_notes: args.append('--no-notes')
    if show_signature: args.append('--show-signature')
    if verify: args.append('--verify')
    args += objects
    if read_output:
        return git(args)
    else:
        git_out(args)
        return None


# TODO git-stash
# TODO git-status
# TODO git-submodule
# TODO git-tag

