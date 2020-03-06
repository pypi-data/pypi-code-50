"""Main module."""
import glob
import re
from pathlib import Path
import json

def snake_to_camel(name):
    components = name.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

def convert(spec):
    # extract plugin name from the parent folder name
    name = Path(spec).parent.stem
    
    # path to Dockerfile
    docker_file = Path(spec).parent.joinpath('Dockerfile')
    
    with open(spec) as f:
        s = json.load(f)
        
        # Get input and output parameters from APEER module specification
        inputs = s['spec']['inputs']
        outputs = s['spec']['outputs']

        input_blocks = []
        input_blocks.append(f"""\
    --inputCollection)
    INPUTCOLLECTION="$2"
    shift # past argument
    shift # past value
    ;;
""")
        input_blocks.append(f"""\
    --outputCollection)
    OUTPUTCOLLECTION="$2"
    shift # past argument
    shift # past value
    ;;
""")
        converter_blocks = []
        wfe_input_json = {"WFE_output_params_file":"wfe_module_params_1_1.json"}
        
        ui = s.get('ui', {})
        
        wipp_inputs = []
        wipp_outputs = []
        wipp_ui = []
        
        # Add input and output WIPP collections
        wipp_inputs.append({
            "name": "inputCollection",
            "type": "collection",
            "description": "Input image collection for the plugin."
        })
        wipp_outputs.append({
            "name": "outputCollection",
            "type": "collection",
            "description": "Output image collection for the plugin"
        })
        wipp_ui.append({
            "key": "inputs.inputCollection",
            "title": "Image Collection: ",
            "description": "Pick a collection..."
        })
        
        # Get all input parameters and convert them to appropriate WIPP type
        for inp in inputs.keys():
            # Since underscores `_` are not allowed in WIPP parameter names,
            #  we need to rename them to lowerCamelCase
            new_name = snake_to_camel(inp)
            
            apeer_type = next(x for x in inputs[inp].keys() if 'type:' in x)
            default = None
            if 'default' in inputs[inp].keys():
                default = inputs[inp]['default']
            
            wipp_input_entry = {"name": new_name}
            
            # Convert APEER type to WIPP type or raise exception
            if apeer_type=='type:string':
                wipp_input_entry.update({"type": "string"})
            elif apeer_type=='type:file':
                wipp_input_entry.update({"type": "string"})
                converter_blocks.append(f"""{new_name.upper()}=${{INPUTCOLLECTION}}/${{{new_name.upper()}}}""")
            elif apeer_type=='type:number' or apeer_type=='type:integer':
                wipp_input_entry.update({"type": "number"})
            elif apeer_type=='type:choice_single':
                wipp_input_entry.update({
                    "type": "enum",
                    "options": {
                        "values": inputs[inp][apeer_type]
                    },
                })
            elif apeer_type=='type:choice_binary':
                wipp_input_entry.update({"type": "boolean"})
            elif apeer_type=='type:list[file]':
                wipp_input_entry.update({"type": "string"})
                converter_blocks.append(f"""\
append_to_list ${{{new_name.upper()}}} ${{INPUTCOLLECTION}}
{new_name.upper()}=$func_result
""")
            else:
                print('UNKNOWN INPUT TYPE', apeer_type)
                raise
            wipp_inputs.append(wipp_input_entry)
            
            # Create UI block in WIPP spec
            wipp_ui_entry = {
                "key": f"inputs.{new_name}",
                "title": new_name,
            }
            
            # check if label is provided in UI section of APEER spec
            if 'inputs' in ui: 
                if inp in ui['inputs']:
                    if 'label' in ui['inputs'][inp]:
                        wipp_ui_entry['title'] = ui['inputs'][inp]['label']
                    if 'description' in ui['inputs'][inp]:
                        wipp_ui_entry['description'] = ui['inputs'][inp]['description']
            wipp_ui.append(wipp_ui_entry)
            
            # Add new variable block to bash script
            input_blocks.append(f"""\
    --{new_name})
    {new_name.upper()}="$2"
    shift # past argument
    shift # past value
    ;;
""")
            wfe_input_json.update({inp: f"""${{{new_name.upper()}}}"""})


    # Extract execution command from Dockerfile
    # It could be CMD or ENTRYPOINT
    with open(docker_file) as f:
        lines = f.readlines()
        cmd_line_index, cmd = next((index, ' '.join(re.findall(r'"(.*?)"',x.strip('\n')))) for index,x in enumerate(lines) if x.startswith('CMD') or x.startswith('ENTRYPOINT'))
        lines.pop(cmd_line_index)
        lines.insert(cmd_line_index, 'COPY wipp_to_apeer.sh .\n')
        lines.insert(cmd_line_index+1, 'ENTRYPOINT [ "bash", "wipp_to_apeer.sh" ]\n')
        f.close()
    
    with open(Path(spec).parent.joinpath('Dockerfile_WIPP'), "w+") as f:
        for line in lines:
            f.write(line)
        f.close()
    
    script = f"""\
#!/bin/sh

append_to_list () {{
  IFS=', ' read -r -a array <<< "$1"
  func_result=$(printf ",\"$2/%s\"" "${{array[@]}}")
  func_result=[${{func_result:1}}]
}}

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
{''.join(input_blocks)}
esac
done

{''.join(converter_blocks)}

# Create symlink for output collection
ln -s $OUTPUTCOLLECTION /output

WFE_INPUT_JSON={json.dumps(json.dumps(wfe_input_json))}
export WFE_INPUT_JSON=$WFE_INPUT_JSON
sh -c "{cmd}"
"""
    
    with open(Path(spec).parent.joinpath('wipp_to_apeer.sh'), "w+") as wrapper:
        wrapper.write(script)
        wrapper.close()
        
    # Build the final plugin.json for WIPP
    wipp_spec = {
        "name": name,
        "version": "0.1.0",
        "title": f"Converted plugin: {name}",
        "institution": f"Converted plugin: {name}",
        "description": "",
        "containerId": f"ktaletsk/{name}:0.1.0",
        "inputs": wipp_inputs,
        "outputs": wipp_outputs,
        "ui": wipp_ui
    }
    with open(Path(spec).parent.joinpath('plugin.json'), "w+") as plugin_json:
        plugin_json.write(json.dumps(wipp_spec, indent=4))
        plugin_json.close()