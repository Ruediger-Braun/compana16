import subprocess

def rst2html(target, source, env):
    subprocess.call(['rst2html', '-t', '--stylesheet-path=style_css',
                     '--output-encoding=ascii:xmlcharrefreplace',
                     str(source[0])],
                    stdout=open(str(target[0]), 'w'))

env = Environment()
rst2html = Builder(action=rst2html)
env.Append(BUILDERS = {'rst2html': rst2html })

env.rst2html('befehle.html', 'befehle.rest')


