import yaml
import os

pattern = {'my_project':
        [{'settings': [
            '__init__.py', 'dev.py', 'prod.py'
        ],

        },
            {'mainapp': [
                '__init.py__', 'models.py', 'vievs.py', {'templates': [{
                    'mainapp': ['base.html', 'index.html']}]
                }]},
            {'authapp': ['__init__.py', 'models.py', 'vievs.py', {'tempales': [{
                'authapp': ['base.html', 'index.html']}]
            }
                         ]
             }
        ]
}

with open('config.yaml', 'w') as file:
    file.write(yaml.dump(pattern))

with open('config.yaml') as fin:
    data = yaml.safe_load(fin)


def create_data(data):
    for folder, tmps in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for tmp in tmps:
            if isinstance(tmp, dict):
                create_data(tmp)
            else:
                if not os.path.exists(tmp):
                    if '.' in tmp:
                        with open(tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')


create_data(data)
