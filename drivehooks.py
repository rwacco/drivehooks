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

    def __str__(self) -> str:
        pass


def load_hooks(path="hooks/"):
    hooks = {}
    hook_files = [f"{path + f}" for f in os.listdir(path) if isfile(join(path, f)) and f[0] != '_']
    for f_path in hook_files:
        with open(f_path, 'rb') as f: 
            hook = Hook(tomllib.load(f))
        hooks[hook.form_name] = hook
    return hooks


hooks = load_hooks()
print(hooks)

app = Quart(__name__)


@app.route('/', methods=["POST"])
async def root():
    form_data = dict(await request.form)
    key = request.args.get("key") 

    print(form_data)
    print(form_data.keys())
    print(key)

    hook = hooks.get(form_data["form_name"])

    # no existing hook registered
    if not hook:
        pass

    return "kaas"


app.run(host="0.0.0.0", port=8030)
    
    