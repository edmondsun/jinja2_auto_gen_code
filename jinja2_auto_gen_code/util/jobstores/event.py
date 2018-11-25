#!/usr/bin/env python
import copy
import re
import os
import six
import yaml
import collections
import distutils.dir_util
from jinja2_auto_gen_code.util.jobstores.base import BaseJobStore


class Event(BaseJobStore):

    def __init__(self):
        super(Event, self).__init__()

    def run_macros(self, template, variables, output_file):
        result = self.rendered_template(
            self.env.get_template(template),
            variables,
            os.path.join(
                self.render_path, output_file
            )
        )
        return result

    def rendered_template(self, template, variables, output_file):
        try:
            distutils.dir_util.mkpath(os.path.dirname(output_file))
        except Exception as e:
            print e

        data = {}
        with open(os.path.join(self.var_path, variables), 'r') as f:
            data = yaml.safe_load(f)

        conf = sorted(data, key=lambda x: x.get('id'), reverse=False)
        config = self._update_conf(conf)

        for index, class_conf in enumerate(config):
            variables = self._parse_vars(conf[index])
            class_vars = { i : '' for i in variables}

            with open(output_file,'a') as f:
                f.write(
                    template.render(
                        evt_class=class_conf, 
                        evt_vars=class_vars, 
                        parent_args='BaseEvt',
                        msg=class_conf['msg']
                    )
                )
        return output_file

    def _update_conf(self, config):
        info = []
        conf = copy.deepcopy(config)

        for doc in conf:
            msg_list = self._parse_vars(doc)
            msg = doc.get('msg')
            for m in msg_list:
                msg = re.sub("\\[(%s)\\]" %m, "[{%s}]" %m, msg)
            doc.update({'msg': msg})
            info.append(doc)
        return info

    def _parse_vars(self, config):
        return  re.findall("\\[(.*?)\\]", str(config.get('msg')))

