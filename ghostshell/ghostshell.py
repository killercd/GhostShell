import yaml
from jinja2 import Template



def find_by_opt(opt, template_list):
    for tmpl in template_list:
        if opt == tmpl["choice_c"]:
            return tmpl
    return None

def main():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    ip_address = config['reverse_shell_config']['r_host']
    port = config['reverse_shell_config']['r_port']    

    print("#### CONFIGURATION ####")
    print(f"IPADDRESS: {ip_address}")
    print(f"PORT: {port}")
    print("")
    print("")


  
    exit_code = "e"
    choice = ""
    while choice!=exit_code:
        for payload in config["payload_template"]:
            print(f"[{payload["choice_c"]}] {payload["name"]}")
        print(f"[e] exit")

        choice = str(input("> "))
        template = find_by_opt(choice, config["payload_template"])
        if template:
            code_template = Template(template["code"])
            payload = code_template.render(r_host=ip_address, r_port=port)
            print(payload)
if __name__ == '__main__':
    main()