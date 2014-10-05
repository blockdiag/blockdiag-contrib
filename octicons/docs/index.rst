=========================
blockdiagcontrib-octicons
=========================
A plugin for `blockdiag` that provides octicons as background/icon of nodes.

examples
=========
`blockdiagcontrib-octicons` detects background and icon attributes starts with 'octicon://',
and converts it as octicons_ .

.. _octicons: https://octicons.github.com/

Example::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github"];
     B [icon = "octicon://cloud-upload?color=red"];
     A -> B;
   }

.. blockdiag::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github"];
     B [icon = "octicon://cloud-upload?color=red"];
     A -> B;
   }

see results at http://pythonhosted.org//blockdiagcontrib-octicons/

Requirements
============
* blockdiag 1.4.3 or later

Copyright of octicons.ttf
=========================
\(c) 2012-2014 GitHub

License
=======
Apache License 2.0

.. note::

   octicons.ttf is licensed under SIL OFL 1.1 (http://scripts.sil.org/OFL)

Usage
=====

At first, load `octicons` plugin with plugin statement.
And then, you can use `octicon://` URI to background and icon attributes::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github"];
   }

`octicon://` URI accepts two options: size and color

`color` option changes color of octicon::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?color=red"];
   }

.. blockdiag::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?color=red"];
   }

`size` option changes size of octicon. you can choose from large, normal, small and pixels::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?size=large"];
     B [label = "", background = "octicon://mark-github?size=normal"];
     C [label = "", background = "octicon://mark-github?size=small"];
     D [label = "", background = "octicon://mark-github?size=8"];
   }

.. blockdiag::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?size=large"];
     B [label = "", background = "octicon://mark-github?size=normal"];
     C [label = "", background = "octicon://mark-github?size=small"];
     D [label = "", background = "octicon://mark-github?size=8"];
   }

name of octicons
=================


