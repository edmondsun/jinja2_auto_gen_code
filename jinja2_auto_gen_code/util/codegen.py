#!/usr/bin/env python

import os
import argparse
import pdb

from jinja2_auto_gen_code.util.tasks.executer import ExecuteJob


class ConfigKeys:

    FOLDER = {
        '.py': 'python',
        '.yml': 'yml',
        '.xml': 'xml',
        '.json': 'json',
    }

def main():
    description_text = """
    codegen is a code generator tool based on Jinja2 template engine

    Usage: codegen [OPTIONS] [TEMPLATE_VARIABLES] [TEMPLATE]

    --option:
        -e, --extension FILENAME          Place the rendered template into FILENAME
        -v, --variable  FILENAME          Read template variables from FILENAME
        -t, --template  FILENAME          Read template model from FILENAME

    Example:
        ./codegen.py -e evt_i18n.py -v evt_i18n_en_us.yml -t eventlog.j2 (render/python/evt_i18n.py)
        ./codegen.py -v schedule.yml -t schedule.j2                      (render/others/schedule)
    """
    parser = argparse.ArgumentParser(
        description=description_text,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-e', '--extension', help='rendered file')
    parser.add_argument('-v', '--variable', help='variable file, currently only support yml')
    parser.add_argument('-t', '--template', help='template file')
    args = parser.parse_args()

    filename = args.extension
    variable = args.variable
    template = args.template

    conf = ConfigKeys()

    if not filename:
        filename = os.path.splitext(variable)[0]

    # file extension ex: .py, .yml, .xml, .json
    file_extension = os.path.splitext(filename)[1]
    # classify output file directory ex: python, yml, xlm, json, others
    directory = conf.FOLDER.get(file_extension, 'others')
    # absolute file path, ex: python/evt_i18n.py, others/schedule
    absolute_file = os.path.join(directory, filename)
    # generate the file
    exec_result = ExecuteJob.Builder().create(
        template=template,
        variable=variable,
        path=absolute_file
    )
    print exec_result

if __name__ == '__main__':
    main()
