#!/usr/bin/env python
import os
from jinja2_auto_gen_code.util.jobstores.event import Event


class ExecuteJob(object):

    class Templates:
        EVENT = 'event'
        ALL = [EVENT]

    class Builder:

        def __init__(self):
            self.available_model = {
                ExecuteJob.Templates.EVENT: Event
            }

        def get_available_model(self):
            return self.available_model.keys()

        def get_model(self, template):
            return self.available_model.get(os.path.splitext(template)[0], {})

        def load_config(self, template, config):
            model = self.get_model(template, {})
            return model().load_from_config(config)

        def create(self, template, variable, path):
            model = self.get_model(template)
            return model().run_macros(template, variable, path)
