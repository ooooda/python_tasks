import sys
import os


def remove(x):
    x = list(x)
    result = ''
    for i in range(len(x)):
        if x[i] == ' ':
            result += '-'
        else:
            result += x[i]
    return result


if __name__ == '__main__':
    names = []
    urls = []
    sources = []
    argument = sys.argv
    if os.path.exists(argument[-1]):
        for el in os.listdir(argument[-1]):
            names.append(el)
            helper = []
            with open(argument[-1] + '/' + el, 'r') as f:
                for i, line in enumerate(f):
                    if i == 0:
                        urls.append(line)
                    else:
                        helper.append(line)
            sources.append(helper)
        with open(argument[-1] + '.md', 'w') as f:
            x = argument[-1].split('/')
            f.write('# ' + x[-1])
            f.write('\n\n')
            for i in range(len(names)):
                x = names[i].lower()
                x = remove(x)
                f.write('+ [' + names[i][:-3] + '](#' + x[:-3] + ')')
                f.write('\n\n')
            for i in range(len(names)):
                f.write('## ' + names[i][:-3])
                f.write('\n\n')
                f.write(urls[i][2:])
                f.write('\n\n')
                f.write("```python")
                f.write('\n\n')
                for el in sources[i]:
                    if el == '\n':
                        f.write('\n\n')
                    else:
                        f.write(el)
                f.write('\n\n')
                f.write("```")
                f.write('\n\n')
    else:
        print("No such folder")


