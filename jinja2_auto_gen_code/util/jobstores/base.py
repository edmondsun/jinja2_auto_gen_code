#!/usr/bin/env python
import six
import abc
from jinja2 import Environment, FileSystemLoader


class BaseJobStore(six.with_metaclass(abc.ABCMeta)):

    def __init__(
        self,
        var_path="vars/",
        render_path="renders/",
        template_path="templates/", env=None
    ):
        self.var_path = var_path
        self.render_path = render_path
        self.template_path = template_path
        self.env = Environment(
            loader=FileSystemLoader(template_path),
            trim_blocks=True,
            lstrip_blocks=True,
            extensions=['jinja2.ext.do']
        )

    @abc.abstractmethod
    def run_macros():
        pass