.. list-table::
   :header-rows: 0

   * - octicon://code

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://code']; }

     - octicon://log-out

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://log-out']; }

     - octicon://trashcan

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://trashcan']; }

   * - octicon://screen-full

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://screen-full']; }

     - octicon://graph

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://graph']; }

     - octicon://comment-discussion

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://comment-discussion']; }

   * - octicon://repo-pull

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-pull']; }

     - octicon://file-media

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-media']; }

     - octicon://terminal

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://terminal']; }

   * - octicon://gist-fork

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://gist-fork']; }

     - octicon://color-mode

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://color-mode']; }

     - octicon://sign-out

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://sign-out']; }

   * - octicon://repo-delete

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-delete']; }

     - octicon://stop

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://stop']; }

     - octicon://file-text

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-text']; }

   * - octicon://repo

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo']; }

     - octicon://hubot

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://hubot']; }

     - octicon://cloud-download

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://cloud-download']; }

   * - octicon://gist-private

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://gist-private']; }

     - octicon://settings

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://settings']; }

     - octicon://git-pull-request

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-pull-request']; }

   * - octicon://tag-add

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://tag-add']; }

     - octicon://microscope

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://microscope']; }

     - octicon://x

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://x']; }

   * - octicon://chevron-down

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://chevron-down']; }

     - octicon://mirror-public

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mirror-public']; }

     - octicon://search-save

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://search-save']; }

   * - octicon://arrow-down

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-down']; }

     - octicon://arrow-small-right

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-small-right']; }

     - octicon://sync

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://sync']; }

   * - octicon://pulse

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://pulse']; }

     - octicon://fold

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://fold']; }

     - octicon://comment-add

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://comment-add']; }

   * - octicon://calendar

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://calendar']; }

     - octicon://hourglass

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://hourglass']; }

     - octicon://chevron-left

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://chevron-left']; }

   * - octicon://clock

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://clock']; }

     - octicon://move-up

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://move-up']; }

     - octicon://move-left

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://move-left']; }

   * - octicon://primitive-dot

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://primitive-dot']; }

     - octicon://person-follow

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://person-follow']; }

     - octicon://mark-github

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mark-github']; }

   * - octicon://key

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://key']; }

     - octicon://file-binary

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-binary']; }

     - octicon://search

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://search']; }

   * - octicon://device-camera

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://device-camera']; }

     - octicon://credit-card

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://credit-card']; }

     - octicon://diff-removed

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://diff-removed']; }

   * - octicon://arrow-right

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-right']; }

     - octicon://jersey

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://jersey']; }

     - octicon://comment

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://comment']; }

   * - octicon://primitive-square

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://primitive-square']; }

     - octicon://markdown

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://markdown']; }

     - octicon://unfold

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://unfold']; }

   * - octicon://heart

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://heart']; }

     - octicon://diff

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://diff']; }

     - octicon://tools

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://tools']; }

   * - octicon://git-pull-request-abandoned

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-pull-request-abandoned']; }

     - octicon://mail-read

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mail-read']; }

     - octicon://eye

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://eye']; }

   * - octicon://file-directory

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-directory']; }

     - octicon://beer

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://beer']; }

     - octicon://logo-github

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://logo-github']; }

   * - octicon://three-bars

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://three-bars']; }

     - octicon://diff-modified

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://diff-modified']; }

     - octicon://megaphone

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://megaphone']; }

   * - octicon://pencil

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://pencil']; }

     - octicon://file-directory-create

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-directory-create']; }

     - octicon://gist

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://gist']; }

   * - octicon://tag-remove

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://tag-remove']; }

     - octicon://list-ordered

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://list-ordered']; }

     - octicon://git-branch

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-branch']; }

   * - octicon://diff-ignored

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://diff-ignored']; }

     - octicon://ruby

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://ruby']; }

     - octicon://gist-new

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://gist-new']; }

   * - octicon://eye-unwatch

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://eye-unwatch']; }

     - octicon://diff-added

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://diff-added']; }

     - octicon://repo-force-push

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-force-push']; }

   * - octicon://repo-clone

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-clone']; }

     - octicon://dashboard

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://dashboard']; }

     - octicon://history

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://history']; }

   * - octicon://alignment-unalign

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://alignment-unalign']; }

     - octicon://circuit-board

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://circuit-board']; }

     - octicon://lock

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://lock']; }

   * - octicon://sign-in

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://sign-in']; }

     - octicon://tag

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://tag']; }

     - octicon://git-commit

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-commit']; }

   * - octicon://file-symlink-file

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-symlink-file']; }

     - octicon://triangle-right

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://triangle-right']; }

     - octicon://clippy

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://clippy']; }

   * - octicon://repo-push

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-push']; }

     - octicon://split

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://split']; }

     - octicon://person-add

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://person-add']; }

   * - octicon://briefcase

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://briefcase']; }

     - octicon://repo-forked

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-forked']; }

     - octicon://alert

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://alert']; }

   * - octicon://law

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://law']; }

     - octicon://move-down

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://move-down']; }

     - octicon://screen-normal

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://screen-normal']; }

   * - octicon://arrow-small-up

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-small-up']; }

     - octicon://gist-secret

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://gist-secret']; }

     - octicon://database

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://database']; }

   * - octicon://star-add

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://star-add']; }

     - octicon://person

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://person']; }

     - octicon://organization

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://organization']; }

   * - octicon://rocket

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://rocket']; }

     - octicon://mute

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mute']; }

     - octicon://arrow-small-down

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-small-down']; }

   * - octicon://keyboard

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://keyboard']; }

     - octicon://file-symlink-directory

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-symlink-directory']; }

     - octicon://alignment-aligned-to

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://alignment-aligned-to']; }

   * - octicon://repo-create

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-create']; }

     - octicon://device-camera-video

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://device-camera-video']; }

     - octicon://location

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://location']; }

   * - octicon://alignment-align

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://alignment-align']; }

     - octicon://mail

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mail']; }

     - octicon://move-right

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://move-right']; }

   * - octicon://diff-renamed

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://diff-renamed']; }

     - octicon://mention

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mention']; }

     - octicon://milestone

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://milestone']; }

   * - octicon://file-submodule

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-submodule']; }

     - octicon://jump-up

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://jump-up']; }

     - octicon://gift

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://gift']; }

   * - octicon://server

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://server']; }

     - octicon://steps

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://steps']; }

     - octicon://issue-opened

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://issue-opened']; }

   * - octicon://octoface

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://octoface']; }

     - octicon://file-code

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-code']; }

     - octicon://telescope

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://telescope']; }

   * - octicon://globe

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://globe']; }

     - octicon://triangle-left

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://triangle-left']; }

     - octicon://arrow-left

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-left']; }

   * - octicon://mirror

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mirror']; }

     - octicon://home

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://home']; }

     - octicon://git-branch-create

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-branch-create']; }

   * - octicon://device-mobile

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://device-mobile']; }

     - octicon://playback-pause

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://playback-pause']; }

     - octicon://eye-watch

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://eye-watch']; }

   * - octicon://mirror-private

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mirror-private']; }

     - octicon://list-unordered

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://list-unordered']; }

     - octicon://circle-slash

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://circle-slash']; }

   * - octicon://ellipsis

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://ellipsis']; }

     - octicon://file-pdf

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-pdf']; }

     - octicon://squirrel

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://squirrel']; }

   * - octicon://git-compare

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-compare']; }

     - octicon://horizontal-rule

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://horizontal-rule']; }

     - octicon://git-branch-delete

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-branch-delete']; }

   * - octicon://issue-closed

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://issue-closed']; }

     - octicon://plug

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://plug']; }

     - octicon://git-merge

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-merge']; }

   * - octicon://package

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://package']; }

     - octicon://issue-reopened

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://issue-reopened']; }

     - octicon://jump-down

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://jump-down']; }

   * - octicon://file-add

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-add']; }

     - octicon://plus

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://plus']; }

     - octicon://mortar-board

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mortar-board']; }

   * - octicon://rss

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://rss']; }

     - octicon://puzzle

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://puzzle']; }

     - octicon://inbox

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://inbox']; }

   * - octicon://jump-right

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://jump-right']; }

     - octicon://zap

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://zap']; }

     - octicon://bookmark

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://bookmark']; }

   * - octicon://light-bulb

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://light-bulb']; }

     - octicon://git-fork-private

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://git-fork-private']; }

     - octicon://question

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://question']; }

   * - octicon://triangle-up

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://triangle-up']; }

     - octicon://link-external

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://link-external']; }

     - octicon://file-zip

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://file-zip']; }

   * - octicon://chevron-right

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://chevron-right']; }

     - octicon://checklist

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://checklist']; }

     - octicon://broadcast

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://broadcast']; }

   * - octicon://playback-rewind

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://playback-rewind']; }

     - octicon://link

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://link']; }

     - octicon://jump-left

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://jump-left']; }

   * - octicon://mail-reply

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://mail-reply']; }

     - octicon://bug

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://bug']; }

     - octicon://device-desktop

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://device-desktop']; }

   * - octicon://info

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://info']; }

     - octicon://versions

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://versions']; }

     - octicon://unmute

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://unmute']; }

   * - octicon://flame

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://flame']; }

     - octicon://radio-tower

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://radio-tower']; }

     - octicon://browser

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://browser']; }

   * - octicon://arrow-up

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-up']; }

     - octicon://pin

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://pin']; }

     - octicon://dash

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://dash']; }

   * - octicon://check

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://check']; }

     - octicon://gear

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://gear']; }

     - octicon://repo-sync

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://repo-sync']; }

   * - octicon://book

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://book']; }

     - octicon://log-in

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://log-in']; }

     - octicon://cloud-upload

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://cloud-upload']; }

   * - octicon://triangle-down

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://triangle-down']; }

     - octicon://playback-fast-forward

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://playback-fast-forward']; }

     - octicon://star

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://star']; }

   * - octicon://quote

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://quote']; }

     - octicon://podium

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://podium']; }

     - octicon://playback-play

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://playback-play']; }

   * - octicon://remove-close

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://remove-close']; }

     - octicon://star-delete

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://star-delete']; }

     - octicon://arrow-small-left

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://arrow-small-left']; }

   * - octicon://paintcan

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://paintcan']; }

     - octicon://no-newline

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://no-newline']; }

     - octicon://chevron-up

       .. blockdiag::

          { plugin octicons; A [label = '', background = 'octicon://chevron-up']; }
