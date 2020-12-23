import sys
import os


class Generator:
    def __init__(self, file_name):
        self.names = []
        self.urls = []
        self.sources = []
        self.file_name = file_name
        folder_name = file_name.split('/')
        self.task_name = folder_name[0]
        self.md_name = os.path.join(self.task_name, self.task_name + '.md')
        self.content = ''

    def read_input(self):
        self.sources.append([])
        with open(self.file_name, 'r') as f:
            for i, line in enumerate(f.readlines()):
                if i == 0:
                    self.names.append(line[:-1])
                elif i == 1:
                    self.urls.append(line)
                else:
                    self.sources[-1].append(line)

    def create_pretty_link(self, name):
        container = name.lower()
        container = container.replace(' ', '_')
        self.content += '+ [' + name + '](#' + container + ')' + '\n\n'
        return container

    def compose(self):
        self.content = '# ' + self.task_name + '\n\n'
        for name in self.names:
            self.create_pretty_link(name)

        for j in range(len(self.sources)):
            self.content += '## ' + self.names[j] + '\n\n'
            self.content += self.urls[j] + '\n\n'

            self.content += "```python" + '\n'
            for line in self.sources[j]:
                self.content += line
            self.content += "```" + '\n\n'

    def write_result(self):
        with open(self.md_name, 'w') as f:
            f.write(self.content)

    def read_md(self):
        read_file = False
        with open(self.md_name, 'r') as f:
            for line in f.readlines():
                if line.startswith('https:/'):
                    self.urls.append(line)
                elif line.startswith('##'):
                    self.names.append(line[3:-1])
                elif line.startswith('```python'):
                    read_file = True
                    self.sources.append([])
                elif line.startswith('```'):
                    read_file = False
                elif read_file:
                    self.sources[-1].append(line)

    def run(self):
        if os.path.exists(self.md_name):
            self.read_md()
        self.read_input()
        self.compose()
        self.write_result()


if __name__ == '__main__':
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        raise ValueError(f'File {input_file} does not exist')

    generator = Generator(sys.argv[1])
    generator.run()
