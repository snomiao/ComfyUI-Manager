# ## Description

# For each command, the following scenarios need to be tested:

# - When a node is registered in CNR
#     - Classified as CNR or nightly
#     - `<node-id>@nightly`
#     - `<node-id>@<cnr version>`
#     - `<node-id>@latest`

# - When a node is not registered in CNR
#     - Classified as unknown
#     - `<node-id>@unknown`
#     - unknown is identified as a separate node even if its ID overlaps with a CNR node

# Installation status

# - installed
#     - enabled:
#         - CNR and nightly nodes cannot be enabled simultaneously
#     - disabled
#         - CNR and nightly nodes can be in a disabled state simultaneously
# - not-installed

# Installation state

# - managed nodes
#     - enabled
#         - `custom_nodes/<node-id>@nightly`
#         - `custom_nodes/<node-id>@<cnr version>`
#             - NOTE1: must contain a '.tracking' file
#             - NOTE2: <cnr version> cannot be `latest`
#         - `custom_nodes/<node-id>@unknown`
#     - disabled
#         - `custom_nodes/.disabled/<node-id>@nightly`
#         - `custom_nodes/.disabled/<node-id>@<cnr version>`
#             - NOTE1: must contain a '.tracking' file
#             - NOTE2: <cnr version> cannot be `latest`
#         - `custom_nodes/.disabled/<node-id>@unknown`
# - unmanaged nodes
#     - `custom_nodes/<repo name>` # nightly
#     - `custom_nodes/<repo name>` # unknown
#     - `custom_nodes/<repo name>.disabled` # nightly
#     - `custom_nodes/<repo name>.disabled` # unknown
# - broken nodes (ComfyUI-Manager will not handle this)
#     - `custom_nodes/.disabled/<node-id>` # without <cnr version>
#     - `custom_nodes/.disabled/<node-id>@<version spec>.disabled` # .disabled suffix in .disabled dir
#     - `custom_nodes/<node-id>@<version spec>` # missing .tracking file in custom_nodes/<node-id>@<version spec>
#     - `custom_nodes/.disabled/<node-id>@<version spec>` # missing .tracking file in custom_nodes/<node-id>@<version spec>
#     - `custom_nodes/<node-id>@<version spec>.disabled` # .disabled suffix for managed nodes
# - When using only <node-id> without a version
#     - Priority for install/reinstall/uninstall
#         - Priority 1: CNR latest
#         - Priority 2: unknown
#     - For commands like enable, disable, and update that target already installed nodes
#         - disable:
#             - Priority 1: CNR or nightly in enabled state
#             - Priority 2: unknown in enabled state
#         - enable:
#             - Priority 1: CNR in disabled state
#             - Priority 2: nightly in disabled state
#             - Priority 3: unknown in disabled state
#         - update:
#             - Priority 1: CNR or nightly in enabled state
#             - Priority 2: unknown in enabled state

# ---

# For each command, the following scenarios need to be tested:

commands = 'cm-cli' #TODO

# - When a node is registered in CNR
#     - Classified as CNR or nightly
#     - `<node-id>@nightly`
#     - `<node-id>@<cnr version>`
#     - `<node-id>@latest`

# - When a node is not registered in CNR
#     - Classified as unknown
#     - `<node-id>@unknown`
#     - unknown is identified as a separate node even if its ID overlaps with a CNR node

# Installation status

# - installed
#     - enabled:
#         - CNR and nightly nodes cannot be enabled simultaneously
#     - disabled
#         - CNR and nightly nodes can be in a disabled state simultaneously
# - not-installed

# Installation state

# - managed nodes
#     - enabled
#         - `custom_nodes/<node-id>@nightly`
#         - `custom_nodes/<node-id>@<cnr version>`
#             - NOTE1: must contain a '.tracking' file
#             - NOTE2: <cnr version> cannot be `latest`
#         - `custom_nodes/<node-id>@unknown`
#     - disabled
#         - `custom_nodes/.disabled/<node-id>@nightly`
#         - `custom_nodes/.disabled/<node-id>@<cnr version>`
#             - NOTE1: must contain a '.tracking' file
#             - NOTE2: <cnr version> cannot be `latest`
#         - `custom_nodes/.disabled/<node-id>@unknown`
# - unmanaged nodes
#     - `custom_nodes/<repo name>` # nightly
#     - `custom_nodes/<repo name>` # unknown
#     - `custom_nodes/<repo name>.disabled` # nightly
#     - `custom_nodes/<repo name>.disabled` # unknown
# - broken nodes (ComfyUI-Manager will not handle this)
#     - `custom_nodes/.disabled/<node-id>` # without <cnr version>
#     - `custom_nodes/.disabled/<node-id>@<version spec>.disabled` # .disabled suffix in .disabled dir
#     - `custom_nodes/<node-id>@<version spec>` # missing .tracking file in custom_nodes/<node-id>@<version spec>
#     - `custom_nodes/.disabled/<node-id>@<version spec>` # missing .tracking file in custom_nodes/<node-id>@<version spec>
#     - `custom_nodes/<node-id>@<version spec>.disabled` # .disabled suffix for managed nodes
# - When using only <node-id> without a version
#     - Priority for install/reinstall/uninstall
#         - Priority 1: CNR latest
#         - Priority 2: unknown
#     - For commands like enable, disable, and update that target already installed nodes
#         - disable:
#             - Priority 1: CNR or nightly in enabled state
#             - Priority 2: unknown in enabled state
#         - enable:
#             - Priority 1: CNR in disabled state
#             - Priority 2: nightly in disabled state
#             - Priority 3: unknown in disabled state
#         - update:
#             - Priority 1: CNR or nightly in enabled state
#             - Priority 2: unknown in enabled state

# ---

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
