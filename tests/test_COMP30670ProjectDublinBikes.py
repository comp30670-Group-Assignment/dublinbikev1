#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `COMP30670ProjectDublinBikes` package."""


import unittest
from click.testing import CliRunner

from COMP30670ProjectDublinBikes import COMP30670ProjectDublinBikes
from COMP30670ProjectDublinBikes import cli


class TestComp30670projectdublinbikes(unittest.TestCase):
    """Tests for `COMP30670ProjectDublinBikes` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'COMP30670ProjectDublinBikes.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
