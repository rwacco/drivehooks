import tomllib
import os
from os.path import isfile, join
from quart import Quart, request

class Hook():
    def __init__(self, config):
        self.name = config['name']
        self.form_name = config['form_name']
        self.sheet_id = config['sheet_id']
        self.mapping = config['mapping']

    @staticmethod
    def new_hook(form_data):
        pass
    
    def save(self):
        pass

    def new_entry(self, form_data):
        pass


def load_hooks(path="hooks/"):
    hooks = {}
    hook_files = [f"{path + f}" for f in os.listdir(path) if isfile(join(path, f)) and f[0] != '_']
    for f_path in hook_files:
        hook = Hook(tomllib.load(f_path))
        hooks[hook.form_name] = hook


hooks = load_hooks()

app = Quart(__name__)


@app.route('/')
async def root():
    form_data = dict(request.form)
    hook = hooks.get(form_data["Form name"])

    if not hook:
        pass


app.run(host="0.0.0.0", port=8030)
    
    