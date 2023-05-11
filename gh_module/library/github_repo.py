#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

	 module = AnsibleModule(argument_spec={})
	 response = {"hello": "world"}
	 module.exit_json(changed=False, meta=response)

- name: Create a github Repo
      github_repo:
        github_auth_key: "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"
        username: "edpro99"
        name: "Hello-World"
        description: "This is your first repository"
        private: yes
        has_issues: no
        has_wiki: no
        has_downloads: no
        state: present
      register: result

	
def main():

    fields = {
        "github_auth_key": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "name": {"required": True, "type": "str"},
        "description": {"required": False, "type": "str"},
        "private": {"default": False, "type": "bool"},
        "has_issues": {"default": True, "type": "bool"},
        "has_wiki": {"default": True, "type": "bool"},
        "has_downloads": {"default": True, "type": "bool"},
        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
    }

	if __name__ == '__main__':
		    main()
